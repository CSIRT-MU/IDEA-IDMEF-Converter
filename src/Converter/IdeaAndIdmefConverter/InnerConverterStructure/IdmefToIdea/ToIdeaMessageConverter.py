from IdeaAndIdmefConverter.InnerConverterStructure.MessageConverter import MessageConverter

from IdeaAndIdmefConverter.InnerConverterStructure.Helper.ElementTreeHelper import get_elementattribute, \
    get_elementvalue, get_elementvalues, get_elementattributes, tag_element_converted, remove_beginend_whitespaces


def save_value_to_dict(dictionary, key, value):
    """
    Prevents from saving empty values (such as None, [], {}) into dictionary

    :param dictionary: dictionary, where value will be saved
    :param key: key of dictionary
    :param value: value of dictionary
    :return: if value saved, return True, otherwise return false
    """
    if value:
        if isinstance(value, list) and any(x is None for x in value):
            return False
        dictionary[key] = value
        return True
    return False


def save_addresses(idmef_element, device_dict, tag_converted):
    """
    Save addresses from specific idmef node into device (means "Source" or "Target") in IDEA representing by dictionary

    :param idmef_element: idmef device element ("Source" or "Target")
    :param device_dict: device ("Source" or "Target") dictionary, where addresses will be saved
    :param tag_converted: boolean, which says if addresses should be tag as converted
    """
    save_value_to_dict(device_dict, "IP4",
                       get_elementvalues(idmef_element, "Node/Address[@category='ipv4-addr']/address", tag_converted))
    save_value_to_dict(device_dict, "IP6",
                       get_elementvalues(idmef_element, "Node/Address[@category='ipv6-addr']/address", tag_converted))
    save_value_to_dict(device_dict, "MAC",
                       get_elementvalues(idmef_element, "Node/Address[@category='mac']/address", tag_converted))
    save_value_to_dict(device_dict, "Email",
                       get_elementvalues(idmef_element, "Node/Address[@category='e-mail']/address", tag_converted))
    save_value_to_dict(device_dict, "IP4-hex",
                       get_elementvalues(idmef_element, "Node/Address[@category='ipv4-addr-hex']/address",
                                         tag_converted))
    save_value_to_dict(device_dict, "IP6-hex",
                       get_elementvalues(idmef_element, "Node/Address[@category='ipv6-addr-hex']/address",
                                         tag_converted))


def save_value_to_dict_safely(dictionary, key, value):
    """
    Special function for method convert_elementtree_to_dict

    :param dictionary: dictionary, where "value" wil be stored in "key"
    :param key: key in dictionary, where we want to save value
    :param value: value to be stored in dictionary
    """

    if value:
        if key in dictionary:
            if isinstance(dictionary[key], list):
                dictionary[key].append(value)
            else:
                value_list = [dictionary[key], value]
                dictionary[key] = value_list
        else:
            dictionary[key] = value


def convert_elementtree_to_dict(element, parent_dictionary):
    """
    Function, which does natural conversion from elementtree to dict (xml to json)

    :param element: input root element, which will be converted to dict
    :param parent_dictionary: dict, where
    :return: parent_dictionary with converted keys and values
    """
    for key, value in element.items():
        if "$converted$" not in key:
            save_value_to_dict_safely(parent_dictionary, "@" + key, value)
    if element.text and "$converted$" not in element.tag:
        if element.items() or get_element_children(element):
            save_value_to_dict_safely(parent_dictionary, "#text", remove_beginend_whitespaces(element.text))
            # parent_dictionary["value"] = element.text
        else:
            parent_dictionary = element.text
            # return parent_dictionary
    for child in get_element_children(element):
        dictionary = {}
        child_value = convert_elementtree_to_dict(child, dictionary)
        if child_value:
            if "$converted" in child.tag:
                save_value_to_dict_safely(parent_dictionary, child.tag[:-len("$converted$")], child_value)
            else:
                save_value_to_dict_safely(parent_dictionary, child.tag, child_value)
    return parent_dictionary


def get_element_children(element):
    """
    Get all children of element

    :param element: parent element
    :return: list of element children
    """
    return list(element)


