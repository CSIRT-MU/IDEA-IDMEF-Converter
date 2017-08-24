import json
import os

from IdeaAndIdmefConverter.InnerConverterStructure.Exporter import Exporter


class IdeaExporter(Exporter):
    """
    Class, which provides export of dictionary containing IDEA data to a file
    """

    def __init__(self, output_file=None):
        """
        Init section of Exporter class taking file

        :param output_file: file, where converted data will be written
        """

        Exporter.__init__(self, output_file)
        self.output_file = output_file

    def export_message(self, output_message, prettify=False):
        """
        Exports IDEA dictionary with converted data to file.

        :param output_message: list of dictionaries (eventually dictionary) containing IDEA keys and output values
        :param prettify: boolean, if true, JSON data in output file will be prettified (indentation), otherwise message
                         will be written to one line
        """

        indentation = None
        if prettify:
            indentation = 4
        if isinstance(output_message, list):
            for message in output_message:
                self.output_file.write(json.dumps(message, indent=indentation) + os.linesep)
        else:
            self.output_file.write(json.dumps(output_message, indent=indentation) + os.linesep)

    def export_message_tostring(self, output_message):
        """
        Exports dict with IDEA to string

        :param output_message: list of dictionaries (eventually dictionary) containing IDEA
        :return: converted string with newline at the end
        """
        output_string = ""
        if isinstance(output_message, list):
            for message in output_message:
                output_string += json.dumps(message) + os.linesep
            return output_string
        return json.dumps(output_message) + os.linesep
