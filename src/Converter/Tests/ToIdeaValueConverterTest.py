import unittest

from IdeaAndIdmefConverter.InnerConverterStructure.IdmefToIdea.ToIdeaValueConverter import IdmefToIdeaValueConverter


class ToIdeaValuesTest(unittest.TestCase):
    def test_detecttime(self):
        input_dictionary = {
            "DetectTime": "0xbc722ebe.0x00000000"
        }
        expected_dictionary = {
            "DetectTime": "2000-03-09 14:07:58"
        }
        values_to_idea_converter = IdmefToIdeaValueConverter()
        self.assertEqual(values_to_idea_converter.convert_values(input_dictionary), expected_dictionary,
                         "In DetectTime, timestamp is not converted to hex ntp correctly")

    def test_createtime(self):
        input_dictionary = {
            "CreateTime": "0xbc71f4f5.0x000e42f0"
        }
        expected_dictionary = {
            "CreateTime": "2000-03-09 10:01:25.934640"
        }
        values_to_idea_converter = IdmefToIdeaValueConverter()
        self.assertEqual(values_to_idea_converter.convert_values(input_dictionary), expected_dictionary,
                         "In DetectTime, timestamp is not converted to hex ntp correctly")

    def test_spoofed_source_true(self):
        input_dictionary = {
            "Source":
                [
                    {"Spoofed": "yes"}
                ]
        }
        expected_dictionary = {
            "Source":
                [
                    {"Spoofed": True}
                ]
        }
        values_to_idmef_converter = IdmefToIdeaValueConverter()
        self.assertEqual(values_to_idmef_converter.convert_values(input_dictionary), expected_dictionary,
                         "Spoofed in Source is not converted correctly")

    def test_spoofed_source_false(self):
        input_dictionary = {
            "Source":
                [
                    {"Spoofed": "no"}
                ]
        }
        expected_dictionary = {
            "Source":
                [
                    {"Spoofed": False}
                ]
        }
        values_to_idmef_converter = IdmefToIdeaValueConverter()
        self.assertEqual(values_to_idmef_converter.convert_values(input_dictionary), expected_dictionary,
                         "Spoofed in Source is not converted correctly")

    def test_spoofed_source_unknown(self):
        input_dictionary = {
            "Source":
                [
                    {"Spoofed": "unknown"}
                ]
        }
        expected_dictionary = {
            "Source":
                [
                    {}
                ]
        }
        values_to_idmef_converter = IdmefToIdeaValueConverter()
        self.assertEqual(values_to_idmef_converter.convert_values(input_dictionary), expected_dictionary,
                         "Spoofed in Source is not converted correctly")

    def test_spoofed_target_true(self):
        input_dictionary = {
            "Target":
                [
                    {"Spoofed": "yes"}
                ]
        }
        expected_dictionary = {
            "Target":
                [
                    {"Spoofed": True}
                ]
        }
        values_to_idmef_converter = IdmefToIdeaValueConverter()
        self.assertEqual(values_to_idmef_converter.convert_values(input_dictionary), expected_dictionary,
                         "Spoofed in Target is not converted correctly")

    def test_spoofed_target_false(self):
        input_dictionary = {
            "Target":
                [
                    {"Spoofed": "no"}
                ]
        }
        expected_dictionary = {
            "Target":
                [
                    {"Spoofed": False}
                ]
        }
        values_to_idmef_converter = IdmefToIdeaValueConverter()
        self.assertEqual(values_to_idmef_converter.convert_values(input_dictionary), expected_dictionary,
                         "Spoofed in Target is not converted correctly")

    def test_spoofed_target_unknown(self):
        input_dictionary = {
            "Target":
                [
                    {
                        "Spoofed": "unknown",
                        "Somevalue": "something"
                    },
                ]
        }
        expected_dictionary = {
            "Target":
                [
                    {
                        "Somevalue": "something"
                    }
                ]
        }
        values_to_idmef_converter = IdmefToIdeaValueConverter()
        self.assertEqual(values_to_idmef_converter.convert_values(input_dictionary), expected_dictionary,
                         "Spoofed in Target is not converted correctly")

    def test_conversion_from_ip4hex(self):
        input_dictionary = {
            "Source":
                [
                    {
                        "IP4-hex": ["0xde796f70"]
                    }
                ],
            "Target":
                [
                    {
                        "IP4": ["10.10.20.20", "10.10.20.30"],
                        "IP4-hex": ["123ef5"]
                    }
                ]
        }
        expected_dictionary = {
            "Source":
                [
                    {
                        "IP4": ["222.121.111.112"]
                    }
                ],
            "Target":
                [
                    {
                        "IP4": ["10.10.20.20", "10.10.20.30", "0.18.62.245"]
                    }
                ]
        }
        values_to_idmef_converter = IdmefToIdeaValueConverter()
        self.assertEqual(values_to_idmef_converter.convert_values(input_dictionary), expected_dictionary,
                         "Spoofed in Source is not converted correctly")

    def test_conversion_from_ip6hex(self):
        input_dictionary = {
            "Source":
                [
                    {
                        "IP6-hex": ["0x20010db80a0b12f00000000000000001"]
                    }
                ],
            "Target":
                [
                    {
                        "IP6": ["10::10:ab:a:a:a/64", "10::10:ab:a:a:b/64"],
                        "IP6-hex": ["0x1048965422001000ab000a000a000b"]
                    }
                ]
        }
        expected_dictionary = {
            "Source":
                [
                    {
                        "IP6": ["2001:db8:a0b:12f0::1"]
                    }
                ],
            "Target":
                [
                    {
                        "IP6": ["10::10:ab:a:a:a/64", "10::10:ab:a:a:b/64", "10:4896:5422:10:ab:a:a:b"]
                    }
                ]
        }
        values_to_idmef_converter = IdmefToIdeaValueConverter()
        self.assertEqual(values_to_idmef_converter.convert_values(input_dictionary), expected_dictionary,
                         "Spoofed in Source is not converted correctly")


if __name__ == '__main__':
    unittest.main()
