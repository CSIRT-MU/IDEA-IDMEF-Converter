import os
import unittest
import xml.etree.ElementTree as ElTree

from IdeaAndIdmefConverter.InnerConverterStructure.IdeaToIdmef.IdmefExporter import IdmefExporter


def get_test_idmef_message():
    return """
    <IDMEF-Message version="1.0">
    <Alert messageid="123d45">
        <Analyzer analyzerid="5468">
        </Analyzer>
        <CreateTime ntpstamp="0xbc723b45.0xef449129">2
            000-03-09T10:01:25.93464-05:00
        </CreateTime>
        <Classification ident="1" text="Phishing">
            <Reference meaning="meaning of reference" origin="vendor-specific">
                <name>Name of alert</name>
                <url>ref.example.com</url>
            </Reference>
        </Classification>
        <Source ident="2">
            <Service>
                <name>
                    ServiceName
                </name>
                <port>
                    154
                </port>
            </Service>
        </Source>
        <Source>
            <Node>
                <Address category="e-mail">
                    <address>
                        example@example.com
                    </address>
                </Address>
            </Node>
        </Source>
    </Alert>
</IDMEF-Message>
    """


def get_test_elementtree():
    return ElTree.fromstring(get_test_idmef_message())


class IdmefExporterTest(unittest.TestCase):
    def test_file_export(self):
        with open("OutputTestData/idmef_test.xml", "w") as output_file:
            idmef_exporter = IdmefExporter(output_file)
            idmef_exporter.export_message([get_test_elementtree()])

        with open("OutputTestData/idmef_test.xml", "r") as input_file:
            expected_value = ElTree.tostring(ElTree.fromstring(get_test_idmef_message()),
                                             encoding="unicode") + os.linesep
            if os.name == "nt":
                expected_value = ElTree.tostring(ElTree.fromstring(get_test_idmef_message()),
                                             encoding="unicode") + "\n\n"
            self.assertEqual(input_file.read(), expected_value, "IDMEF export to file is not correct")

    def test_string_export(self):
        idmef_exporter = IdmefExporter()
        export_tuple = idmef_exporter.export_message_tostring([get_test_elementtree()])
        self.assertEqual(export_tuple[0], ElTree.tostring(ElTree.fromstring(get_test_idmef_message()),
                                                          encoding="unicode"),
                         "IDMEF export to string is not correct")


if __name__ == '__main__':
    unittest.main()
