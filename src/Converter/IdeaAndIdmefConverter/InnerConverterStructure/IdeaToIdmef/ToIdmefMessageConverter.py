from xml.etree.ElementTree import Element, SubElement, register_namespace

from IdeaAndIdmefConverter.InnerConverterStructure.MessageConverter import MessageConverter

IDMEF_NAMESPACE_TAG = "{http://iana.org/idmef}"
IDMEF_NAMESPACE_ATTRIBUTE = "http://iana.org/idmef"


def get_unconverted_values(idea_dict):
    """
    Actually unused, older version of convert_dict_to_elementtree method
    """
    filtered_dict = {}
    for key, value in idea_dict.items():
        if "$converted$" not in key:
            if isinstance(value, dict):
                filtered_dict[key] = get_unconverted_values(value)
            elif isinstance(value, list):
                filtered_dict[key] = []
                for value_item in value:
                    if isinstance(value_item, dict):
                        filtered_dict[key].append(get_unconverted_values(value_item))
                    elif not isinstance(value_item, list):
                        filtered_dict[key].append(value_item)
            else:
                filtered_dict[key] = value
    return filtered_dict


def convert_dict_to_elementtree(dict_for_conversion, parent_element):
    """
    Takes input dictionary  and converts it to elementtree with all children and fields (like json to xml)

    :param dict_for_conversion: input dictionary which will be converted
    :param parent_element: element, which will be root element to converted elementtree
    """
    for key, value in dict_for_conversion.items():
        if "$converted$" not in key:
            if isinstance(value, dict):
                element = SubElement(parent_element, key)
                convert_dict_to_elementtree(value, element)
                if not element.text and not element.items() and not list(element):
                    parent_element.remove(element)
            elif isinstance(value, list):
                for value_item in value:
                    element = SubElement(parent_element, key)
                    if isinstance(value_item, dict):
                        convert_dict_to_elementtree(value_item, element)
                    elif not isinstance(value_item, list):
                        element.text = str(value_item)
            else:
                if key[0] == "@":
                    parent_element.set(key[1:], str(value))
                elif key == "#text":
                    parent_element.text = str(value)
                else:
                    element = SubElement(parent_element, key)
                    element.text = str(value)


def save_attributes_into_element(element, attributes={}):
    """
    Save attribute into element in elementtree using element.set method

    :param element: xml node, where will be attributes assigned to
    :param attributes: dictionary with name af attribute and values
    """
    for key, value in attributes.items():
        if value is not None:
            element.set(key, str(value))


def tag_converted(dictionary, key):
    """
    Takes key from dictionary and concats label $converted$ to this key

    :param dictionary: dict, where key is located
    :param key: key which will be marked as $converted$
    """
    if dictionary:
        value = dictionary.pop(key, None)
        if value:
            dictionary[key + "$converted$"] = value


def get_from_dict(dictionary, key, default_value):
    """
    Gets value from dict, if it does not exist, returns default_value

    :param dictionary: dict, which we want to retrieve value of key from
    :param key: key, which value we are looking for
    :param default_value: if key does not exists in dictionary, this value is returned
    :return: dict[key], or default_value
    """
    if dictionary:
        return dictionary.get(key, default_value)
    return default_value