class IdmefToIdeaMessageConverter(MessageConverter):
    """
    Class providing methods for converting just single "Alert" from IDMEF to IDEA
    """

    def __init__(self):
        """
        Init part containing initialization of input_message and output idea dictionary
        """

        self.input_message = None
        self.idea_dict = {}
        self.namespace = "{http://iana.org/idmef}"

    def modify_data(self, input_message=None):
        """
        Takes input elementtree with "IDMEF-Message" root and converts it into IDEA dictionary

        :param input_message: elementtree with "Alert" root, if None, takes input_message from class attributes
        :return list of dictionaries with alerts converted from IDMEF to IDEA (one dict, one alert of single message)
        """

        self.input_message = input_message
        tag_converted = True
        idea_dict = {}
        if input_message:
            save_value_to_dict(idea_dict, "Format", "IDEA0")
            save_value_to_dict(idea_dict, "ID", get_elementattribute(input_message, ".", "messageid", tag_converted, None))
            self.save_time(idea_dict, input_message, "CreateTime", "CreateTime")
            self.save_time(idea_dict, input_message, "DetectTime", "DetectTime")
            save_value_to_dict(idea_dict, "CorrelID",
                               get_elementvalues(input_message, "./CorrelationAlert/alertident", tag_converted))
            save_value_to_dict(idea_dict, "Ref",
                               get_elementvalues(input_message, "./Classification/Reference/url", tag_converted))
            save_value_to_dict(idea_dict, "Category", get_elementattributes(input_message,
                                                                            "./Classification", "text", tag_converted))
            self.save_confidence(input_message, idea_dict, tag_converted)
            save_value_to_dict(idea_dict, "Source", self.save_sources_into_idea(input_message))
            save_value_to_dict(idea_dict, "Target", self.save_targets_into_idea(input_message))

            node = self.save_analyzer_into_idea(input_message)
            if node:
                save_value_to_dict(idea_dict, "Node", [node])
            self.save_additionaldata_into_idea(input_message, idea_dict)
            self.add_rest_values(input_message, idea_dict)
        return idea_dict

    def save_confidence(self, alert, idea_dict, tag_converted):
        """
        Converts confidence from IDMEF alert to IDEA message

        :param alert: input IDMEF alert element
        :param idea_dict: dict, where converted IDEA is saved
        :param tag_converted: boolean, which says if confidence should be tag as converted
        """
        confidence_element = alert.find("Assessment/Confidence")
        if confidence_element is not None:
            rating_attr = confidence_element.get("rating", None)
            if rating_attr == "numeric":
                save_value_to_dict(idea_dict, "Confidence",
                                   get_elementvalue(confidence_element, ".", tag_converted))

    def save_time(self, idea_dict, parent_element, time_element_tag, idea_key):
        """
        Save specific time (CreateTime or DetectTime) to IDEA from IDMEF

        :param idea_dict: dict, where converted IDEA is saved
        :param parent_element: parent element of time element
        :param time_element_tag: tag of specific time element, in this case CreateTime or DetectTime
        :param idea_key: key, where converted time will be saved in dictionary
        """
        time_element = parent_element.find(time_element_tag)
        ntp_attribute = get_elementattribute(time_element, ".", "ntpstamp", tag_converted=True, default_value=None)
        if ntp_attribute is not None:
            save_value_to_dict(idea_dict, idea_key, ntp_attribute)
        else:
            save_value_to_dict(idea_dict, idea_key, get_elementvalue(time_element, ".", tag_converted=True))

    def save_sources_into_idea(self, alert):
        """
        Methods, which call save_devices with path to Source from Alert in elementtree

        :param alert: input IDMEF alert
        """

        return self.save_devices(".Source", alert, False)

    def save_targets_into_idea(self, alert):
        """
        Methods, which call save_devices with path to Target from Alert in elementtree

        :param alert: input IDMEF alert
        """

        return self.save_devices(".Target", alert, False)

    def get_port_from_idmef(self, device, tag_converted):
        """
        Get port or portlist from IDMEF

        :param device: specific IDMEF source or target element
        :param tag_converted: boolean, which says if port (portlist should be tag as converted
        :return: list of ports, which was retrieved from portlist or port element
        """
        ports = get_elementvalues(device, "Service/port", tag_converted)
        if not ports:
            portlist = get_elementvalue(device, "Service/portlist", tag_converted)
            if portlist:
                portlist_items = portlist.split(",")
                for portlist_item in portlist_items:
                    portlist_item = portlist_item.replace(" ", "")
                    if "-" in portlist_item:
                        range_borders = portlist_item.split("-")
                        # here if range borders has count not 2, throw an exception
                        port_inside_range = int(range_borders[0])
                        up_border = int(range_borders[1])
                        while port_inside_range <= up_border:
                            ports.append(port_inside_range)
                            port_inside_range += 1
                    else:
                        ports.append(int(portlist_item))
        else:
            ports = [int(port) for port in ports]
        return ports

    def save_devices(self, path_to_device, alert, tag_converted):
        """
        Save all Sources or Targets (depends on path to device) from IDMEF elementtree to IDEA dictionary

        :param path_to_device: relative path from Alert to Source or Target in IDMEF
        :param alert: input IDMEF alert
        :param tag_converted: boolean, which says if confidence should be tag as converted
        """
        xml_devices = alert.findall(path_to_device)
        device_list = []
        for item in xml_devices:
            device_dict = {}
            save_value_to_dict(device_dict, "Hostname", get_elementvalues(item, "Node/name", tag_converted))
            save_value_to_dict(device_dict, "Port", self.get_port_from_idmef(item, tag_converted))
            save_value_to_dict(device_dict, "Proto", get_elementvalues(item, "Service/protocol", tag_converted))
            save_value_to_dict(device_dict, "Url", get_elementvalues(item, "Service/URL", tag_converted))
            save_value_to_dict(device_dict, "Router", get_elementattributes(item, ".", "interface", tag_converted))
            spoofed_string = "decoy"
            if "Source" in path_to_device:
                spoofed_string = "spoofed"
            save_value_to_dict(device_dict, "Spoofed", get_elementattribute(item, ".", spoofed_string, tag_converted,
                                                                            default_value=None))
            save_addresses(item, device_dict, tag_converted)
            device_list.append(device_dict)
        return device_list

    def get_sw_attribute(self, alert, attribute_name, last_char=""):
        """
        Retrieves specific attribute of Analyzer for Node.SW attribute in IDEA

        :param alert: parent alert element of analyzer
        :param attribute_name: key to specific attribute
        :param last_char: says what char should in sw string go after this specific analyzer attribute
        :return: retrieved analyzer attribute + last_char as a string
        """
        attribute_value = get_elementattribute(alert, "Analyzer", attribute_name, tag_converted=True, default_value="")
        if attribute_value is not "":
            return attribute_value + last_char
        return ""

    def save_analyzer_into_idea(self, alert):
        """
        Converts Analyzer element from IDMEF to IDEA "Node" object

        :param alert: parent alert of analyzer
        :return: Converted Node as a dictionary
        """
        node_value = {}
        save_value_to_dict(node_value, "Name", get_elementattribute(alert, "Analyzer", "name", tag_converted=True,
                                                                    default_value=None))
        save_value_to_dict(node_value, "SW", self.get_sw_attribute(alert, "model", " ")
                           + self.get_sw_attribute(alert, "version", " ")
                           + self.get_sw_attribute(alert, "class", " ")
                           + self.get_sw_attribute(alert, "ostype", " ")
                           + self.get_sw_attribute(alert, "osversion"))
        return node_value

    def save_additionaldata_into_idea(self, alert, idea_dict):
        """
        Converts IDMEF AdditionalData into IDEA Attach

        :param alert: input IDMEF alert
        :param idea_dict: output dictionary with converted IDEA
        """
        additional_data_list = alert.findall("AdditionalData")
        if not idea_dict.get("Attach", None):
            idea_dict["Attach"] = []
        for additional_data_item in additional_data_list:
            converted_additional_data = convert_elementtree_to_dict(additional_data_item, {})
            if converted_additional_data:
                attach_item = {"Content": str(converted_additional_data)} # json.dumps(converted_additional_data)
                idea_dict["Attach"].append(attach_item)
                tag_element_converted(additional_data_item)
        if not idea_dict["Attach"]:
            idea_dict.pop("Attach", None)

    def add_rest_values(self, alert, idea_dict):
        """
        Creates one more Attach object with data, which could not be converted from IDMEF to IDEA.
        Into "Content" key is saved result of convert_elementtree_to_dict, what naturally converted alert element to
        dictionary.

        :param alert: input IDMEF alert
        :param idea_dict: output dictionary with converted IDEA
        """
        converted = convert_elementtree_to_dict(alert, {})
        if converted:
            attachement_dict = {"Note": "Data which could not be converted from IDMEF properly and whole "
                                        "Attach, Source and Target converted naturally from IDMEF",
                                "Content": str(convert_elementtree_to_dict(alert, {}))}
            if not idea_dict.get("Attach", None):
                idea_dict["Attach"] = []
            idea_dict["Attach"].append(attachement_dict)
            if not idea_dict["Attach"]:
                idea_dict.pop("Attach", None)
