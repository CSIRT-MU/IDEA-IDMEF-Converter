import time

import dateutil.parser

from IdeaAndIdmefConverter.InnerConverterStructure.ValuesConverter import ValuesConverter

NTP_TO_EPOCH_DELTA = 2208988800 + 3600
HEX_DATETIME_STRING_MIDDLE = 11


class IdeaToIdmefValueConverter(ValuesConverter):
    """
    Class which converts specific data types of values in IDEA dict to IDMEF data types
    """

    def convert_values(self, idea_dictionary):
        """
        Method, which converts all values, which has to be converted from IDEA to IDMEF (converts only values,
        not fields or data structures)

        :param idea_dictionary: input dict with parsed IDEA keys and values
        :return: dict with converted values
        """
        if "Confidence" in idea_dictionary:
            idea_dictionary["Confidence"] = str(idea_dictionary["Confidence"])
        self.convert_spoofed(idea_dictionary, "Source")
        self.convert_spoofed(idea_dictionary, "Target")
        self.convert_time(idea_dictionary, "DetectTime")
        self.convert_time(idea_dictionary, "CreateTime")
        return idea_dictionary

    def convert_spoofed(self, dictionary, device_key):
        """
        Takes key Spoofed from specific source or target and converts it from boolean to "yes", "no", "unknown"

        :param dictionary: input dict
        :param device_key: key of field "Source" or "Target"
        """
        devices = dictionary.get(device_key, [])
        for device in devices:
            spoofed_value = device.get("Spoofed", None)
            if spoofed_value:
                device["Spoofed"] = "yes"
            elif spoofed_value is None:
                device["Spoofed"] = "unknown"
            else:
                device["Spoofed"] = "no"

    def convert_time(self, dictionary, time_key):
        """
        Takes specific time field and converts it from timestamp to ntp hexadecimal type

        :param dictionary: input dict
        :param time_key: specific time key ("CreateTime" or "DetectTime")
        """
        time = dictionary.get(time_key, None)
        if time:
            dictionary[time_key] = (time, self.convert_datetime_to_ntphex(time))

    def convert_datetime_to_ntphex(self, datetime_stamp):
        """
        Converts timestamp to ntp hexadecimal type

        :param datetime_stamp: input timestamp value
        :return: ntp hexadecimal type (in form 0x.......0x........)
        """
        if isinstance(datetime_stamp, str):
            date_struct = dateutil.parser.parse(datetime_stamp)
            high = int(time.mktime(date_struct.timetuple())) + NTP_TO_EPOCH_DELTA
            low = date_struct.microsecond
            number = low + (high << 32)
            hex_number = hex(number)
            return "{0}.0x{1}".format(hex_number[0:(HEX_DATETIME_STRING_MIDDLE - 1)],
                                      hex_number[(HEX_DATETIME_STRING_MIDDLE - 1):])
        return None
