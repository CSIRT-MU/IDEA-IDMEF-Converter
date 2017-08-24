from io import StringIO
from xml.etree.ElementTree import iterparse

from IdeaAndIdmefConverter.InnerConverterStructure.MessageParser import MessageParser


class IdmefParser(MessageParser):
    """
    Parser of Idmef. For parsing is used xml.etree.ElementTree module
    """

    def __init__(self, input_data):
        """
        Constructor which takes input file as argument

        :param input_data: file or string containing input IDMEF data in XML format
        """
        MessageParser.__init__(self, input_data)
        self.previous_root = None

    def parse_file_partially(self):
        """
        Parses file with IDMEF messages, creates elementtree of each alert node (but once return just actual alert)

        Can be used for large file, because once is parsed just one alert.

        :return: generator that generates "Alert" root with all children and attributes
        """

        xml_iterator = iterparse(self.input_data, events=("start", "end"))
        xml_iterator = iter(xml_iterator)
        event, root = xml_iterator.__next__()
        for event, element in xml_iterator:
            if '}' in element.tag:
                element.tag = element.tag.split('}', 1)[1]  # strip all namespaces
            if event == "end" and element.tag == "Alert":
                if self.previous_root:
                    self.previous_root.clear()
                self.previous_root = root
                yield element

    def parse_string(self):
        file_object = StringIO(self.input_data)
        self.input_data = file_object
        message_generator = self.parse_file_partially()
        try:
            return message_generator.__next__()
        except StopIteration:
            return None
