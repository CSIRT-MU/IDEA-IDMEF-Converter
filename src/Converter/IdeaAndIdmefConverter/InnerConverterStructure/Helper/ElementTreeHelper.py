import os
import re
from xml.etree.ElementTree import Element, tostring, ElementTree
import xml.etree.ElementTree as ElTree
from io import StringIO


def idmefmessage_tag_tostring(root_tag):
    """
    Make XML tag from root_tag string with declaration

    :param root_tag: tag to be returned in xml
    :return: pair of declaration + start tag, and end tag
    """

    if root_tag:
        simple_root = Element(root_tag)
    else:
        simple_root = Element("SimpleRandomRoot")
    # simple_root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
    # xml_string = tostring(simple_root, short_empty_elements=False, encoding="unicode")
    tmp_stream = StringIO()
    elementtree = ElementTree(simple_root)
    elementtree.write(tmp_stream, encoding='unicode', xml_declaration=True, short_empty_elements=False)
    root_string = tmp_stream.getvalue()
    if root_tag:
        simple_root = Element(root_tag)
        start_roottag = re.search('<.*?>.*?<' + root_tag + '.*?>', root_string, flags=re.DOTALL).group()
        end_roottag = re.search('</' + root_tag + '.*?>', root_string).group()
    else:
        start_roottag = re.search('<.*?xml.*?>', root_string, flags=re.DOTALL).group()
        end_roottag = ""
    return start_roottag + os.linesep, end_roottag + os.linesep


def namespace(element):
    """
    Gets XML namespace of element

    :param element: element, whose tag carry namespace
    :return: namespace of element, if element does not have one, return empty string
    """

    m = re.match('\{.*\}', element.tag)
    return m.group(0) if m else ''


def remove_beginend_whitespaces(input_string):
    """
    Applies lstrip and rstrip methods to input_string

    :param input_string: string to be stripped
    :return: stripped input_string or None, if string is None or ""
    """
    if input_string:
        input_string = input_string.lstrip()
        return input_string.rstrip()
    return None


def tag_element_converted(element):
    """
    Concats label $converted$ to tag of element

    :param element: element, which tag will be tagged as converted
    """
    element.tag += "$converted$"


def tag_attribute_converted(element, attribute):
    """
    Concats label $converted$ to key of specific attribute

    :param element: element, which attribute key will be tagged as converted
    :param attribute: key of attribute to be tagged
    """
    attr_value = element.get(attribute, None)
    if attr_value:
        element.set(attribute + "$converted$", attr_value)
        element.attrib.pop(attribute, None)


def get_elementvalue(element, xpath, tag_converted, default_value=None):
    """Gets value of element specified in xpath, relative to specific element

    :param element: element, which behave as root to xpath
    :param xpath: path from element in argument to element, which value should be retrieved
    :param tag_converted: boolean, if true element will be tagged as converted
    :param default_value: value, which will be returned if xpath or value at xpath does not exists
    :return: if there is element, which matches the xpath, return text of element, otherwise return None
    """

    if element is not None:
        subelement = element.find(xpath)
        if subelement is not None:
            if tag_converted:
                tag_element_converted(subelement)
            if subelement.text:
                return remove_beginend_whitespaces(subelement.text)
        return default_value
    return None


def get_elementvalues(element, xpath, tag_converted):
    """Gets value of multiple elements matching single xpath, relative to specific element

    :param element: element, which behave as root to xpath
    :param xpath: path from element in argument to elements, which value should be retrieved
    :param tag_converted: boolean, if true element will be tagged as converted
    :return: list of values of specified elements
    """

    if element is not None:
        subelements = element.findall(xpath)
        listoftexts = []
        for subelement in subelements:
            listoftexts.append(remove_beginend_whitespaces(subelement.text))
            if tag_converted:
                tag_element_converted(subelement)
        return listoftexts
    return None


def get_elementattribute(element, xpath, attribute, tag_converted, default_value):
    """Gets value of attribute of specific element with specified xpath

    :param element: element, which behave as root to xpath
    :param xpath: path from element in argument to element, which attribute value should be retrieved
    :param attribute: name of attribute which value should be retrieved
    :param tag_converted: boolean, if true, attribute will be tagged as converted
    :param default_value: value, which will be returned if xpath or value at xpath does not exists
    :return: if there is element, which matches the xpath, return text of element, otherwise return None
    """

    if element is not None:
        subelement = element.find(xpath)
        if subelement is not None:
            attr_value = subelement.get(attribute, None)
            if tag_converted:
                tag_attribute_converted(subelement, attribute)
            return attr_value if attr_value is not None else default_value
    return default_value


def get_elementattributes(element, xpath, attribute, tag_converted):
    """Gets value of attribute of specific multiple elements matching single xpath

    :param element: element, which behave as root to xpath
    :param xpath: path from element in argument to elements, which attribute value should be retrieved
    :param attribute: name of attribute which value should be retrieved
    :param tag_converted: boolean, if true, attribute will be tagged as converted
    :return: list of values of specified attribute in specified elements
    """

    subelements = element.findall(xpath)
    listofattrs = []
    for subelement in subelements:
        attr_value = subelement.get(attribute, None)
        if tag_converted:
            tag_attribute_converted(subelement, attribute)
        if attr_value is not None:
            listofattrs.append(attr_value)
    return listofattrs


def elements_equal(first_element, second_element):
    """
    Method, which checks if one element is equal to the other element (same tag, text, children, attributes)

    :param first_element: first element for comparison
    :param second_element: second element for comparison
    :return: true, if elements are equal, otherwise false
    """
    if first_element.tag != second_element.tag:
        # print(first_element.tag + "!=" + second_element.tag)
        return False
    if first_element.text != second_element.text:
        #  print(first_element.text + "!=" + second_element.text)
        return False
    if first_element.tail != second_element.tail:
        # print(first_element.tail + "!=" + second_element.tail)
        return False
    if first_element.attrib != second_element.attrib:
        # print(str(first_element.attrib) + "!=" + str(second_element.attrib))
        return False
    if len(first_element) != len(second_element):
        # print(first_element.tag + "has" + str(len(first_element)) + "children," +
        #      second_element.tag + "has" + str(len(second_element)) + "children")
        return False
    first_children = list(first_element)
    second_children = list(second_element)
    for first_child in first_children:
        true_count = 0
        for second_child in second_children:
            if elements_equal(first_child, second_child):
                true_count += 1
        if true_count != 1:
            return False
    return True
