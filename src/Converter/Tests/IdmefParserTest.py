import unittest

from IdeaAndIdmefConverter.InnerConverterStructure.IdmefToIdea.IdmefParser import IdmefParser

from IdeaAndIdmefConverter.InnerConverterStructure.Helper.ElementTreeHelper import remove_beginend_whitespaces
from Tests.IdmefMessageString import get_idmef_string


def message(element_name, error):
    if error == "tag":
        return "Element" + element_name + " has wrong tag"
    elif error == "attrib":
        return "Element " + element_name + " has wrong attributes"
    elif error == "childrencount":
        return "Element " + element_name + " has wrong number of children"
    elif error == "elementscount":
        return "There is different number of " + element_name + " elements in parsed idmef"
    elif error == "text":
        return "Element" + element_name + " has wrong value"


def get_linkage_names(root):
    linkage_names = root.findall("Target/File/Linkage/name")
    names_text = []
    for linkage_name in linkage_names:
        names_text.append(remove_beginend_whitespaces(linkage_name.text))
    return names_text


class SingleIdmefMessageParserTest(unittest.TestCase):

    def test_parsed_from_string(self):
        idmef_parser = IdmefParser(get_idmef_string())
        alert = idmef_parser.parse_string()
        self.generic_test(alert, "Alert", {"messageid": "123d45"}, 13)

        linkage_names = get_linkage_names(alert)
        self.assertEqual(len(linkage_names), 4, message("Linkage name", "elementscount"))
        self.assertListEqual(linkage_names, ["FsObject", "FsObject", "FsObject", "FsObject"])

    def get_root(self):
        with open("InputTestData/longidmef.xml", "r") as input_file:
            idmef_parser = IdmefParser(input_file)
            result_root = idmef_parser.parse_file_partially()
            result_root = result_root.__next__()
        return result_root

    def generic_test(self, element, expected_tag, expected_attrib=None, expected_children_length=None,
                     expected_text=None):
        self.assertEqual(element.tag, expected_tag, message(expected_tag, "tag"))
        if expected_attrib:
            self.assertDictEqual(element.attrib, expected_attrib, message(expected_tag, "attrib"))
        if expected_children_length:
            self.assertEqual(len(list(element)), expected_children_length, message(expected_tag, "childrencount"))
        if expected_text:
            self.assertEqual(remove_beginend_whitespaces(element.text), expected_text, message(expected_tag, "text"))

    def test_alert(self):
        alert = self.get_root()
        self.generic_test(alert, "Alert", {"messageid": "123d45"}, 13)

    def test_analyzer(self):
        result_root = self.get_root()
        analyzers = result_root.findall("Analyzer")
        self.assertEqual(len(analyzers), 1, message("Analyzer", "elementscount"))
        analyzer = analyzers[0]
        self.generic_test(analyzer, "Analyzer", {"analyzerid": "5468",
                                                 "name": "DetectorExample",
                                                 "manufacturer": "Great s.r.o",
                                                 "model": "detector great",
                                                 "version": "2.0",
                                                 "class": "highest",
                                                 "ostype": "Linux",
                                                 "osversion": "4.4.0-31-generic"}, 2)

    def test_createtime(self):
        result_root = self.get_root()
        createtimes = result_root.findall("CreateTime")
        self.assertEqual(len(createtimes), 1, message("CreateTime", "elementscount"))
        createtime = createtimes[0]
        self.generic_test(createtime, "CreateTime", {"ntpstamp": "0xbc723b45.0xef449129"}, 0,
                          "2000-03-09T10:01:25.93464-05:00")

    def test_classification(self):
        result_root = self.get_root()
        classifications = result_root.findall("Classification")
        self.assertEqual(len(classifications), 1, message("Classification", "elementscount"))
        classification = classifications[0]
        self.generic_test(classification, "Classification", {"ident": "1", "text": "Phishing"}, 1)

    def test_detecttime(self):
        result_root = self.get_root()
        detecttimes = result_root.findall("DetectTime")
        self.assertEqual(len(detecttimes), 1, message("DetectTime", "elementscount"))
        detecttime = detecttimes[0]
        self.generic_test(detecttime, "DetectTime", {"ntpstamp": "0xbc723b45.0xef449129"}, 0,
                          "2017-03-04T15:10:52.86445Z")

    def test_analyzertime(self):
        result_root = self.get_root()
        analyzertimes = result_root.findall("AnalyzerTime")
        self.assertEqual(len(analyzertimes), 1, message("AnalyzerTime", "elementscount"))
        analyzertime = analyzertimes[0]
        self.generic_test(analyzertime, "AnalyzerTime", {"ntpstamp": "2017-03-03T19:10:52.86445Z"}, 0,
                          "2017-03-03T19:10:52.86445Z")

    def test_sources_count(self):
        result_root = self.get_root()
        sources = result_root.findall("Source")
        self.assertEqual(len(sources), 2, message("Source", "elementscount"))

    def test_targets_count(self):
        result_root = self.get_root()
        targets = result_root.findall("Target")
        self.assertEqual(len(targets), 2, message("Target", "elementscount"))

    def test_first_source(self):
        result_root = self.get_root()
        source = result_root.findall("Source")[0]
        self.generic_test(source, "Source", {"ident": "2", "spoofed": "yes", "interface": "interfaceExample"}, 4)

    def test_second_source(self):
        result_root = self.get_root()
        source = result_root.findall("Source")[1]
        self.generic_test(source, "Source", {"ident": "3", "spoofed": "unknown", "interface": "interfaceExample2"}, 4)

    def test_first_target(self):
        result_root = self.get_root()
        target = result_root.findall("Target")[0]
        self.generic_test(target, "Target", {"ident": "4", "decoy": "no", "interface": "interfaceExample3"}, 6)

    def test_second_target(self):
        result_root = self.get_root()
        target = result_root.findall("Target")[1]
        self.generic_test(target, "Target", {"ident": "5", "decoy": "yes", "interface": "interfaceExample4"}, 6)

    def test_assessment(self):
        result_root = self.get_root()
        assessments = result_root.findall("Assessment")
        self.assertEqual(len(assessments), 1, message("Assessment", "elementscount"))
        assessment = assessments[0]
        self.generic_test(assessment, "Assessment", expected_children_length=4)

    def test_correlationalert(self):
        result_root = self.get_root()
        correlation_alerts = result_root.findall("CorrelationAlert")
        self.assertEqual(len(correlation_alerts), 1, message("CorrelationAlert", "elementscount"))
        correlation_alert = correlation_alerts[0]
        self.generic_test(correlation_alert, "CorrelationAlert", expected_children_length=3)

    def test_additionaldata_count(self):
        result_root = self.get_root()
        additional_data = result_root.findall("AdditionalData")
        self.assertEqual(len(additional_data), 2, message("AdditionalData", "elementscount"))

    def test_first_additionaldata(self):
        result_root = self.get_root()
        first_additional_data = result_root.findall("AdditionalData")[0]
        self.generic_test(first_additional_data, "AdditionalData", {"meaning": "Test additional data"}, 0,
                          "First additional data test example")

    def test_second_additionaldata(self):
        result_root = self.get_root()
        second_additional_data = result_root.findall("AdditionalData")[1]
        self.generic_test(second_additional_data, "AdditionalData", {"meaning": "Test additional data too"}, 0,
                          "Second additional data test example")

    def test_analyzer_addresses(self):
        result_root = self.get_root()
        analyzer_addresses = result_root.findall("Analyzer/Node/Address/address")
        addresses_text = []
        for address in analyzer_addresses:
            addresses_text.append(remove_beginend_whitespaces(address.text))
        self.assertListEqual(addresses_text, ["93.184.216.119", "100.184.216.119"])

    def test_sources_userid_number(self):
        result_root = self.get_root()
        userid_numbers = result_root.findall("Source/User/UserId/number")
        numbers_value = []
        for userid_number in userid_numbers:
            numbers_value.append(remove_beginend_whitespaces(userid_number.text))
        self.assertListEqual(numbers_value, ["51", "14"])