class IdeaToIdmefMessageConverter(MessageConverter):
    """
    Class providing methods for converting just single IDEA message to IDMEF
    """

    def __init__(self):
        """
        Init part containing initialization of input_message and output idmef tree represented by root
        """

        self.input_message = None
        self.root = None
        self.cached_classifications = []
        self.cached_hostnames = []
        self.idmef_namespace = False

    def modify_data(self, input_message=None, idmef_namespace=False, convert_unconvertable=False):
        """
        Takes input IDEA dictionary and converts it into elementtree with IDMEF

        :param convert_unconvertable: boolean, if unconvertable values has to be converted, true, otherwise false
        :param input_message: dictionary with IDEA message, if None, takes input_message from class attributes
        :param idmef_namespace: boolean, if true, idmef namespace, as is mentioned in rfc4765 will be included in whole
                                message and added before every tag of output message
        :return pair of root of elementtree (converted from dict with IDEA) and fields, which were converted naturally
                from dict to elementtree and could not be converted properly to IDMEF
        """

        self.idmef_namespace = idmef_namespace
        if input_message:
            self.input_message = input_message
        else:
            return self.create_root(), None
        self.root = self.create_root()
        alert = self.save_alert()
        self.save_analyzer(alert)
        self.save_createtime(alert)
        self.save_detecttime(alert)
        self.save_sources(alert)
        self.save_targets(alert)
        self.save_classification(alert)
        self.save_assessment(alert)
        self.save_correlationalert(alert)
        self.add_additional_data(alert)
        unconvertable_root = None
        if convert_unconvertable:
            unconvertable_root = self.convert_unconverted_values()
        return self.root, unconvertable_root

    def create_root(self):
        """
        Create "IDMEF-Message" root with attributes and with namespace if needed

        :return: root element
        """
        root_attributes = {"version": "1.0"}
        namespace = ""
        if self.idmef_namespace:
            register_namespace("idmef", IDMEF_NAMESPACE_ATTRIBUTE)
            namespace = IDMEF_NAMESPACE_TAG
            root_attributes["xmlns:idmef"] = IDMEF_NAMESPACE_ATTRIBUTE
        root = Element(namespace + "IDMEF-Message")
        save_attributes_into_element(root, {"version": "1.0"})
        return root

    def create_subelement(self, element, subelement_name, subelement_value=None, subelement_attributes={},
                          required_value=False):
        """
        Creates subelemement in XML elementtree

        :param element: element, which children will be created
        :param subelement_name: tag name of new element
        :param subelement_value: optional, value of new element
        :param subelement_attributes: optional, attribute dictionary of new element
        :param required_value: says, if element must contain subelement_value;
                                if yes and value is not provided, subelement is not created
        :return: created subelement
        """

        namespace = ""
        if self.idmef_namespace:
            namespace = IDMEF_NAMESPACE_TAG
        if required_value and not subelement_value:
            return None
        child = SubElement(element, namespace + subelement_name)
        # child = SubElement(element, subelement_name)
        if subelement_value is not None:
            child.text = str(subelement_value)
        save_attributes_into_element(child, subelement_attributes)
        return child

    def save_alert(self):
        """
        Creates alert and saves it into elementtree

        :return: created "Alert" element
        """

        alert = self.create_subelement(self.root, "Alert")
        save_attributes_into_element(alert, {"messageid": get_from_dict(self.input_message, "ID", None)})
        tag_converted(self.input_message, "ID")
        return alert

    def save_analyzer(self, alert):
        idea_nodes = self.input_message.get("Node", None)
        analyzer = self.create_subelement(alert, "Analyzer")
        if idea_nodes:
            first_node = idea_nodes[0]
            save_attributes_into_element(analyzer, {"name": get_from_dict(first_node, "Name", None)})
            tag_converted(first_node, "Name")

    def save_createtime(self, alert):
        """
        Creates "CreateTime" subelement of alert and saves it into elementtree

        :param alert: parent of "CreateTime"
        :return: created "CreateTime" element or None, if createtime does not exists in IDEA
        """
        datetimestamp = get_from_dict(self.input_message, "CreateTime", None)
        tag_converted(self.input_message, "CreateTime")
        if datetimestamp:
            if isinstance(datetimestamp, tuple):
                return self.create_subelement(alert, "CreateTime", datetimestamp[0],
                                              {"ntpstamp": datetimestamp[1]})
            else:
                return self.create_subelement(alert, "CreateTime", datetimestamp, {"ntpstamp": datetimestamp})
        return None

    def save_detecttime(self, alert):
        """
        Creates "DetectTime" subelement of alert and saves it into elementtree

        :param alert: parent of "DetectTime"
        :return: created "DetectTime" element
        """
        datetimestamp = get_from_dict(self.input_message, "DetectTime", None)
        tag_converted(self.input_message, "DetectTime")
        if datetimestamp:
            if isinstance(datetimestamp, tuple):
                return self.create_subelement(alert, "DetectTime", datetimestamp[0],
                                              {"ntpstamp": datetimestamp[1]})
            else:
                return self.create_subelement(alert, "DetectTime", datetimestamp, {"ntpstamp": datetimestamp})
        return None

    def save_correlationalert(self, alert):
        """
        Creates "CorrelationAlert" subelement of alert and saves it into elementtree

        :param alert: parent of "CorrelationAlert"
        :return: created "CorrelationAlert" element, or None, if it would be empty
        """
        correlids = get_from_dict(self.input_message, "CorrelID", [])
        if correlids:
            corellation_alert = self.create_subelement(alert, "CorrelationAlert")
            self.create_subelement(corellation_alert, "name")  # problem with required name
            tag_converted(self.input_message, "CorrelID")
            for correlid in correlids:
                self.create_subelement(corellation_alert, "alertident", required_value=True, subelement_value=correlid)
            return corellation_alert
        return None

    def extract_list_item(self, dictionary, key, index):
        """
        Extract list item at specific index (return this value and remove it from list)

        :param dictionary: dict, where list is located
        :param key: key in dict, where list is located
        :param index: order of item in list
        :return: extracted value
        """
        extracting_list = dictionary.get(key, None)  # change to get
        extracted_value = None
        if extracting_list:
            extracted_value = extracting_list.pop(index)

        # here cannot be else, because in clause before this, one value from list is extracted
        if not extracting_list:
            tag_converted(dictionary, key)
        return extracted_value

    def save_classification(self, alert):
        """
        Creates "Classification" subelement of alert and saves it into elementtree

        :param alert: parent of "Classification"
        :return: created "Classification" element
        """
        classification = self.create_subelement(alert, "Classification")
        save_attributes_into_element(classification, {
            "text": self.extract_list_item(self.input_message, "Category",
                                           0)})  # problem with list of categories from IDEA
        self.save_ref(classification)
        return classification

    def save_ref(self, classification):
        """
        Takes Ref key from IDEA and converts it to reference

        :param classification: parent classification element, where Reference element will be located
        """
        uris = get_from_dict(self.input_message, "Ref", [])  # solve difference between uri and url
        tag_converted(self.input_message, "Ref")
        for uri in uris:
            classification_reference = self.create_subelement(classification, "Reference", None,
                                                              {"origin": "unknown"})
            self.create_subelement(classification_reference, "name")
            self.create_subelement(classification_reference, "url", uri)  # solve problem with url, uri etc

    def save_assessment(self, alert):
        """
        Creates "Assessment" subelement of alert and saves it into elementtree

        In this method is also set Confidence to elementtree as a subelement of Assessment

        :param alert: parent of "Assessment"
        :return: created "Assessment" element
        """
        idea_confidence = get_from_dict(self.input_message, "Confidence", None)
        assessment = None
        if idea_confidence:
            assessment = self.create_subelement(alert, "Assessment")
            self.create_subelement(assessment, "Confidence", idea_confidence,
                                   {"rating": "numeric"}, required_value=True)
            tag_converted(self.input_message, "Confidence")
        return assessment

    def save_all_adresses(self, node, idea_device):
        """
        Saves addresses from specific IDEA fields to node in Source or Target

        :param node: Node tag, which is child of Source or Target tag
        :param idea_device: IDEA "Source" or "Target" dictionary, from which are data saved to node
        """
        self.save_address_to_idmef(node, "ipv4-addr", get_from_dict(idea_device, "IP4", None))
        self.save_address_to_idmef(node, "ipv6-addr", get_from_dict(idea_device, "IP6", None))
        self.save_address_to_idmef(node, "mac", get_from_dict(idea_device, "MAC", None))
        self.save_address_to_idmef(node, "e-mail", get_from_dict(idea_device, "Email", None))

    def save_address_to_idmef(self, node_element, address_category, value_list):
        """
        Save just one specific address to IDMEF tree

        :param node_element: node parent of address
        :param address_category: category, which will be stored into attribute of Address tag (for example MAC, IP4...)
        :param value_list: values taken from IDEA of this address category
        """
        if value_list:
            for value in value_list:
                address_element = self.create_subelement(node_element, "Address")
                save_attributes_into_element(address_element, {"category": address_category})
                self.create_subelement(address_element, "address", value)

    def save_sources(self, alert):
        """
        Creates "Source" subelement of alert and saves it into elementtree

        :param alert: parent of "Source"
        :return: created "Source" element
        """

        idea_sources = self.input_message.get("Source", [])
        for idea_source in idea_sources:
            source = self.create_subelement(alert, "Source")
            save_attributes_into_element(source, {
                "spoofed": get_from_dict(idea_source, "Spoofed", None),
                "interface": self.extract_list_item(idea_source, "Router", 0)})
            self.save_devices_subtrees(source, idea_source)

    def save_targets(self, alert):
        """
        Creates "Target" subelement of alert and saves it into elementtree

        :param alert: parent of "Target"
        """

        idea_targets = self.input_message.get("Target", [])
        for idea_target in idea_targets:
            target = self.create_subelement(alert, "Target")
            save_attributes_into_element(target, {
                "decoy": get_from_dict(idea_target, "Spoofed", None),
                "interface": self.extract_list_item(idea_target, "Router", 0)})
            self.save_devices_subtrees(target, idea_target)

    def save_protocol(self, service, idea_device):
        """
        Converts protocol of source or target from IDEA to IDMEF

        :param service: parent element of protocol in IDMEF
        :param idea_device: particular source or target dict object, where input protocol key is located
        """
        self.create_subelement(service, "protocol", self.extract_list_item(idea_device, "Proto", -1),
                               required_value=True)

    def save_port(self, service, idea_device):
        """
        Converts port of source or target from IDEA to IDMEF

        :param service: parent element of protocol in IDMEF
        :param idea_device: particular source or target dict object, where input protocol key is located
        """
        idea_ports = get_from_dict(idea_device, "Port", [])
        if idea_ports:
            portlist = self.create_subelement(service, "portlist", subelement_value="")
            for idea_port in idea_ports:
                portlist.text += str(idea_port) + ", "
            portlist.text = portlist.text.rstrip(", ")

    def save_service(self, element_device, idea_device):
        """
        Save service with protocols and ports

        :param element_device: parent source or target element
        :param idea_device: particular source or target dict object
        """
        service = self.create_subelement(element_device, "Service")
        self.save_port(service, idea_device)
        self.save_protocol(service, idea_device)
        if not list(service):
            element_device.remove(service)

    def save_hostname(self, node, idea_device):
        """
        Saves hostname from IDEA source or target to elementtree under Source/Node, or Target/Node

        :param node: parent element Node
        :param idea_device: input source or target dict object, where hostname key is located
        :return:
        """
        self.create_subelement(node, "name", self.extract_list_item(idea_device, "Hostname", 0), required_value=True)

    def save_devices_subtrees(self, device, idea_device):
        """
        Save subtrees of "Source" or "Target", which definition is common for both element definition in XML

        :param device: IDMEF "Source" or "Target" parent element
        :param idea_device: IDEA "Source" or "Target", which values will be converted from
        """

        node = self.create_subelement(device, "Node")
        self.save_hostname(node, idea_device)
        self.save_all_adresses(node, idea_device)
        self.save_service(device, idea_device)

    def add_additional_data(self, alert):
        """
        Saves attachments from IDEA to IDMEF AdditionalData element

        :param alert: parent idmef alert
        """
        attachments = self.input_message.get("Attach", [])
        for attachment in attachments:
            additional_data = self.create_subelement(alert, "AdditionalData")
            self.create_subelement(additional_data, "string",
                                                    str(get_from_dict(attachment, "Content", None)))

    def convert_unconverted_values(self):
        """
        Converts all keys from IDEA, which could not be converted to this point

        :return: Root element with tag UnconvertedFromIDEA, under which are all rest elements converted from IDEA dict
                 to elementtree
        """
        unconverted_element = Element("UnconvertableFromIDEAMessage")
        convert_dict_to_elementtree(self.input_message, unconverted_element)
        return unconverted_element
