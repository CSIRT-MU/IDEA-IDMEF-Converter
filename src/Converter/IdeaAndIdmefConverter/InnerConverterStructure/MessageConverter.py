from abc import ABC, abstractmethod


class MessageConverter(ABC):
    """
    Abstract class, which declares methods for converting just single message for specific format.
    All important operations of data conversion should be done in this class.
    """

    @abstractmethod
    def modify_data(self, input_message):
        """
        Takes data from input_message structure and converts it into data structure of output format

        :param input_message: Parsed message of specific format, for example in JSON it will be probably dictionary,
                                in XML ElementTree root, but it depends on parsers.
                                If input_message is None, method takes input_message from class attribute
        :return: data in output data structure for exporting
        """
        pass
