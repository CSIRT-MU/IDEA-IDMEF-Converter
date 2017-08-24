import logging

import IdeaAndIdmefConverter.InnerConverterStructure.Helper.Exceptions as OwnExceptions
from IdeaAndIdmefConverter.InnerConverterStructure.IdeaToIdmef.IdeaParser import IdeaParser
from IdeaAndIdmefConverter.InnerConverterStructure.IdeaToIdmef.IdeaToIdmefConverter import IdeaToIdmefConverter
from IdeaAndIdmefConverter.InnerConverterStructure.IdeaToIdmef.IdmefExporter import IdmefExporter
from IdeaAndIdmefConverter.InnerConverterStructure.IdeaToIdmef.ToIdmefMessageConverter import IdeaToIdmefMessageConverter
from IdeaAndIdmefConverter.InnerConverterStructure.IdeaToIdmef.ToIdmefValueConverter import IdeaToIdmefValueConverter
from IdeaAndIdmefConverter.InnerConverterStructure.IdmefToIdea.IdeaExporter import IdeaExporter
from IdeaAndIdmefConverter.InnerConverterStructure.IdmefToIdea.IdmefParser import IdmefParser
from IdeaAndIdmefConverter.InnerConverterStructure.IdmefToIdea.IdmefToIdeaConverter import IdmefToIdeaConverter
from IdeaAndIdmefConverter.InnerConverterStructure.IdmefToIdea.ToIdeaValueConverter import IdmefToIdeaValueConverter

from IdeaAndIdmefConverter.InnerConverterStructure.IdmefToIdea.ToIdeaMessageConverter import IdmefToIdeaMessageConverter


def convert_file_idea_into_idmef(input_filename, output_filename, time_output_filename=None, unconverted_filename=None,
                                 single_message=False, prettify=False, idmef_namespace=False):
    """
    Function which takes file with IDEA message (messages) and converts it into file with IDMEF message (messages).

    IMPORTANT: if you want to convert more than one message, each IDEA message must be in single line. Otherwise IDEA
               will not be parsed correctly.

    Each message will be converted to valid IDMEF with root IDMEF-Message, but root of all
    these messages in output file will be IDMEF-Messages (only if there are more input messages, if it is just single,
    absolute root will be IDMEF-Message). It means single valid IDMEF message is enclosed to tag
    (<IDMEF-Message></IDMEF-Message>)

    Be careful before you decide to convert, many fields from IDEA cannot be converted to IDMEF. If you do not provide
    unconverted_filename, where this unconverted data are stored converted naturally from JSON to XML, you may lose some
    data from IDEA.

    :param input_filename: Path to input file with IDEA message (messages).
    :param output_filename: Path to output file, which will contain converted IDMEF messages. Whole file will be
                            rewritten with IDMEF messages, so it is recommended to use path to file which does not exist
                            or is empty.
    :param time_output_filename: file for saving time of conversion
    :param unconverted_filename: Path to output file, which will contain XML data, which could not be converted properly
                                 from IDEA to IDMEF and therefore are converted naturally. Each messsage is
                                 encloded to tag UnconvertedFromIDEA, all messages (if more than one input IDEA is
                                 provided) are enclosed to root tag AllUnconvertedFromIDEA. Whole file will be
                                 rewritten, so it is recommended to use path to file which does not exist or is empty.
    :param single_message: boolean, information whether input file contains one or more messages
    :param prettify: boolean, information whether output XML has to be prettified (indentation) or not.
                    If you use your library at Windows os, this function always writes output prettified, you do not
                    need to use this parameter (use it from Linux systems)
    :param idmef_namespace: boolean, information, whether output IDMEF message (messages) has to contain "idmef"
                            namespace or not
    """
    input_file, output_file, time_file, unconverted_file = None, None, None, None
    converter = None
    try:
        input_file = open(input_filename, "r")
        output_file = open(output_filename, "w")
        if time_output_filename:
            time_file = open(time_output_filename, "w")
        if unconverted_filename:
            unconverted_file = open(unconverted_filename, "w")

        idea_parser = IdeaParser(input_file)
        idea_to_idmef = IdeaToIdmefMessageConverter()
        values_to_idmef = IdeaToIdmefValueConverter()
        idmef_exporter = IdmefExporter(output_file, unconverted_file)
        converter = IdeaToIdmefConverter(idea_parser, idea_to_idmef, values_to_idmef, idmef_exporter, time_file)
        converter.convert_file(single_message, prettify, idmef_namespace)
    except FileNotFoundError as error:
        logging.exception(repr(error))
    except PermissionError as error:
        logging.exception(repr(error))
    except OwnExceptions.JsonParserException as error:
        logging.exception(repr(error))
        if converter:
            converter.correct_file_after_interruption()
    except OwnExceptions.IdeaToIdmefMessageConverterException as error:
        logging.exception(repr(error))
        if converter:
            converter.correct_file_after_interruption()
    except OwnExceptions.IdeaToIdmefValueConverterException as error:
        logging.exception(repr(error))
        if converter:
            converter.correct_file_after_interruption()
    finally:
        if input_file:
            input_file.close()
        if output_file:
            output_file.close()
        if time_file:
            time_file.close()
        if unconverted_file:
            unconverted_file.close()


