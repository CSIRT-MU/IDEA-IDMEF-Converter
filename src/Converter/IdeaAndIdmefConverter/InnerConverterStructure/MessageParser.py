from abc import ABC, abstractmethod


class MessageParser(ABC):
    """
    Class which provides parsing services
    """
    def __init__(self, input_data):
        """
        Init section taking file with data for parsing

        :param input_data: string or file with input data
        """
        self.input_data = input_data

    @abstractmethod
    def parse_file_partially(self):
        """
        Parsing file just for pieces (lines, or nodes) and yields actual parsed piece

        :return: generated actual parsed piece of file
        """
        pass
