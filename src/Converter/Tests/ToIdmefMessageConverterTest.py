import unittest

from IdeaAndIdmefConverter.InnerConverterStructure.IdeaToIdmef.ToIdmefMessageConverter import IdeaToIdmefMessageConverter
from Tests.InputTestData.IdeaDictionaries import get_dict1


def get_idmefalert_from_ideamessage():
    input_message = get_dict1()
    converter = IdeaToIdmefMessageConverter()
    return converter.modify_data(input_message)[0].find("Alert")


def get_nth_device_from_idmef(device_name, order):
    return get_idmefalert_from_ideamessage().findall(device_name)[order]


def get_addresses_from_idmef(device_name, order, address_category):
    addresses_valuelist = []
    addresses = get_nth_device_from_idmef(device_name, order)\
        .findall('Node/Address[@category="' + address_category + '"]/address')
    for address in addresses:
        addresses_valuelist.append(address.text)
    return addresses_valuelist


def get_analyzer_from_idmef():
    return get_idmefalert_from_ideamessage().find("Analyzer")


class ToIdmefMessageTest(unittest.TestCase):
    def test_id_conversion(self):
        self.assertEqual(get_idmefalert_from_ideamessage().get("messageid"),
                         "2E4A3926-B1B9-41E3-89AE-B6B474EB0A54",
                         "ID was not converted properly from IDEA to IDMEF message")

    def test_createtime_conversion(self):
        self.assertEqual(get_idmefalert_from_ideamessage().find("CreateTime").text, "2017-03-23T10:10:42Z",
                         "CreateTime was not converted properly from IDEA to IDMEF message")

    def test_detecttime_conversion(self):
        self.assertEqual(get_idmefalert_from_ideamessage().find("DetectTime").text, "2017-03-23T09:15:50Z",
                         "DetectTime was not converted properly from IDEA to IDMEF message")

    def test_correlId_conversion(self):
        alertident_valuelist = []
        correlation_alert = get_idmefalert_from_ideamessage().find("CorrelationAlert")
        for alertident in correlation_alert.findall("alertident"):
            alertident_valuelist.append(alertident.text)
        self.assertListEqual(alertident_valuelist,
                             ["3E4A3926-B1B9-41E3-89AE-B6B474EB0A56", "4E4A3926-B1B9-41E3-89AE-B6B474EB0A57",
                              "5E4A3926-B1B9-41E3-89AE-B6B474EB0A58"],
                             "CorrelID was not converted properly from IDEA to IDMEF message")

    def test_category_conversion(self):
        self.assertEqual(get_idmefalert_from_ideamessage().find("Classification").get("text"), "Abusive.Spam",
                         "Category (classification) was not converted properly from IDEA to IDMEF message")

    def test_confidence_conversion(self):
        self.assertEqual(get_idmefalert_from_ideamessage().find("Assessment/Confidence").text, str(0.563),
                         "Confidence was not converted properly from IDEA to IDMEF message")

    def test_reference_conversion(self):
        reference_valuelist = []
        references = get_idmefalert_from_ideamessage().findall("Classification/Reference/url")
        for reference in references:
            reference_valuelist.append(reference.text)
        self.assertListEqual(reference_valuelist, ["http://www.example.com", "http://www.other.example.com"],
                             "Reference was not converted properly from IDEA to IDMEF message")

    def test_hostname_conversion(self):
        self.assertEqual(get_nth_device_from_idmef("Source", 0).find("Node/name").text, "hostexample.com",
                         "Hostname of first source was not converted properly from IDEA to IDMEF message")
        self.assertEqual(get_nth_device_from_idmef("Source", 1).find("Node/name").text, "hostexample2.com",
                         "Hostname of second source was not converted properly from IDEA to IDMEF message")
        self.assertEqual(get_nth_device_from_idmef("Target", 0).find("Node/name").text, "targethostexample.com",
                         "Hostname of first target was not converted properly from IDEA to IDMEF message")
        self.assertEqual(get_nth_device_from_idmef("Target", 1).find("Node/name").text, "example.com",
                         "Hostname of second target was not converted properly from IDEA to IDMEF message")

    def test_ipv4_conversion(self):
        self.assertListEqual(get_addresses_from_idmef("Source", 0, "ipv4-addr"), ["93.184.216.119"],
                             "IPv4 addresses of first source was not converted properly from IDEA to IDMEF message")
        self.assertListEqual(get_addresses_from_idmef("Source", 1, "ipv4-addr"), ["93.184.216.119", "93.184.216.120"],
                             "IPv4 addresses of second source was not converted properly from IDEA to IDMEF message")
        self.assertListEqual(get_addresses_from_idmef("Target", 0, "ipv4-addr"), ["0.184.216.119"],
                             "IPv4 addresses of first target was not converted properly from IDEA to IDMEF message")
        self.assertListEqual(get_addresses_from_idmef("Target", 1, "ipv4-addr"), ["0.0.216.119"],
                             "IPv4 addresses of second target was not converted properly from IDEA to IDMEF message")


    def test_ipv6_conversion(self):
        self.assertListEqual(get_addresses_from_idmef("Source", 0, "ipv6-addr"), ["2001:db8::2:1", "2001:db8:a::123/64"],
                             "IPv6 addresses of first source was not converted properly from IDEA to IDMEF message")
        self.assertListEqual(get_addresses_from_idmef("Source", 1, "ipv6-addr"), ["2001:db8::2:1", "2001:db8:a::123/64"],
                             "IPv6 addresses of second source was not converted properly from IDEA to IDMEF message")
        self.assertListEqual(get_addresses_from_idmef("Target", 0, "ipv6-addr"), ["0:db8::2:1", "2001:db8:a::123/64"],
                             "IPv6 addresses of first target was not converted properly from IDEA to IDMEF message")
        self.assertListEqual(get_addresses_from_idmef("Target", 1, "ipv6-addr"), ["0:0::2:1", "00:db8:a::123/64"],
                             "IPv6 addresses of second target was not converted properly from IDEA to IDMEF message")

    def test_mac_conversion(self):
        self.assertListEqual(get_addresses_from_idmef("Source", 0, "mac"), ["01:23:45:67:89:ab", "01:23:45:67:89:cd"],
                             "Mac addresses of first source was not converted properly from IDEA to IDMEF message")
        self.assertListEqual(get_addresses_from_idmef("Source", 1, "mac"), ["01:23:45:67:89:ab", "01:23:45:67:89:cd"],
                             "Mac addresses of second source was not converted properly from IDEA to IDMEF message")
        self.assertListEqual(get_addresses_from_idmef("Target", 0, "mac"), ["00:00:45:67:89:ab", "00:23:45:67:89:ed"],
                             "Mac addresses of first target was not converted properly from IDEA to IDMEF message")
        self.assertListEqual(get_addresses_from_idmef("Target", 1, "mac"), ["00:00:00:67:89:ab", "00:23:45:67:89:fd"],
                             "Mac addresses of second target was not converted properly from IDEA to IDMEF message")

    def test_email_conversion(self):
        self.assertListEqual(get_addresses_from_idmef("Source", 0, "e-mail"), ["example@example.com", "example2@example2.com"],
                             "Mail addresses of first source was not converted properly from IDEA to IDMEF message")
        self.assertListEqual(get_addresses_from_idmef("Source", 1, "e-mail"), ["example@example.com", "example2@example2.com"],
                             "Mail addresses of second source was not converted properly from IDEA to IDMEF message")
        self.assertListEqual(get_addresses_from_idmef("Target", 0, "e-mail"), ["example00@example.com", "example000@example2.com"],
                             "Mail addresses of first target was not converted properly from IDEA to IDMEF message")
        self.assertListEqual(get_addresses_from_idmef("Target", 1, "e-mail"), ["example00@example.com", "example000@example2.com"],
                             "Mail addresses of second target was not converted properly from IDEA to IDMEF message")


    def test_spoofed_conversion(self):
        self.assertEqual(get_nth_device_from_idmef("Source", 0).get("spoofed"), "False",
                         "Spoofed attribute of first source was not converted properly from IDEA to IDMEF message")
        self.assertEqual(get_nth_device_from_idmef("Source", 1).get("spoofed"), "False",
                         "Spoofed attribute of second source was not converted properly from IDEA to IDMEF message")
        self.assertEqual(get_nth_device_from_idmef("Target", 0).get("decoy"), "True",
                         "Spoofed attribute of first target was not converted properly from IDEA to IDMEF message")
        self.assertEqual(get_nth_device_from_idmef("Target", 1).get("decoy"), "False",
                         "Spoofed attribute of second target was not converted properly from IDEA to IDMEF message")

    def test_router_conversion(self):
        self.assertEqual(get_nth_device_from_idmef("Source", 0).get("interface"), "router1",
                         "Router of first source was not converted properly from IDEA to IDMEF message")
        self.assertEqual(get_nth_device_from_idmef("Source", 1).get("interface"), "router1",
                         "Router of second source was not converted properly from IDEA to IDMEF message")
        self.assertEqual(get_nth_device_from_idmef("Target", 0).get("interface"), "router3",
                         "Router of first target was not converted properly from IDEA to IDMEF message")
        self.assertEqual(get_nth_device_from_idmef("Target", 1).get("interface"), "router5",
                         "Router of second target was not converted properly from IDEA to IDMEF message")

    def test_port_conversion(self):
        self.assertEqual(get_nth_device_from_idmef("Source", 0).find("Service/portlist").text, "245",
                         "Ports of first source was not converted properly from IDEA to IDMEF message")
        self.assertEqual(get_nth_device_from_idmef("Source", 1).find("Service/portlist").text, "210, 542",
                         "Ports of second source was not converted properly from IDEA to IDMEF message")
        self.assertEqual(get_nth_device_from_idmef("Target", 0).find("Service/portlist").text, "80",
                         "Ports of first target was not converted properly from IDEA to IDMEF message")
        self.assertEqual(get_nth_device_from_idmef("Target", 1).find("Service/portlist").text, "210, 542",
                         "Ports of second target was not converted properly from IDEA to IDMEF message")

    def test_proto_conversion(self):
        self.assertEqual(get_nth_device_from_idmef("Source", 0).find("Service/protocol").text, "epmap2",
                         "Ports of first source was not converted properly from IDEA to IDMEF message")
        self.assertEqual(get_nth_device_from_idmef("Source", 1).find("Service/protocol").text, "epmap2",
                         "Ports of second source was not converted properly from IDEA to IDMEF message")
        self.assertEqual(get_nth_device_from_idmef("Target", 0).find("Service/protocol").text, "epmap",
                         "Ports of first target was not converted properly from IDEA to IDMEF message")
        self.assertEqual(get_nth_device_from_idmef("Target", 1).find("Service/protocol").text, "epmap2",
                         "Ports of second target was not converted properly from IDEA to IDMEF message")

    def test_node_name_conversion(self):
        self.assertEqual(get_analyzer_from_idmef().get("name"), "com.example.specific",
                         "Name of analyzer was not converted properly from IDEA to IDMEF message")

    def test_attachments_conversion(self):
        idmef_additional_data = get_idmefalert_from_ideamessage().findall("AdditionalData")
        content_list = []
        self.assertEqual(len(idmef_additional_data), 3, "Length of additional data is not same as attach in IDEA")
        for single_additional_data in idmef_additional_data:
            content_list.append(single_additional_data.find("string").text)
        self.assertListEqual(content_list, ["This is content of the attach", "This is content of the attach",
                                            "This is content of the attach"],
                             "Contents of IDMEF additional data is not the same as content of IDEA attach")


if __name__ == '__main__':
    unittest.main()
