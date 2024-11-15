import unittest
from main import parse_xml_to_config


class TestParseXmlToConfig(unittest.TestCase):

    def test_simple_dictionary(self):
        xml_input = """
        <config>
            <name>test_config</name>
            <version>1</version>
        </config>
        """
        expected_output = """{
    name = "test_config";
    version = 1;
}"""
        self.assertEqual(parse_xml_to_config(xml_input.strip()), expected_output)

    def test_nested_dictionary(self):
        xml_input = """
        <database>
            <name>test_db</name>
            <credentials>
                <user>admin</user>
                <password>12345</password>
            </credentials>
        </database>
        """
        expected_output = """{
    name = "test_db";
    credentials = 
    {
        user = "admin";
        password = 12345;
    }
}"""
        self.assertEqual(parse_xml_to_config(xml_input.strip()), expected_output)

    def test_single_line_comment(self):
        xml_input = """
        <comment>Это однострочный комментарий</comment>
        """
        expected_output = "# Это однострочный комментарий\n"
        self.assertEqual(parse_xml_to_config(xml_input.strip()), expected_output)

    def test_multi_line_comment(self):
        xml_input = """
        <comment multiline="true">Это многострочный
        комментарий</comment>
        """
        expected_output = """(*
Это многострочный
комментарий
*)
"""
        self.assertEqual(parse_xml_to_config(xml_input.strip()), expected_output)

    def test_numeric_values(self):
        xml_input = """
        <settings>
            <max_connections>100</max_connections>
            <timeout>30</timeout>
        </settings>
        """
        expected_output = """{
    max_connections = 100;
    timeout = 30;
}"""
        self.assertEqual(parse_xml_to_config(xml_input.strip()), expected_output)

    def test_mixed_content(self):
        xml_input = """
        <application>
            <title>MyApp</title>
            <version>2</version>
            <author>dev_user</author>
            <features>
                <feature1>Feature A</feature1>
                <feature2>Feature B</feature2>
            </features>
        </application>
        """
        expected_output = """{
    title = "MyApp";
    version = 2;
    author = "dev_user";
    features = 
    {
        feature1 = "Feature A";
        feature2 = "Feature B";
    }
}"""
        self.assertEqual(parse_xml_to_config(xml_input.strip()), expected_output)

    def test_invalid_tag_name(self):
        xml_input = "<invalid<tag>"
        with self.assertRaises(SyntaxError) as context:
            parse_xml_to_config(xml_input)
        self.assertTrue("Недопустимое имя тега" in str(context.exception))


if __name__ == "__main__":
    unittest.main()
