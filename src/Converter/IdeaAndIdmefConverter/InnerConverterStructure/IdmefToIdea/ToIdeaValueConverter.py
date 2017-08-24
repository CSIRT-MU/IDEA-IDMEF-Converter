import ipaddress
import socket
import struct
from datetime import datetime

from IdeaAndIdmefConverter.InnerConverterStructure.ValuesConverter import ValuesConverter

NTP_TO_EPOCH_DELTA = 2208988800 + 3600


class IdmefToIdeaValueConverter(ValuesConverter):
    """
    Class which converts data types from IDMEF to IDEA. Data structure used is dict with already converted IDEA message
    (but unconverted values, what is responsibility of this class).
    """

    def convert_values(self, input_values):
        """
        Method, which converts all values, which has to be converted from IDMEF to IDEA (converts only values,
        not fields or data structures)

        :param input_values: input dictionary with parsed IDEA keys and values
        :return: list of input dictionaries with converted values
        """
        if input_values:
            if "Confidence" in input_values:
                input_values["Confidence"] = float(input_values["Confidence"])
            self.convert_spoofed(input_values, "Source")
            self.convert_spoofed(input_values, "Target")
            self.convert_time(input_values, "DetectTime")
            self.convert_time(input_values, "CreateTime")
            self.convert_hex_ip_addresses(input_values, "Source", "IP4", "IP4-hex")
            self.convert_hex_ip_addresses(input_values, "Source", "IP6", "IP6-hex")
            self.convert_hex_ip_addresses(input_values, "Target", "IP4", "IP4-hex")
            self.convert_hex_ip_addresses(input_values, "Target", "IP6", "IP6-hex")
        return input_values

    def convert_spoofed(self, dictionary, device_key):
        """
        Takes key Spoofed from specific source or target and converts it from "yes", "no", "unknown" to boolean

        :param dictionary: input dict with message
        :param device_key: key of field "Source" or "Target"
        """
        devices = dictionary.get(device_key, [])
        for device in devices:
            spoofed_key = device.get("Spoofed", None)
            if spoofed_key == "yes":
                device["Spoofed"] = True
            elif spoofed_key == "no":
                device["Spoofed"] = False
            else:
                device.pop("Spoofed", None)

    def convert_hex_ip_addresses(self, dictionary, device_key, ip_key, temp_hexip_key):
        """
        Takes IPv4 or IPv6 in hexadecimal format (from IDMEF) and converts it to standard dotted format

        :param dictionary: input dict with message
        :param device_key: "Source" or "Target"
        :param ip_key: key of ip address ("IP4" or "IP6")
        :param temp_hexip_key: key to temporary field in IDEA for storing hexadecimal address, until they are converted
                                to normal and appended to keys "IP4" or "IP6".
                                This keys have value either "IP4-hex" or "IP6-hex" and after this method is done, this
                                key will not exist in IDEA dictionary
        """
        devices = dictionary.get(device_key, [])
        for device in devices:
            hex_addresses = device.pop(temp_hexip_key, [])
            addresses = device.get(ip_key, None)
            if not addresses:
                device[ip_key] = []
            for hex_address in hex_addresses:
                device[ip_key].append(self.decode_hex_ip(hex_address, ip_key))
            if not device[ip_key]:
                device.pop(ip_key, None)

    def convert_time(self, dictionary, time_key):
        """
        Takes specific time field and converts it from ntp hexadecimal type to timestamp

        :param dictionary: input dict
        :param time_key: specific time key ("CreateTime" or "DetectTime")
        """
        time = dictionary.get(time_key, None)
        if time:
            dictionary[time_key] = self.convert_ntphex_to_datetime(time)

    def convert_ntphex_to_datetime(self, ntphex_stamp):
        """
        Converts ntp hexadecimal value to timestamp

        :param ntphex_stamp: input timestamp value
        :return: string value formatted to standard timestamp
        """
        single_hextimestamp = ntphex_stamp.replace("0x", "")
        hextimestamps = single_hextimestamp.split(".")
        seconds_timestamp = int(hextimestamps[0], 16) - NTP_TO_EPOCH_DELTA
        microseconds_timestamp = int(hextimestamps[1], 16)
        return str(datetime.fromtimestamp((seconds_timestamp + microseconds_timestamp/1e6)))

    def decode_hex_ip(self, hex_addr, address_type):
        """
        Converts hex_addr from hexadecimal form to standard string dotted form"

        :param hex_addr: ip address in hexadecimal form
        :param address_type: "IP4" or "IP6"
        :return: standard string dotted form of particular IP address
        """
        if address_type == "IP4":
            return socket.inet_ntoa(struct.pack(">L", int(hex_addr, 16)))
        if address_type == "IP6":
            return str(ipaddress.ip_address(int(hex_addr, 16)))
