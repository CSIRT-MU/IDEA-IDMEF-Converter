from abc import ABC, abstractmethod


class InputConverter(ABC):
    """
    Class, which takes cares about export specific message in a specific data structure to a file
    """

    def __init__(self, input_parser, message_converter, value_converter, exporter):
        """
        Constructor

        :param input_parser: instance of InputParser class
        :param message_converter: instance of MessageConverter class
        :param value_converter: instance of ValueConverter class
        :param exporter: instance of Exporter class
        """
        self.message_converter = message_converter
        self.value_converter = value_converter
        self.exporter = exporter
        self.input_parser = input_parser

    @abstractmethod
    def convert_file(self):
        """
        Method, which converts whole file with input messages to file with output messages
        """
        pass

    @abstractmethod
    def convert_string(self):
        """
        Method, which converts string with input message to string with output message
        :return:
        """
        pass
