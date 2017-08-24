import unittest

from IdeaAndIdmefConverter.InnerConverterStructure.IdeaToIdmef.ToIdmefValueConverter import IdeaToIdmefValueConverter


class ToIdmefValuesTest(unittest.TestCase):
    def test_detecttime(self):
        input_dictionary = {
            "DetectTime": "2000-03-09T14:07:58Z"
        }
        expected_dictionary = {
            "DetectTime": ("2000-03-09T14:07:58Z", "0xbc722ebe.0x00000000")
        }
        values_to_idmef_converter = IdeaToIdmefValueConverter()
        self.assertDictEqual(values_to_idmef_converter.convert_values(input_dictionary), expected_dictionary,
                             "In DetectTime, timestamp is not converted to hex ntp correctly")

    def test_createtime(self):
        input_dictionary = {
            "CreateTime": "2000-03-09T10:01:25.93464Z"
        }
        expected_dictionary = {
            "CreateTime": ("2000-03-09T10:01:25.93464Z", "0xbc71f4f5.0x000e42f0")
        }
        values_to_idmef_converter = IdeaToIdmefValueConverter()
        self.assertDictEqual(values_to_idmef_converter.convert_values(input_dictionary), expected_dictionary,
                             "In CreateTime, timestamp is not converted to hex ntp correctly")

    def test_spoofed_source_true(self):
        input_dictionary = {
            "Source":
                [
                    {"Spoofed": True}
                ]
        }
        expected_dictionary = {
            "Source":
                [
                    {"Spoofed": "yes"}
                ]
        }
        values_to_idmef_converter = IdeaToIdmefValueConverter()
        self.assertDictEqual(values_to_idmef_converter.convert_values(input_dictionary), expected_dictionary,
                             "Spoofed in Source is not converted correctly")

    def test_spoofed_source_false(self):
        input_dictionary = {
            "Source":
                [
                    {"Spoofed": False}
                ]
        }
        expected_dictionary = {
            "Source":
                [
                    {"Spoofed": "no"}
                ]
        }
        values_to_idmef_converter = IdeaToIdmefValueConverter()
        self.assertDictEqual(values_to_idmef_converter.convert_values(input_dictionary), expected_dictionary,
                             "Spoofed in Source is not converted correctly")

    def test_spoofed_source_unknown(self):
        input_dictionary = {
            "Source":
                [
                    {}
                ]
        }
        expected_dictionary = {
            "Source":
                [
                    {"Spoofed": "unknown"}
                ]
        }
        values_to_idmef_converter = IdeaToIdmefValueConverter()
        self.assertDictEqual(values_to_idmef_converter.convert_values(input_dictionary), expected_dictionary,
                             "Spoofed in Source is not converted correctly")

    def test_spoofed_target_true(self):
        input_dictionary = {
            "Target":
                [
                    {"Spoofed": True}
                ]
        }
        expected_dictionary = {
            "Target":
                [
                    {"Spoofed": "yes"}
                ]
        }
        values_to_idmef_converter = IdeaToIdmefValueConverter()
        self.assertDictEqual(values_to_idmef_converter.convert_values(input_dictionary), expected_dictionary,
                             "Spoofed in Target is not converted correctly")

    def test_spoofed_target_false(self):
        input_dictionary = {
            "Target":
                [
                    {"Spoofed": False}
                ]
        }
        expected_dictionary = {
            "Target":
                [
                    {"Spoofed": "no"}
                ]
        }
        values_to_idmef_converter = IdeaToIdmefValueConverter()
        self.assertDictEqual(values_to_idmef_converter.convert_values(input_dictionary), expected_dictionary,
                             "Spoofed in Target is not converted correctly")

    def test_spoofed_target_unknown(self):
        input_dictionary = {
            "Target":
                [
                    {
                        "Somevalue": "something"
                    },
                ]
        }
        expected_dictionary = {
            "Target":
                [
                    {
                        "Spoofed": "unknown",
                        "Somevalue": "something"
                    }
                ]
        }
        values_to_idmef_converter = IdeaToIdmefValueConverter()
        self.assertDictEqual(values_to_idmef_converter.convert_values(input_dictionary), expected_dictionary,
                             "Spoofed in Target is not converted correctly")

    def test_converting_all_types(self):
        input_dictionary = {
            "DetectTime": "2010-05-19T14:02:25.93464",
            "CreateTime": "2000-03-09 10:01:25.93464",
            "RandomField": 5,
            "Source":
                [
                    {
                        "AnotherRandomField": True,
                    },
                    {
                        "Spoofed": True
                    }
                ],
            "Target":
                [
                    {
                        "Somevalue": "something",
                        "Spoofed": True
                    },
                    {
                        "Spoofed": False
                    }
                ]
        }
        expected_dictionary = {
            "DetectTime": ("2010-05-19T14:02:25.93464", "0xcf9e5fe1.0x000e42f0"),
            "CreateTime": ("2000-03-09 10:01:25.93464", "0xbc71f4f5.0x000e42f0"),
            "RandomField": 5,
            "Source":
                [
                    {
                        "AnotherRandomField": True,
                        "Spoofed": "unknown"
                    },
                    {
                        "Spoofed": "yes"
                    }
                ],
            "Target":
                [
                    {
                        "Somevalue": "something",
                        "Spoofed": "yes"
                    },
                    {
                        "Spoofed": "no"
                    }
                ]
        }
        values_to_idmef_converter = IdeaToIdmefValueConverter()
        self.assertDictEqual(values_to_idmef_converter.convert_values(input_dictionary), expected_dictionary,
                             "Spoofed in Target is not converted correctly")


if __name__ == '__main__':
    unittest.main()