class MultipleIdmefMessageParserTest(unittest.TestCase):
    def generic_test(self, element, expected_tag, expected_attrib=None, expected_children_length=None,
                     expected_text=None):
        self.assertEqual(element.tag, expected_tag, message(expected_tag, "tag"))
        if expected_attrib:
            self.assertDictEqual(element.attrib, expected_attrib, message(expected_tag, "attrib"))
        if expected_children_length:
            self.assertEqual(len(list(element)), expected_children_length, message(expected_tag, "childrencount"))
        if expected_text:
            self.assertEqual(element.text, expected_text, message(expected_tag, "text"))

    def test_messages_count(self):
        with open("InputTestData/multiplelongidmef.xml", "r") as input_file:
            idmef_parser = IdmefParser(input_file)
            i = 0
            for _ in idmef_parser.parse_file_partially():
                i += 1
        self.assertEqual(i, 2, "Number of messages is different as it is in file")

    def test_alerts(self):
        with open("InputTestData/multiplelongidmef.xml", "r") as input_file:
            idmef_parser = IdmefParser(input_file)
            message_generator = idmef_parser.parse_file_partially()
            self.generic_test(message_generator.__next__(), "Alert", expected_children_length=6)
            self.generic_test(message_generator.__next__(), "Alert", {"messageid": "abc123456789"}, 7)

    def test_chosen_values_first_message(self):
        with open("InputTestData/multiplelongidmef.xml", "r") as input_file:
            idmef_parser = IdmefParser(input_file)
            message_generator = idmef_parser.parse_file_partially()
            impacts = message_generator.__next__().findall("Assessment/Impact")
            self.assertEqual(len(impacts), 1, message("Impact", "elementscount"))
            impact = impacts[0]
            self.generic_test(impact, "Impact", {"severity": "high", "completion": "succeeded", "type": "admin"}, 0)

    def test_chosen_values_second_message(self):
        with open("InputTestData/multiplelongidmef.xml", "r") as input_file:
            idmef_parser = IdmefParser(input_file)
            message_generator = idmef_parser.parse_file_partially()
            message_generator.__next__()
            services = message_generator.__next__().findall("Target/Service")
            self.assertEqual(len(services), 1, message("Impact", "elementscount"))
            service = services[0]
            self.generic_test(service, "Service", {"ident": "t01-4"}, 2)


if __name__ == '__main__':
    unittest.main()
