from abc import ABC, abstractmethod


class ValuesConverter(ABC):
    """
    Abstract class which declares function which should convert data types of values from data types of input format to
    data types of output format
    """

    @abstractmethod
    def convert_values(self, input_values):
        """
        Takes parsed data and converts data types of values, that has to be converted

        :param input_values: input data with unconverted data types
        :return: data in the same data structure with converted values
        """
        pass
