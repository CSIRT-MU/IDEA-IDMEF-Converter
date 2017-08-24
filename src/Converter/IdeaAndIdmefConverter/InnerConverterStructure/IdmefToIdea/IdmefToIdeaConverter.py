import os
import time
from xml.etree.ElementTree import ParseError

from IdeaAndIdmefConverter.InnerConverterStructure.InputConverter import InputConverter

import IdeaAndIdmefConverter.InnerConverterStructure.Helper.Exceptions as Exceptions


class IdmefToIdeaConverter(InputConverter):
    """
    Class which converts whole IDMEF file to IDEA file or whole IDMEF string to IDEA string
    """

    def __init__(self, input_parser,  message_converter, value_converter, exporter, time_output_file=None):
        """
        :param input_parser: instance of IdeaParser
        :param message_converter: instance of IdmefToIdeaMessageConverter
        :param value_converter: instance of IdmefToIdeaValueConverter
        :param exporter: instance of IdeaExporter
        :param time_output_file:
        """
        InputConverter.__init__(self, input_parser, message_converter, value_converter, exporter)
        self.time_output_file = time_output_file

    def convert_file(self, prettify=False):
        """XML
        Method which takes input file with IDMEF and converts it into output file with IDEA message(s)

        :param prettify: boolean, if true, JSON data in output file will be prettified (indentation), otherwise message
                         will be written to one line
        :raises IdmefToIdeaValueConverterException: when values cannot be converted properly
        :raises IdmefToIdeaMessageConverterException: when data cannot be converted properly from dict to elementtree
        :raises XmlParserException: when message could not be parsed, because message is not valid XML
        """
        messages_time = []
        all_time_before = time.process_time()
        message_number = 1
        try:
            for input_message in self.input_parser.parse_file_partially():
                message_time_before = time.process_time()
                output_message_unconv_values = self.convert_message(input_message, message_number)
                output_message = self.convert_values(output_message_unconv_values, message_number)
                self.exporter.export_message(output_message, prettify)
                messages_time.append(str(time.process_time() - message_time_before) + os.linesep)
                message_number += 1
        except ParseError:
            raise Exceptions.XmlParserException(
                "Message number " + str(message_number) + " is not valid XML and could not be parsed, parser has "
                "thrown this: " + repr(ParseError)
            )
        all_time_after = time.process_time() - all_time_before
        if self.time_output_file:
            self.print_process_times(self.time_output_file, all_time_after, messages_time)

    def convert_string(self):
        """
        Method which takes input string with single IDMEF message and converts it into output string with IDEA message

        :return: output string, where converted IDEA was exported
        :raises IdmefToIdeaValueConverterException: when values cannot be converted properly
        :raises IdmefToIdeaMessageConverterException: when data cannot be converted properly from dict to elementtree
        """
        message_number = 1
        try:
            input_message = self.input_parser.parse_string()
            output_message_unconv_values = self.convert_message(input_message, message_number)
            output_message = self.convert_values(output_message_unconv_values, message_number)
            return self.exporter.export_message_tostring(output_message)
        except ParseError:
            raise Exceptions.XmlParserException(
                "Message number " + str(message_number) + " is not valid XML and could not be parsed, parser has "
                "thrown this: " + repr(ParseError)
            )

    def convert_values(self, input_message, message_number):
        """
        Method which call convert_values method from value_converter and throw exception in case that it crashes

        :param input_message: dict input for value conversion
        :return: converted dict
        :raises IdmefToIdeaValueConverterException: when values cannot be converted properly
        """
        try:
            return self.value_converter.convert_values(input_message)
        except ValueError as value_error:
            raise Exceptions.IdmefToIdeaValueConverterException(
                "Message number " + str(message_number) + " is not valid so much, that it is not possible to convert "
                "value types from IDMEF to IDEA message and this error was thrown: " + repr(value_error)
            )
        except TypeError as type_error:
            raise Exceptions.IdmefToIdeaValueConverterException(
                "Message number " + str(message_number) + " is not valid so much, that it is not possible to convert "
                "value types from IDMEF to IDEA message and this error was thrown: " + repr(type_error)
            )

    def convert_message(self, input_message, message_number):
        """
        Method which call modify_data method from message_converter and throw exception in case that it crashes

        :param input_message: elementtree input for message conversion
        :return: converted dict
        :raises IdmefToIdeaMessageConverterException: when data cannot be converted properly from dict to elementtree
        """
        try:
            return self.message_converter.modify_data(input_message)
        except ValueError as value_error:
            raise Exceptions.IdmefToIdeaMessageConverterException(
                "Message number " + str(message_number) + " is not valid so much, that it is not possible to convert "
                "message from elementtree to dict and this exception was thrown: " + repr(value_error)
            )
        except TypeError as type_error:
            raise Exceptions.IdmefToIdeaMessageConverterException(
                "Message number " + str(message_number) + " is not valid so much, that it is not possible to convert "
                "message from elementtree to dict and this exception was thrown: " + repr(type_error)
            )

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