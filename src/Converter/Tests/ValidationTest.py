import json
import unittest

import jsonschema
from lxml import etree

from IdeaAndIdmefConverter.ConverterFunctions import convert_file_idea_into_idmef, convert_file_idmef_into_idea, \
    convert_string_idea_into_idmef, convert_string_idmef_into_idea


class MyTestCase(unittest.TestCase):
    def test_idmef_validity(self):
        convert_file_idea_into_idmef("InputTestData/longidea.json",
                                     "OutputTestData/longidea-converted.xml",
                                     unconverted_filename=None, single_message=True, prettify=True,
                                     idmef_namespace=False)
        dtd = etree.DTD("Schemas/idmef_schema.dtd")
        tree = etree.iterparse("OutputTestData/outputidmef1.xml")
        tree = iter(tree)
        event, root = tree.__next__()
        for event, element in tree:
            if '}' in element.tag:
                element.tag = element.tag.split('}', 1)[1]  # strip all namespaces
            if event == "end" and element.tag == "IDMEF-Message":
                self.assertTrue(dtd.validate(element), dtd.error_log.filter_from_errors())
                root.clear()

    def test_idea_validity(self):
        convert_file_idmef_into_idea("InputTestData/longidmef.xml", "OutputTestData/longidmef-converted.json",
                                     prettify=False)
        with open("OutputTestData/outputidea1.json", "r") as idea, open("Schemas/schema.json") as schema:
            i = 0
            loaded_schema = json.load(schema)
            try:
                jsonschema.validate(json.loads(idea.readline()), loaded_schema)
                i += 1
            except jsonschema.ValidationError as ex:
                self.fail("Test of validation of file outputidea1.json threw ValidationError on idea message: " +
                          str(i) + ". Message of exception: " + ex.message)

if __name__ == '__main__':
    unittest.main()
