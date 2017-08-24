import unittest

from IdeaAndIdmefConverter.InnerConverterStructure.IdeaToIdmef.IdeaParser import IdeaParser
from Tests.InputTestData.IdeaDictionaries import get_dict1, get_expected_dict2, get_test_string


class SingleIdeaMessageParserTest(unittest.TestCase):

    def test_idea_parsed_together(self):
        with open("InputTestData/longidea.json", "r") as input_message:
            idea_parser = IdeaParser(input_message)
            result_dict = idea_parser.parse_file_together()
            self.assertDictEqual(result_dict, get_dict1())

    def test_idea_parsed_fromstring(self):
        idea_parser = IdeaParser(get_test_string())
        result_dict = idea_parser.parse_string()
        self.assertDictEqual(result_dict, get_dict1())


class MultipleIdeaMessageParserTest(unittest.TestCase):

    def test_idea_parsed_partially(self):
        with open("InputTestData/multiplelongidea.json", "r") as input_message:
            idea_parser = IdeaParser(input_message)
            result_generator = idea_parser.parse_file_partially()
            self.assertDictEqual(result_generator.__next__(), get_dict1())
            self.assertDictEqual(result_generator.__next__(), get_expected_dict2())


if __name__ == '__main__':
    unittest.main()
