import re
import sys
import xml.etree.ElementTree as ET

constants = {}


def parse_xml_to_config(xml_input):
    try:
        root = ET.fromstring(xml_input)
        config_output = extract_constants(root)
        config_output += convert_element_to_config(root)
        return config_output
    except ET.ParseError as e:
        raise SyntaxError("Ошибка синтаксиса XML: Недопустимое имя тега") from e


def extract_constants(element):
    output = ""
    if element.tag.lower() == "constants":
        for child in element:
            if re.match(r"[_a-zA-Z]+", child.tag):
                if child.text and child.text.strip():
                    value = child.text.strip()
                    constants[child.tag] = value
                    output += f"{value} -> {child.tag};\n"
    elif element.tag.lower() == "constant":
        name = element.attrib.get("name")
        value = element.text.strip() if element.text else ""
        if not name or not value:
            raise SyntaxError("Тег <constant> должен содержать атрибут 'name' и текстовое значение")
        constants[name] = value
        output += f"{value} -> {name};\n"
    else:
        for child in element:
            output += extract_constants(child)
    return output


def convert_element_to_config(element, indent=0):
    config_output = ""
    indent_str = "    " * indent

    if element.tag.lower() in ["constants", "constant"]:
        return ""

    if element.tag.lower() == "comment":
        if "multiline" in element.attrib and element.attrib["multiline"] == "true":
            lines = element.text.strip().split('\n')
            comment_body = "\n".join([indent_str + line.strip() for line in lines])
            config_output += f"{indent_str}(*\n{comment_body}\n{indent_str}*)\n"
        else:
            config_output += f"{indent_str}# {element.text.strip()}\n"
        return config_output

    config_output += f"{indent_str}{{\n"
    for child in element:
        if re.match(r"[_a-zA-Z]+", child.tag):
            if child.tag.lower() not in ["constants", "constant", "comment"]:
                child_output = f"{indent_str}    {child.tag} = {parse_value(child)}"
                if not len(child):
                    child_output += ";"
                config_output += child_output + "\n"
            else:
                config_output += convert_element_to_config(child, indent + 1)
        else:
            raise SyntaxError(f"Недопустимое имя тега: {child.tag}")

    config_output += f"{indent_str}}}"
    return config_output


def parse_value(element):
    if len(element):
        return f"\n{convert_element_to_config(element, indent=1)}"

    if element.text and element.text.strip().isdigit():
        return element.text.strip()

    if element.text and element.text.strip():
        value = element.text.strip()
        if re.match(r"^\|[_a-zA-Z]+\|$", value):
            const_name = value.strip('|')
            if const_name in constants:
                return constants[const_name]
            else:
                raise SyntaxError(f"Константа '{const_name}' не определена")
        return f'"{value}"'

    raise SyntaxError(f"Не удалось определить значение для элемента {element.tag}")


if __name__ == "__main__":
    filename = sys.argv[1]

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            xml_input = file.read()
        config_output = parse_xml_to_config(xml_input.strip())
        print("\nРезультат:")
        print(config_output)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден.")
    except SyntaxError as e:
        print(f"Ошибка: {e}")
