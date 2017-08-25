import unittest
from xml.etree.ElementTree import Element, SubElement

from IdeaAndIdmefConverter.InnerConverterStructure.Helper.ElementTreeHelper import elements_equal
from IdeaAndIdmefConverter.InnerConverterStructure.IdeaToIdmef.ToIdmefMessageConverter \
    import convert_dict_to_elementtree

from IdeaAndIdmefConverter.InnerConverterStructure.IdmefToIdea.ToIdeaMessageConverter import convert_elementtree_to_dict


class StraightConversion(unittest.TestCase):
    def test_xml_to_json(self):
        root = Element("root")
        child1 = SubElement(root, "child1")
        child1.text = "Value1"
        child2 = SubElement(root, "child2")
        child2.text = "Value2"
        child2_second = SubElement(root, "child2")
        child2_second.text = "Value3"
        child2_third = SubElement(root, "child2")
        child2_third.text = "Value4"
        result = {}
        expected_result = {
            "child1": "Value1",
            "child2": [
                "Value2",
                "Value3",
                "Value4"
            ]
        }
        convert_elementtree_to_dict(root, result)
        self.assertDictEqual(result, expected_result)

    def test_xml_to_json2(self):
        root = Element("root")
        child1 = SubElement(root, "child1")
        child11 = SubElement(child1, "child11")
        child111 = SubElement(child11, "child111")
        child111.text = "Value"
        result = {}
        expected_result = {
            "child1": {
                "child11": {
                    "child111": "Value"
                }
            }
        }
        convert_elementtree_to_dict(root, result)
        self.assertDictEqual(result, expected_result)

    def test_xml_to_json3(self):
        root = Element("root")
        child1 = SubElement(root, "child1")
        child11 = SubElement(child1, "child11")
        child111 = SubElement(child11, "child111")
        child111.text = "Value"
        child2 = SubElement(root, "child2")
        child2.text = "Value2"
        child2_second = SubElement(root, "child2")
        child2_second.text = "Value3"
        child2_third = SubElement(root, "child2")
        child2_third.text = "Value4"
        result = {}
        expected_result = {
            "child1": {
                "child11": {
                    "child111": "Value"
                }
            },
            "child2": [
                "Value2",
                "Value3",
                "Value4"
            ]
        }
        convert_elementtree_to_dict(root, result)
        self.assertDictEqual(result, expected_result)

    def test_xml_to_json4(self):
        root = Element("root")
        child1 = SubElement(root, "child1")
        child1.set("attr1", "attr-value1")
        child11 = SubElement(child1, "child11")
        child11.set("attr11", "attr-value11")
        child111 = SubElement(child11, "child111")
        child111.set("attr111", "attr-value111")
        child111.text = "Value"
        child2 = SubElement(root, "child2")
        child2.set("attr2", "attr-value2")
        child2.text = "Value2"
        child2_second = SubElement(root, "child2")
        child2_second.set("attr2", "attr-value2")
        child2_second.text = "Value3"
        child2_third = SubElement(root, "child2")
        child2_third.set("attr2", "attr-value2")
        child2_third.text = "Value4"
        result = {}
        expected_result = {
            "child1": {
                "@attr1": "attr-value1",
                "child11": {
                    "@attr11": "attr-value11",
                    "child111": {
                        "#text": "Value",
                        "@attr111": "attr-value111"
                    }
                }
            },
            "child2": [
                {
                    "@attr2": "attr-value2",
                    "#text": "Value2"
                },
                {
                    "@attr2": "attr-value2",
                    "#text": "Value3"
                },
                {
                    "@attr2": "attr-value2",
                    "#text": "Value4"
                }
            ]
        }
        convert_elementtree_to_dict(root, result)
        self.assertDictEqual(result, expected_result)

    def test_xml_to_json5(self):
        root = Element("root$converted$")
        child1 = SubElement(root, "child1$converted$")
        child1.text = "Value1"
        child2 = SubElement(root, "child2")
        child2.text = "Value2"
        child2_second = SubElement(root, "child2")
        child2_second.text = "Value3"
        child2_third = SubElement(root, "child2")
        child2_third.text = "Value4"
        result = {}
        expected_result = {
            "child2": [
                "Value2",
                "Value3",
                "Value4"
            ]
        }
        convert_elementtree_to_dict(root, result)
        self.assertDictEqual(result, expected_result)

    def test_xml_to_json6(self):
        root = Element("root$converted$")
        child1 = SubElement(root, "child1$converted$")
        child1.text = "Value1"
        child2 = SubElement(root, "child2$converted$")
        child2.text = "Value2"
        child2_second = SubElement(root, "child2")
        child2_second.text = "Value3"
        child2_third = SubElement(root, "child2")
        child2_third.text = "Value4"
        result = {}
        expected_result = {
            "child2": [
                "Value3",
                "Value4"
            ]
        }
        convert_elementtree_to_dict(root, result)
        self.assertDictEqual(result, expected_result)

    def test_dict_to_elementtree(self):
        test_data = {
            "child1": "Value1",
            "child2": [
                "Value2",
                "Value3",
                "Value4",
            ]
        }
        root = Element("root")
        child1 = SubElement(root, "child1")
        child1.text = "Value1"
        child2 = SubElement(root, "child2")
        child2.text = "Value2"
        child2_second = SubElement(root, "child2")
        child2_second.text = "Value3"
        child2_third = SubElement(root, "child2")
        child2_third.text = "Value4"
        expected_result = root
        result = Element("root")
        convert_dict_to_elementtree(test_data, result)
        self.assertTrue(elements_equal(result, expected_result))

    def test_dict_to_elementtree2(self):
        test_data = {
            "child1": {
                "child11": {
                    "child111": "Value"
                }
            }
        }
        root = Element("root")
        child1 = SubElement(root, "child1")
        child11 = SubElement(child1, "child11")
        child111 = SubElement(child11, "child111")
        child111.text = "Value"
        expected_result = root
        result = Element("root")
        convert_dict_to_elementtree(test_data, result)
        self.assertTrue(elements_equal(result, expected_result))

    def test_dict_to_elementtree3(self):
        test_data = {
            "child1": {
                "child11": {
                    "child111": "Value"
                }
            },
            "child2": [
                "Value2",
                "Value3",
                "Value4"
            ]
        }
        root = Element("root")
        child1 = SubElement(root, "child1")
        child11 = SubElement(child1, "child11")
        child111 = SubElement(child11, "child111")
        child111.text = "Value"
        child2 = SubElement(root, "child2")
        child2.text = "Value2"
        child2_second = SubElement(root, "child2")
        child2_second.text = "Value3"
        child2_third = SubElement(root, "child2")
        child2_third.text = "Value4"
        expected_result = root
        result = Element("root")
        convert_dict_to_elementtree(test_data, result)
        self.assertTrue(elements_equal(result, expected_result))

    def test_dict_to_elementtree4(self):
        test_data = {
            "child1": {
                "@attr1": "attr-value1",
                "child11": {
                    "@attr11": "attr-value11",
                    "child111": {
                        "#text": "Value",
                        "@attr111": "attr-value111"
                    }
                }
            },
            "child2": [
                {
                    "@attr2": "attr-value2",
                    "#text": "Value2"
                },
                {
                    "@attr2": "attr-value2",
                    "#text": "Value3"
                },
                {
                    "@attr2": "attr-value2",
                    "#text": "Value4"
                }
            ]
        }
        root = Element("root")
        child1 = SubElement(root, "child1")
        child1.set("attr1", "attr-value1")
        child11 = SubElement(child1, "child11")
        child11.set("attr11", "attr-value11")
        child111 = SubElement(child11, "child111")
        child111.set("attr111", "attr-value111")
        child111.text = "Value"
        child2 = SubElement(root, "child2")
        child2.set("attr2", "attr-value2")
        child2.text = "Value2"
        child2_second = SubElement(root, "child2")
        child2_second.set("attr2", "attr-value2")
        child2_second.text = "Value3"
        child2_third = SubElement(root, "child2")
        child2_third.set("attr2", "attr-value2")
        child2_third.text = "Value4"
        expected_result = root
        result = Element("root")
        convert_dict_to_elementtree(test_data, result)
        self.assertTrue(elements_equal(result, expected_result))

    def test_dict_to_elementtree5(self):
        test_data = {
            "child2$converted$": [
                "Value1"
                "Value2",
                "Value3",
                "Value4"
            ]
        }
        root = Element("root")
        expected_result = root
        result = Element("root")
        convert_dict_to_elementtree(test_data, result)
        self.assertTrue(elements_equal(result, expected_result))

    def test_dict_to_elementtree6(self):
        test_data = {
            "child1$converted$": "Value1",
            "child2": "Value2",
            "child3": {
                "child31": "Value31",
                "child32$converted$": "Value32",
                "child33": "Value33",
                "child34": {
                    "child341$converted$": "Value341"
                }
            }
        }
        root = Element("root")
        child2 = SubElement(root, "child2")
        child2.text = "Value2"
        child3 = SubElement(root, "child3")
        child31 = SubElement(child3, "child31")
        child31.text = "Value31"
        child33 = SubElement(child3, "child33")
        child33.text = "Value33"
        expected_result = root
        result = Element("root")
        convert_dict_to_elementtree(test_data, result)
        self.assertTrue(elements_equal(result, expected_result))

if __name__ == '__main__':
    unittest.main()

