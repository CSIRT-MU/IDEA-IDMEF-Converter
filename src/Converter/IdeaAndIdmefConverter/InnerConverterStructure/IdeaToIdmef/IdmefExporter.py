import os
import xml.etree.ElementTree as ElTree
from xml.dom import minidom

from IdeaAndIdmefConverter.InnerConverterStructure.Helper.ElementTreeHelper import idmefmessage_tag_tostring

from IdeaAndIdmefConverter.InnerConverterStructure.Exporter import Exporter


class IdmefExporter(Exporter):
    """
    Class, which provides export of elementtree containing IDMEF data to a file or string
    """

    def __init__(self, output_file=None, output_file_rest_values=None):
        """
        Init section of Exporter class taking file

        :param output_file: file, where converted data will be written
        :param output_file_rest_values: file, where converted data of field, which could not be converted are written
        """

        Exporter.__init__(self, output_file)
        self.output_file = output_file
        self.output_file_rest_values = output_file_rest_values

    def export_message(self, output_message, prettify=False):
        """
        Exports IDMEF elementtree with converted data to file and separately, if output_file_rest_values exists,
        exports elementtree with fields which could not be converted from IDEA to IDMEF properly

        :param output_message: elementtree root (element) containing IDMEF tags, attributes and children with output
                               values
        :param prettify: boolean, if true, XML data in output file will be prettified (indentation), otherwise message
                         will be written to one line
        """

        doc = minidom.Document()
        declaration = doc.toxml()

        output_message_string = ElTree.tostring(output_message[0], encoding="unicode")
        if prettify:
            output_message_string = self.make_pretty_xml(output_message_string)[(len(declaration) + 1):]
        else:
            output_message_string += os.linesep
        self.output_file.write(output_message_string)
        if self.output_file_rest_values:
            output_string_rest_values = ElTree.tostring(output_message[1], encoding="unicode")
            if prettify:
                output_string_rest_values = self.make_pretty_xml(output_string_rest_values)[(len(declaration) + 1):]
            else:
                output_string_rest_values += os.linesep
            self.output_file_rest_values.write(output_string_rest_values)

    def write_starttag_tofile(self, tag_name):
        """
        Writes declaration and start tag to file. This method is good for converting more than one message.

        :param tag_name: string, tag of root tag (usually it will be "IDMEF-Messages")
        """
        starttag, endtag = idmefmessage_tag_tostring(tag_name)
        self.output_file.write(starttag)

    def write_endtag_tofile(self, tag_name):
        """
        Writes end tag to file. This method is also good for converting more than one message

        :param tag_name: string, tag of root tag (usually it will be "IDMEF-Messages")
        """
        starttag, endtag = idmefmessage_tag_tostring(tag_name)
        self.output_file.write(endtag)

    def write_starttag_tounconverted(self, tag_name):
        starttag, endtag = idmefmessage_tag_tostring(tag_name)
        if self.output_file_rest_values:
            self.output_file_rest_values.write(starttag)

    def write_endtag_tounconverted(self, tag_name):
        starttag, endtag = idmefmessage_tag_tostring(tag_name)
        if self.output_file_rest_values:
            self.output_file_rest_values.write(endtag)

    def export_message_tostring(self, output_message):
        """
        Takes elementtree

        :param output_message: elementtree root (element) containing IDMEF tags, attributes and children with output
                               values
        :return: pair of string, where output_message was exported and string of unconvertable values
        """
        return ElTree.tostring(output_message[0], encoding="unicode"), \
               ElTree.tostring(output_message[1], encoding="unicode") if self.output_file_rest_values else ""

    def make_pretty_xml(self, xml_string):
        """
        Takes xml, which is in one line and return "prettyfied" xml,
        where are tags and values separated by tab and newline characters

        :param xml_string: input string, which should be in line
        :return: prettified xml string
        """
        return minidom.parseString(xml_string).toprettyxml(newl=os.linesep)

    def rest_values_file_exists(self):
        return self.output_file_rest_values is not None
