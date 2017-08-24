import json
import unittest

from IdeaAndIdmefConverter.InnerConverterStructure.IdmefToIdea.IdeaExporter import IdeaExporter
from Tests.InputTestData.IdeaDictionaries import get_dict1


class IdeaExporterTest(unittest.TestCase):
    def test_file_export(self):
        with open("OutputTestData/idea_test.json", "w") as output_file:
            idea_exporter = IdeaExporter(output_file)
            idea_exporter.export_message([get_dict1()])

        with open("OutputTestData/idea_test.json", "r") as output_file:
            self.assertEqual(json.load(output_file), get_dict1(), "IDEA export to file is not correct")

    def test_string_export(self):
        idea_exporter = IdeaExporter()
        export_string = idea_exporter.export_message_tostring([get_dict1()])
        self.assertEqual(json.loads(export_string), get_dict1(), "IDEA export to string is not correct")

if __name__ == '__main__':
    unittest.main()
