import json

from IdeaAndIdmefConverter.InnerConverterStructure.MessageParser import MessageParser


class IdeaParser(MessageParser):
    """
    Parser of IDEA. For parsing is used json module
    """

    def __init__(self, input_data):
        """
        Constructor which takes input file as argument

        :param input_data: file or string containing input IDEA0 data in JSON format
        """
        MessageParser.__init__(self, input_data)

    def parse_file_partially(self):
        """
        Parses file with multiple IDEA messages and creates dictionary from message (always just from one message).

        Each message must be on separate line, otherwise it will not be parsed correctly
        and probably JSON syntax error will be thrown.

        Can be used for large file, because once is parsed just one line.

        :return: generator, which every time generates dictionary with parsed message of next line
        """

        for line in self.input_data:
            if not line.isspace():
                yield json.loads(line)

    def parse_file_together(self):
        """
        Parses file with IDEA message.

        Parser of JSON expects only single JSON object in file, otherwise syntax error will be thrown.

        :return: dictionary with parsed IDEA message
        """
        return json.load(self.input_data)

    def parse_string(self):
        return json.loads(self.input_data)