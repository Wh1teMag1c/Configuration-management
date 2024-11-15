import xml.etree.ElementTree as ET
import re
import sys


def parse_xml_to_config(xml_input):
    try:
        # Парсим XML из входной строки
        root = ET.fromstring(xml_input)
        return convert_element_to_config(root)
    except ET.ParseError as e:
        # Создаем новое исключение с сообщением, которое мы хотим
        raise SyntaxError("Ошибка синтаксиса XML: Недопустимое имя тега") from e


def convert_element_to_config(element, indent=0):
    """
    Рекурсивно конвертирует элемент XML в конфигурационный язык.
    """
    config_output = ""
    indent_str = "    " * indent  # 4 пробела для каждого уровня вложенности

    # Проверка на комментарии
    if element.tag.lower() == "comment":
        if "multiline" in element.attrib and element.attrib["multiline"] == "true":
            lines = element.text.strip().split('\n')
            comment_body = "\n".join([indent_str + line.strip() for line in lines])
            config_output += f"{indent_str}(*\n{comment_body}\n{indent_str}*)\n"
        else:
            config_output += f"{indent_str}# {element.text.strip()}\n"
        return config_output

    # Конвертация элемента в словарь
    config_output += f"{indent_str}{{\n"
    for child in element:
        if re.match(r"[_a-zA-Z]+", child.tag):
            if child.tag.lower() != "comment":
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
    """
    Определяет значение для элемента.
    """
    # Если у элемента есть дочерние элементы, то это вложенный словарь
    if len(element):
        return f"\n{convert_element_to_config(element, indent=1)}"

    # Если значение - это число
    if element.text and element.text.strip().isdigit():
        return element.text.strip()

    # Обработка текстовых значений
    if element.text and element.text.strip():
        # Возвращаем строку в кавычках
        return f'"{element.text.strip()}"'

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
