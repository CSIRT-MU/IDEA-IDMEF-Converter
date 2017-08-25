import json
import unittest

from IdeaAndIdmefConverter.InnerConverterStructure.IdmefToIdea.IdmefParser import IdmefParser

from IdeaAndIdmefConverter.InnerConverterStructure.IdmefToIdea.ToIdeaMessageConverter import IdmefToIdeaMessageConverter


def convert_single_ideamessage():
    with open("InputTestData/longidmef.xml") as input_idmef:
        idmef_parser = IdmefParser(input_idmef)
        message_converter = IdmefToIdeaMessageConverter()
        input_message = idmef_parser.parse_file_partially().__next__()
        return message_converter.modify_data(input_message)


def get_nth_device(device_name, order):
    return convert_single_ideamessage().get(device_name)[order]


def get_nth_atach_content(order):
    return json.loads(convert_single_ideamessage().get("Attach")[order].get("Content").replace("'", '"'))


class ToIdeaMessageTest(unittest.TestCase):
    def test_correct_format_field(self):
        self.assertEqual(convert_single_ideamessage().get("Format"), "IDEA0", "Format field in IDEA is not correct")

    def test_id_conversion(self):
        self.assertEqual(convert_single_ideamessage().get("ID"), "123d45",
                         "ID was not converted properly from IDMEF to IDEA message")

    def test_correlid_conversion(self):
        self.assertListEqual(convert_single_ideamessage().get("CorrelID"), ["28421", "87955"],
                             "CorrelID was not converted properly from IDMEF to IDEA message")

    def test_createtime_conversion(self):
        self.assertEqual(convert_single_ideamessage().get("CreateTime"), "0xbc723b45.0xef449129",
                         "CreateTime was not converted properly from IDMEF to IDEA message")

    def test_detecttime_conversion(self):
        self.assertEqual(convert_single_ideamessage().get("DetectTime"), "0xbc723b45.0xef449129",
                         "DetectTime was not converted properly from IDMEF to IDEA message")

    def test_category_conversion(self):
        self.assertListEqual(convert_single_ideamessage().get("Category"), ["Phishing"],
                             "Category (classification) was not converted properly from IDMEF to IDEA message")

    def test_ref_conversion(self):
        self.assertListEqual(convert_single_ideamessage().get("Ref"), ["ref.example.com"],
                             "Reference was not converted properly from IDMEF to IDEA message")

    def test_confidence_conversion(self):
        self.assertEqual(convert_single_ideamessage().get("Confidence"), str(0.54),
                         "Confidence was not converted properly from IDMEF to IDEA message")

    def test_hostname_conversion(self):
        self.assertListEqual(get_nth_device("Source", 0).get("Hostname"), ["Second name of the equipment"],
                             "Hostname of first source was not converted properly from IDMEF to IDEA message")
        self.assertListEqual(get_nth_device("Source", 1).get("Hostname"), ["Third name of the equipment"],
                             "Hostname of second source was not converted properly from IDMEF to IDEA message")
        self.assertListEqual(get_nth_device("Target", 0).get("Hostname"), ["Fourth name of the equipment"],
                             "Hostname of first target was not converted properly from IDMEF to IDEA message")
        self.assertListEqual(get_nth_device("Target", 1).get("Hostname"), ["Fifth name of the equipment"],
                             "Hostname of second target was not converted properly from IDMEF to IDEA message")

    def test_ip4_conversion(self):
        self.assertListEqual(get_nth_device("Source", 0).get("IP4"), ["100.184.216.130"],
                             "IP4 of first source was not converted properly from IDMEF to IDEA message")
        self.assertListEqual(get_nth_device("Source", 1).get("IP4"), ["78.184.216.119"],
                             "IP4 of second source was not converted properly from IDMEF to IDEA message")
        self.assertListEqual(get_nth_device("Target", 0).get("IP4"), ["98.184.216.119", "100.89.114.119"],
                             "IP4 of first target was not converted properly from IDMEF to IDEA message")
        self.assertListEqual(get_nth_device("Target", 1).get("IP4"), ["100.184.216.119"],
                             "IP4 of second target was not converted properly from IDMEF to IDEA message")

    def test_ip6_conversion(self):
        self.assertListEqual(get_nth_device("Source", 0).get("IP6"), ["2001:db8:a::123/64"],
                             "IP6 of first source was not converted properly from IDMEF to IDEA message")
        self.assertIsNone(get_nth_device("Source", 1).get("IP6", None),
                          "IP6 of second source exists, despite it should not")
        self.assertIsNone(get_nth_device("Target", 0).get("IP6", None),
                          "IP6 of first target exists, despite it should not")
        self.assertIsNone(get_nth_device("Target", 1).get("IP6", None),
                          "IP6 of second target exists, despite it should not")

    def test_mail_conversion(self):
        self.assertIsNone(get_nth_device("Source", 0).get("Email", None),
                          "Mail of first source exists, despite it should not")
        self.assertListEqual(get_nth_device("Source", 1).get("Email"), ["example@example.com"],
                             "Mail of first source was not converted properly from IDMEF to IDEA message")
        self.assertIsNone(get_nth_device("Target", 0).get("Email", None),
                          "Mail of first target exists, despite it should not")
        self.assertIsNone(get_nth_device("Target", 1).get("Email", None),
                          "Mail of second target exists, despite it should not")

    def test_mac_conversion(self):
        self.assertIsNone(get_nth_device("Source", 0).get("MAC", None),
                          "Mac of first source exists, despite it should not")
        self.assertIsNone(get_nth_device("Source", 1).get("MAC", None),
                          "Mac of second source exists, despite it should not")
        self.assertIsNone(get_nth_device("Target", 0).get("MAC", None),
                          "Mac of first target exists, despite it should not")
        self.assertListEqual(get_nth_device("Target", 1).get("MAC"), ["00:00:45:67:89:ab"],
                             "Mac of second target was not converted properly from IDMEF to IDEA message")

    def test_proto_conversion(self):
        self.assertListEqual(get_nth_device("Source", 0).get("Proto"), ["Additional info of protocol"],
                             "Protocol of first source was not converted properly from IDMEF to IDEA message")
        self.assertListEqual(get_nth_device("Source", 1).get("Proto"), ["Additional info of protocol"],
                             "Protocol of second source was not converted properly from IDMEF to IDEA message")
        self.assertListEqual(get_nth_device("Target", 0).get("Proto"), ["Additional info of protocol"],
                             "Protocol of first target was not converted properly from IDMEF to IDEA message")
        self.assertListEqual(get_nth_device("Target", 1).get("Proto"), ["Additional info of protocol"],
                             "Protocol of second target was not converted properly from IDMEF to IDEA message")

    def test_port_conversion(self):
        self.assertListEqual(get_nth_device("Source", 0).get("Port"), [154],
                             "Port of first source was not converted properly from IDMEF to IDEA message")
        self.assertListEqual(get_nth_device("Source", 1).get("Port"), [158],
                             "Port of second source was not converted properly from IDMEF to IDEA message")
        self.assertListEqual(get_nth_device("Target", 0).get("Port"), [80],
                             "Port of first target was not converted properly from IDMEF to IDEA message")
        self.assertListEqual(get_nth_device("Target", 1).get("Port"), [90, 91, 92, 93, 94],
                             "Port of second target was not converted properly from IDMEF to IDEA message")

    def test_spoofed_conversion(self):
        self.assertEqual(get_nth_device("Source", 0).get("Spoofed"), "yes",
                         "Spoofed attribute of first source was not converted properly from IDMEF to IDEA message")
        self.assertEqual(get_nth_device("Source", 1).get("Spoofed"), "unknown",
                         "Spoofed attribute of second source was not converted properly from IDMEF to IDEA message")
        self.assertEqual(get_nth_device("Target", 0).get("Spoofed"), "no",
                         "Spoofed of first target was not converted properly from IDMEF to IDEA message")
        self.assertEqual(get_nth_device("Target", 1).get("Spoofed"), "yes",
                         "Spoofed of second target was not converted properly from IDMEF to IDEA message")

    def test_router_conversion(self):
        self.assertListEqual(get_nth_device("Source", 0).get("Router"), ["interfaceExample"],
                             "Router of first source was not converted properly from IDMEF to IDEA message")
        self.assertListEqual(get_nth_device("Source", 1).get("Router"), ["interfaceExample2"],
                             "Router of second source was not converted properly from IDMEF to IDEA message")
        self.assertListEqual(get_nth_device("Target", 0).get("Router"), ["interfaceExample3"],
                             "Router of first target was not converted properly from IDMEF to IDEA message")
        self.assertListEqual(get_nth_device("Target", 1).get("Router"), ["interfaceExample4"],
                             "Router of second target was not converted properly from IDMEF to IDEA message")

    def test_node_conversion(self):
        self.assertEqual(len(convert_single_ideamessage().get("Node")), 1, "Number of Nodes is not correct")
        self.assertEqual(convert_single_ideamessage().get("Node")[0].get("Name"), "DetectorExample",
                         "Node name was not converted properly")
        self.assertEqual(convert_single_ideamessage().get("Node")[0].get("SW"),
                         "detector great 2.0 highest Linux 4.4.0-31-generic",
                         "Node SW was not converted properly")

    def test_attachment_conversion(self):
        expected_first_attach = {
            "#text": "First additional data test example",
            "@meaning": "Test additional data"
        }
        expected_second_attach = {
            "#text": "Second additional data test example",
            "@meaning": "Test additional data too"
        }
        self.assertDictEqual(get_nth_atach_content(0),
                             expected_first_attach, "First attachment was not converted properly")
        self.assertEqual(get_nth_atach_content(1),
                         expected_second_attach, "Second attachment was not converted properly")


if __name__ == '__main__':
    unittest.main()
