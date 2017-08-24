import os
import unittest
from xml.etree.ElementTree import Element, SubElement

from IdeaAndIdmefConverter.InnerConverterStructure.Helper.IdeaParsingHelper import correct_braces
from IdeaAndIdmefConverter.InnerConverterStructure.Helper.ElementTreeHelper import elements_equal, idmefmessage_tag_tostring, tag_element_converted, \
    tag_attribute_converted, get_elementvalue, get_elementvalues, get_elementattribute, get_elementattributes


def correct_braces_message(test_string, expected_bool):
    if expected_bool:
        return "String " + test_string + " has correct braces, but function returned false"
    else:
        return "String " + test_string + " has not correct braces, but function returned true"


class HelperMethodTests(unittest.TestCase):
    def test_elements_equal_different_root(self):
        root1 = Element("root")
        root2 = Element("different")
        self.assertFalse(elements_equal(root1, root2))

    def test_elements_equal_same_root(self):
        root1 = Element("root")
        root2 = Element("root")
        self.assertTrue(elements_equal(root1, root2))

    def test_elements_equal_deep_same(self):
        root1 = Element("root")
        child1 = SubElement(root1, "child1")
        child1.set("attr", "attr")
        child1.text = "Value"
        child11 = SubElement(child1, "child11")
        child111 = SubElement(child11, "child111")
        child111.text = "Value"
        child1111 = SubElement(child111, "child1111")
        child1111.set("attrib", "attrib")

        root2 = Element("root")
        child2 = SubElement(root2, "child1")
        child2.set("attr", "attr")
        child2.text = "Value"
        child22 = SubElement(child2, "child11")
        child222 = SubElement(child22, "child111")
        child222.text = "Value"
        child2222 = SubElement(child222, "child1111")
        child2222.set("attrib", "attrib")
        self.assertTrue(elements_equal(root1, root2))

    def test_elements_equal_deep_different(self):
        root1 = Element("root")
        child1 = SubElement(root1, "child1")
        child1.set("attr", "attr")
        child1.text = "Value"
        child11 = SubElement(child1, "child11")
        child111 = SubElement(child11, "child111")
        child111.text = "Value"
        child1111 = SubElement(child111, "child1111")
        child1111.set("attrib", "attrib")

        root2 = Element("root")
        child2 = SubElement(root2, "child1")
        child2.set("attr", "attr")
        child2.text = "Value"
        child22 = SubElement(child2, "chi!!difference!!ld11")
        child222 = SubElement(child22, "child111")
        child222.text = "Value"
        child2222 = SubElement(child222, "child1111")
        child2222.set("attrib", "attrib")
        self.assertFalse(elements_equal(root1, root2))

    def test_element_equal_wide_same(self):
        root1 = Element("root")
        child1 = SubElement(root1, "child1")
        child11 = SubElement(root1, "child11")
        child111 = SubElement(root1, "child111")
        child1.set("attrib1", "value1")
        child1.set("attrib11", "value1")
        child111.text = "text1"

        root2 = Element("root")
        child2 = SubElement(root2, "child1")
        child22 = SubElement(root2, "child11")
        child222 = SubElement(root2, "child111")
        child2.set("attrib1", "value1")
        child2.set("attrib11", "value1")
        child222.text = "text1"
        self.assertTrue(elements_equal(root1, root2))

    def test_element_equal_wide_different(self):
        root1 = Element("root")
        child1 = SubElement(root1, "child1")
        child11 = SubElement(root1, "child11")
        child111 = SubElement(root1, "child111")
        child1.set("attrib1", "value1")
        child1.set("attrib11", "value1")
        child111.text = "text1"

        root2 = Element("root")
        child2 = SubElement(root2, "child1")
        child22 = SubElement(root2, "child11")
        child222 = SubElement(root2, "child111")
        child2.set("attrib1", "value1")
        child2.set("attrib12", "value1")
        child222.text = "text1"
        self.assertFalse(elements_equal(root1, root2))

    def test_idmefmessage_tag_tostring(self):
        expected_first = "<?xml version='1.0' encoding='UTF-8'?><IDMEF-Messages>"
        if os.name == "nt":
            expected_first = "<?xml version='1.0' encoding='cp1250'?>\n<IDMEF-Messages>"
        expected_second = "</IDMEF-Messages>"
        first, second = idmefmessage_tag_tostring("IDMEF-Messages")
        first = first.replace(os.linesep, "")
        second = second.replace(os.linesep, "")
        self.assertEqual(first, expected_first)
        self.assertEqual(second, expected_second)

    def test_tag_element_converted(self):
        root = Element("root")
        subelement = SubElement(root, "subelement")
        tag_element_converted(subelement)
        expected_roottag = "root"
        expected_subelementtag = "subelement$converted$"
        self.assertEqual(root.tag, expected_roottag)
        self.assertEqual(subelement.tag, expected_subelementtag)

    def test_tag_attribute_converted(self):
        root = Element("root")
        subelement = SubElement(root, "child")
        subelement.set("attr", "attr-value")
        tag_attribute_converted(subelement, "attr")
        expected_root = "root"
        expected_subelement = "child"
        expected_attribute_value = "attr-value"
        attribute_value = subelement.get("attr$converted$", None)
        self.assertEqual(root.tag, expected_root)
        self.assertEqual(subelement.tag, expected_subelement)
        self.assertEqual(attribute_value, expected_attribute_value)

    def test_tag_attribute_converted_empty_attribute(self):
        root = Element("root")
        subelement = SubElement(root, "child")
        tag_attribute_converted(subelement, "attr")
        expected_root = "root"
        expected_subelement = "child"
        attribute_value = subelement.get("attr$converted$", None)
        self.assertEqual(root.tag, expected_root)
        self.assertEqual(subelement.tag, expected_subelement)
        self.assertIsNone(attribute_value)

    def test_get_elementvalue_getroot(self):
        root = Element("root")
        child1 = SubElement(root, "child1")
        root.text = "Text"
        expected_result = root.text
        result = get_elementvalue(root, ".", True)
        self.assertEqual(expected_result, result)

    def test_get_elementvalue_getlistelement_from_root(self):
        root = Element("root")
        child1 = SubElement(root, "child1")
        child1.set("attr", "attr")
        child1.text = "Value2"
        child11 = SubElement(child1, "child11")
        child111 = SubElement(child11, "child111")
        child111.text = "Value"
        child1111 = SubElement(child111, "child1111")
        child1111.set("attrib", "attrib")
        expected_result = child111.text
        result = get_elementvalue(root, "child1/child11/child111", True)
        self.assertEqual(expected_result, result)

    def test_get_elementvalue_getlistelement_from_parent(self):
        root = Element("root")
        child1 = SubElement(root, "child1")
        child1.set("attr", "attr")
        child1.text = "Value2"
        child11 = SubElement(child1, "child11")
        child111 = SubElement(child11, "child111")
        child111.text = "Value"
        child1111 = SubElement(child111, "child1111")
        child1111.set("attrib", "attrib")
        expected_result = child111.text
        result = get_elementvalue(child11, "child111", True)
        self.assertEqual(expected_result, result)

    def test_get_elementvalue_same_elements(self):
        root = Element("root")
        child1 = SubElement(root, "child1")
        child1.set("attr", "attr")
        child1.text = "Value2"
        child11 = SubElement(child1, "child11")
        child111 = SubElement(child11, "child111")
        child111.text = "Value"
        child1111 = SubElement(child111, "child1111")
        child1111.set("attrib", "attrib")
        child2 = SubElement(root, "child1")
        child2.set("attr", "attr")
        child2.text = "Different"
        expected_result = child1.text
        result = get_elementvalue(root, "child1", True)
        self.assertEqual(expected_result, result)

    def test_get_elementvalues_root(self):
        root = Element("root")
        root.text = "Roottext"
        child1 = SubElement(root, "child1")
        child1.set("attr", "attr")
        child1.text = "Value2"
        child11 = SubElement(child1, "child11")
        child111 = SubElement(child11, "child111")
        child111.text = "Value"
        child1111 = SubElement(child111, "child1111")
        child1111.set("attrib", "attrib")
        child2 = SubElement(root, "child1")
        child2.set("attr", "attr")
        child2.text = "Different"
        child2.text = "Different"
        expected_result = [root.text]
        result = get_elementvalues(root, ".", True)
        self.assertListEqual(expected_result, result)

    def test_get_elementvalues_list(self):
        root = Element("root")
        root.text = "Roottext"
        child1 = SubElement(root, "child1")
        child1.set("attr", "attr")
        child1.text = "Value2"
        child11 = SubElement(child1, "child11")
        child111 = SubElement(child11, "child111")
        child111.text = "Value"
        child1111 = SubElement(child111, "child1111")
        child1111.set("attrib", "attrib")
        child2 = SubElement(root, "child1")
        child3 = SubElement(root, "child1")
        child2.set("attr", "attr")
        child2.text = "Different"
        child3.text = "Different"
        expected_result = [child1.text, child2.text, child3.text]
        result = get_elementvalues(root, "child1", True)
        self.assertListEqual(expected_result, result)

    def test_get_elementattribute(self):
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
        expected_result = child1.get("attr1")
        result = get_elementattribute(root, "child1", "attr1", True, default_value=None)
        self.assertEqual(expected_result, result)

    def test_get_elementattribute_nonexisting_attribute(self):
        root = Element("root")
        child1 = SubElement(root, "child1")
        child1.set("attr1", "attr-value1")
        result = get_elementattribute(root, ".", "nonexisting", True, default_value=None)
        self.assertIsNone(result)

    def test_get_elementattribute_more_attributes(self):
        root = Element("root")
        child1 = SubElement(root, "child1")
        child1.set("attr", "value1")
        child2 = SubElement(root, "child1")
        child2.set("attr", "value2")
        child3 = SubElement(root, "child1")
        child3.set("attr", "value3")
        child4 = SubElement(root, "child1")
        child4.set("attr", "value4")
        expected_result = child1.get("attr")
        result = get_elementattribute(root, "child1", "attr", True, default_value=None)
        self.assertEqual(expected_result, result)

    def test_get_elementattributes_single_attribute(self):
        root = Element("root")
        root.text = "Roottext"
        child1 = SubElement(root, "child1")
        child1.set("attr", "attr")
        child1.text = "Value2"
        child11 = SubElement(child1, "child11")
        child111 = SubElement(child11, "child111")
        child111.text = "Value"
        child1111 = SubElement(child111, "child1111")
        child1111.set("attrib", "attrib")
        child2 = SubElement(root, "child1")
        child2.set("attr", "attr")
        expected_result = [child1111.get("attrib")]
        result = get_elementattributes(root, "child1/child11/child111/child1111", "attrib", True)
        self.assertListEqual(expected_result, result)

    def test_get_elementattributes_multiple_attributes(self):
        root = Element("root")
        child1 = SubElement(root, "child1")
        child1.set("attr", "value1")
        child2 = SubElement(root, "child1")
        child2.set("attr", "value2")
        child3 = SubElement(root, "child1")
        child3.set("attr", "value3")
        child4 = SubElement(root, "child1")
        child4.set("attr", "value4")
        expected_result = [child1.get("attr"), child2.get("attr"), child3.get("attr"), child4.get("attr")]
        result = get_elementattributes(root, "child1", "attr", True)
        self.assertListEqual(expected_result, result)

    def test_correct_braces_empty_string(self):
        test_string = ""
        self.assertTrue(correct_braces(test_string), correct_braces_message(test_string, True))

    def test_correct_braces_none_string(self):
        test_string = None
        with self.assertRaises(ValueError):
            correct_braces(test_string)

    def test_correct_braces_just_correct_braces(self):
        test_string1 = "{}"
        test_string2 = "{{{{}}}}"
        self.assertTrue(correct_braces(test_string1), correct_braces_message(test_string1, True))
        self.assertTrue(correct_braces(test_string2), correct_braces_message(test_string2, True))

    def test_correct_braces_just_incorrect_braces(self):
        test_string1 = "{"
        test_string2 = "}"
        test_string3 = "{{{}}{"
        test_string4 = "{}}}{}{}{}"
        test_string5 = "{{{{{"
        test_string6 = "}}}}}"
        test_string7 = "}{"
        self.assertFalse(correct_braces(test_string1), correct_braces_message(test_string1, False))
        self.assertFalse(correct_braces(test_string2), correct_braces_message(test_string2, False))
        self.assertFalse(correct_braces(test_string3), correct_braces_message(test_string3, False))
        self.assertFalse(correct_braces(test_string4), correct_braces_message(test_string4, False))
        self.assertFalse(correct_braces(test_string5), correct_braces_message(test_string5, False))
        self.assertFalse(correct_braces(test_string6), correct_braces_message(test_string6, False))
        self.assertFalse(correct_braces(test_string7), correct_braces_message(test_string7, False))

    def test_correct_braces_with_text_correct(self):
        test_string1 = "{random string}"
        test_string2 = "t{his{is}correct}really"
        test_string3 = "{correct{correct{correct{correct{}correct}correct}correct}correct}"
        test_string4 = ":{456adf{adf8.,-%}}*?"
        self.assertTrue(correct_braces(test_string1), correct_braces_message(test_string1, True))
        self.assertTrue(correct_braces(test_string2), correct_braces_message(test_string2, True))
        self.assertTrue(correct_braces(test_string3), correct_braces_message(test_string3, True))
        self.assertTrue(correct_braces(test_string4), correct_braces_message(test_string4, True))

    def test_correct_braces_with_text_incorrect(self):
        test_string1 = "{random string"
        test_string2 = "random string}"
        test_string3 = "so{me}next{{r}}and}{omstring"
        test_string4 = "{some}}next{{rnd}"
        test_string5 = "}t:::e,,,s6545t{"
        self.assertFalse(correct_braces(test_string1), correct_braces_message(test_string1, False))
        self.assertFalse(correct_braces(test_string2), correct_braces_message(test_string2, False))
        self.assertFalse(correct_braces(test_string3), correct_braces_message(test_string3, False))
        self.assertFalse(correct_braces(test_string4), correct_braces_message(test_string4, False))
        self.assertFalse(correct_braces(test_string5), correct_braces_message(test_string5, False))

    def test_correct_braces_with_quotes_correct(self):
        test_string1 = '{"{adfafdsf{{{fds{}"}{}{text}{"}"}'
        test_string2 = '"}{"'
        self.assertTrue(correct_braces(test_string1), correct_braces_message(test_string1, True))
        self.assertTrue(correct_braces(test_string2), correct_braces_message(test_string2, True))

    def test_correct_braces_with_quotes_incorrect(self):
        test_string1 = '"}{"}{}{}{"}{"'
        test_string2 = '{"hello{}{}{}{{}}}}""{}"hello'
        test_string3 = '}"{ok}"{'
        self.assertFalse(correct_braces(test_string1), correct_braces_message(test_string1, False))
        self.assertFalse(correct_braces(test_string2), correct_braces_message(test_string2, False))
        self.assertFalse(correct_braces(test_string3), correct_braces_message(test_string3, False))


if __name__ == '__main__':
    unittest.main()
