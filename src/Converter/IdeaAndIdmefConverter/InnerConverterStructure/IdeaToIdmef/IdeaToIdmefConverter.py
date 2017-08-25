import os
import time
from json import JSONDecodeError

from IdeaAndIdmefConverter.InnerConverterStructure.InputConverter import InputConverter

import IdeaAndIdmefConverter.InnerConverterStructure.Helper.Exceptions as Exceptions


class IdeaToIdmefConverter(InputConverter):
    """
    Class which converts whole IDEA file to IDMEF file or whole IDEA string to IDMEF string
    """

    def __init__(self, input_parser,  message_converter, value_converter, exporter, time_output_file=None):
        """
        Constructor of IdeaToIdmefConverter

        :param input_parser: instance of IdeaParser class
        :param message_converter: instance of IdeaToIdmefMessageConverter class
        :param value_converter: instance of IdeaToIdmefValueConverter
        :param exporter: instance of IdmefExporter
        :param time_output_file: file for saving time (just for tests, later will be deleted)
        """
        InputConverter.__init__(self, input_parser, message_converter, value_converter, exporter)
        self.time_output_file = time_output_file
        self.start_written = False
        self.end_written = False

    def convert_file(self, parse_once=False, prettify=False, idmef_namespace=False):
        """
        Method which takes IDEA input file and converts data from it to IDMEF output file

        :param parse_once: boolean, if true, in file is only single IDEA message with any indentation, otherwise in one
                           line can be just one message
        :param prettify: boolean, if true, XML data in output file will be prettified (indentation), otherwise message
                         will be written to one line
        :param idmef_namespace: boolean, if true, idmef namespace, as is mentioned in rfc4765 will be included in whole
                                message (and all messages, if there is more of them in file)
        :raises IdeaToIdmefValueConverterException: when values cannot be converted properly
        :raises IdeaToIdmefMessageConverterException: when data cannot be converted properly from dict to elementtree
        :raises JsonParserException: when message could not be parsed, because message is not valid JSON
        """
        messages_time = []
        all_time_before = time.process_time()
        message_number = 1
        try:
            if parse_once:
                message_time_before = time.process_time()
                self.exporter.write_starttag_tofile("")
                self.exporter.write_starttag_tounconverted("")
                input_message = self.input_parser.parse_file_together()
                input_message_conv_values = self.convert_values(input_message, message_number)
                output_message = self.convert_message(input_message_conv_values, idmef_namespace, message_number)
                self.exporter.export_message(output_message, prettify)
                messages_time.append(str(time.process_time() - message_time_before) + os.linesep)
            else:
                self.exporter.write_starttag_tofile("IDMEF-Messages")
                self.exporter.write_starttag_tounconverted("UnconvertableFromIDEA")
                self.start_written = True
                for input_message in self.input_parser.parse_file_partially():
                    message_time_before = time.process_time()
                    input_message_conv_values = self.convert_values(input_message, message_number)
                    output_message = self.convert_message(input_message_conv_values, idmef_namespace, message_number)
                    self.exporter.export_message(output_message, prettify)
                    messages_time.append(str(time.process_time() - message_time_before) + os.linesep)
                    message_number += 1
                self.exporter.write_endtag_tofile("IDMEF-Messages")
                self.exporter.write_endtag_tounconverted("UnconvertableFromIDEA")
                self.end_written = True
        except JSONDecodeError:
            raise Exceptions.JsonParserException(
                "Message number " + str(message_number) + " is not valid JSON and could not be parsed, parser has "
                "thrown this: " + repr(JSONDecodeError)
            )
        all_time_after = time.process_time() - all_time_before
        if self.time_output_file:
            self.print_process_times(self.time_output_file, all_time_after, messages_time)

    def is_starttag_written(self):
        return self.start_written

    def is_endtag_written(self):
        return self.end_written

    def convert_string(self, idmef_namespace=False):
        """
        Takes string with single IDEA message and returns string with IDMEF


        :param idmef_namespace: boolean, if true, idmef namespace, as is mentioned in rfc4765 will be included in whole
                                message (and all messages, if there is more of them in file)
        :raises IdeaToIdmefValueConverterException: when values cannot be converted properly
        :raises IdeaToIdmefMessageConverterException: when data cannot be converted properly from dict to elementtree
        """
        message_number = 1
        try:
            input_message = self.input_parser.parse_string()
            input_message_conv_values = self.convert_values(input_message, message_number)
            output_message = self.convert_message(input_message_conv_values, idmef_namespace, message_number)
            return self.exporter.export_message_tostring(output_message)
        except JSONDecodeError:
            raise Exceptions.JsonParserException(
                "Message number " + str(message_number) + " is not valid JSON and could not be parsed, parser has "
                "thrown this: " + repr(JSONDecodeError)
            )

    def convert_values(self, input_message, message_number):
        """
        Method which call convert_values method from value_converter and throw exception in case that it crashes

        :param input_message: dict input for value conversion
        :return: converted dict
        :raises IdeaToIdmefValueConverterException: when values cannot be converted properly
        """
        try:
            return self.value_converter.convert_values(input_message)
        except ValueError as value_error:
            raise Exceptions.IdeaToIdmefValueConverterException(
                "Message number " + str(message_number) + " is not valid so much, that it is not possible to convert "
                "value types from IDEA to IDMEF message and this error was thrown: " + repr(value_error)
            )
        except TypeError as type_error:
            raise Exceptions.IdeaToIdmefValueConverterException(
                "Message number " + str(message_number) + " is not valid so much, that it is not possible to convert "
                "value types from IDEA to IDMEFmessage and this error was thrown: " + repr(type_error)
            )

    def convert_message(self, input_message, idmef_namespace, message_number):
        """
        Method which call modify_data method from message_converter and throw exception in case that it crashes

        :param input_message: dict input for message conversion
        :param idmef_namespace: boolean, if true, idmef namespace, as is mentioned in rfc4765 will be included in whole
                                message (and all messages, if there is more of them in file)
        :return: converted elementtree
        :raises IdeaToIdmefMessageConverterException: when data cannot be converted properly from dict to elementtree
        """
        try:

            return self.message_converter.modify_data(input_message, idmef_namespace,
                                                      self.exporter.rest_values_file_exists())
        except ValueError as value_error:
            raise Exceptions.IdeaToIdmefMessageConverterException(
                "Message number " + str(message_number) + " is not valid so much, that it is not possible to convert "
                "message from dict to elementtree and this exception was thrown: " + repr(value_error)
            )
        except TypeError as type_error:
            raise Exceptions.IdeaToIdmefMessageConverterException(
                "Message number " + str(message_number) + " is not valid so much, that it is not possible to convert "
                "message from dict to elementtree and this exception was thrown: " + repr(type_error)
            )

    def correct_file_after_interruption(self):
        """
        Encloses file with correct tags
        """
        if self.start_written and not self.end_written:
            self.exporter.write_endtag_tofile("IDMEF-Messages")
            self.exporter.write_endtag_tounconverted("AllUnconvertedFromIDEA")

    def print_process_times(self, output_file, all_time, message_times):
        """
        Writes time of conversion to file

        :param output_file: file, where time will be written
        :param all_time: string with value of all time of conversion
        :param message_times: list with time values of conversion of specific messages
        """
        output_file.write("Conversion time of each message: ")
        output_file.write(os.linesep)
        output_file.write(''.join(message_times))
        output_file.write(os.linesep)
        output_file.write("Time of all conversion:")
        output_file.write(os.linesep)
        output_file.write(str(all_time) + os.linesep)
