from abc import ABC, abstractmethod


class Exporter(ABC):
    """
    Class, which takes cares about export specific message in a specific data structure to a file
    """

    def __init__(self, output_file):
        """
        Init section of Exporter class taking file

        :param output_file: file, where converted data will be written
        """
        self.output_file = output_file

    @abstractmethod
    def export_message(self, output_message):
        """
        Method, which exports specific data structure with converted values to file

        :param output_message: data structure with output data
        """
        pass