def convert_file_idmef_into_idea(input_filename, output_filename, time_output_filename=None, prettify=False):
    """
    Function which takes file with IDEA message (messages) and converts it into file with IDMEF message (messages).

    IMPORTANT: If you want to convert more than one message, each message must be enclosed in IDMEF-Message tag and
               because of valid XML it must have some root element, which will be ancestor of each IDMEF-Message (and
               must have different tag name than IDMEF-Message). Indentation of input is not important, in this case
               we do not require one message in one line if more input messages are provided.

    Fields, which could not be converted from IDMEF properly are in result provided in last "Attach" in each IDEA.

    :param input_filename: Path to input file with IDMEF message (messages).
    :param output_filename: Path to output file, which will contain converted IDEA messages. Whole file will be
                            rewritten with IDMEF messages, so it is recommended to use path to file which does not exist
                            or is empty.
    :param time_output_filename: file for saving time of conversion
    :param prettify: boolean, information whether output JSON has to be prettified (indentation) or not
    """
    input_file, output_file, time_file = None, None, None
    try:
        input_file = open(input_filename, "r")
        output_file = open(output_filename, "w")
        if time_output_filename:
            time_file = open(time_output_filename, "w")

        idmef_parser = IdmefParser(input_file)
        idmef_to_idea = IdmefToIdeaMessageConverter()
        idea_exporter = IdeaExporter(output_file)
        values_to_idea = IdmefToIdeaValueConverter()
        converter = IdmefToIdeaConverter(idmef_parser, idmef_to_idea, values_to_idea, idea_exporter, time_file)
        converter.convert_file(prettify=prettify)
    except FileNotFoundError as error:
        logging.exception(repr(error))
    except PermissionError as error:
        logging.exception(repr(error))
    except OwnExceptions.XmlParserException as error:
        logging.exception(repr(error))
    except OwnExceptions.IdmefToIdeaMessageConverterException as error:
        logging.exception(repr(error))
    except OwnExceptions.IdmefToIdeaValueConverterException as error:
        logging.exception(repr(error))
    finally:
        if input_file:
            input_file.close()
        if output_file:
            output_file.close()
        if time_file:
            time_file.close()


def convert_string_idea_into_idmef(input_string, idmef_namespace=False):
    """
    Function which takes string with single IDEA message and converts it into string with single IDMEF message.

    :param input_string: string containing JSON object with IDEA message
    :param idmef_namespace: boolean, information, whether output IDMEF message (messages) has to contain "idmef"
                            namespace or not
    :return: output string with converted IDMEF message
    """
    try:
        idea_parser = IdeaParser(input_string)
        idea_to_idmef = IdeaToIdmefMessageConverter()
        values_to_idmef = IdeaToIdmefValueConverter()
        idmef_exporter = IdmefExporter()
        converter = IdeaToIdmefConverter(idea_parser, idea_to_idmef, values_to_idmef, idmef_exporter)
        return converter.convert_string(idmef_namespace)
    except OwnExceptions.IdeaToIdmefMessageConverterException as error:
        logging.exception(repr(error))
    except OwnExceptions.IdeaToIdmefValueConverterException as error:
        logging.exception(repr(error))


def convert_string_idmef_into_idea(input_string):
    """
    Function which takes string with single IDMEF message and converts it into string with IDEA message (or messages
    when IDMEF message contains more alerts).

    :param input_string: string containing XML with IDEA message
    :return: output string with converted IDEA message (messages)
    """
    try:
        idmef_parser = IdmefParser(input_string)
        idmef_to_idea = IdmefToIdeaMessageConverter()
        idea_exporter = IdeaExporter()
        values_to_idea = IdmefToIdeaValueConverter()
        converter = IdmefToIdeaConverter(idmef_parser, idmef_to_idea, values_to_idea, idea_exporter)
        return converter.convert_string()
    except OwnExceptions.IdmefToIdeaMessageConverterException as error:
        logging.exception(repr(error))
    except OwnExceptions.IdmefToIdeaValueConverterException as error:
        logging.exception(repr(error))

"""
def main():
    convert_file_idea_into_idmef("../ExternalData/InputData/idea-examples.json",
                                 "../ExternalData/OutputData/idea-examples.xml", "idea-examples-time.txt",
                                 unconverted_filename="../ExternalData/OutputData/idea-examples-unconvertable.xml")
    convert_file_idmef_into_idea("../ExternalData/InputData/mid-level-phase-4.xml",
                                 "../ExternalData/OutputData/mid-level-phase-4.json", "mid-level-phase-time.txt")
    convert_file_idmef_into_idea("../ExternalData/InputData/rfc4765-examples.xml",
                                 "../ExternalData/OutputData/rfc4765-examples.json", "rfc4765-examples-time.txt")

if __name__ == "__main__":
    # execute only if run as a script
    main()
"""