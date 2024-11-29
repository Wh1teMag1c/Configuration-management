import json
import struct
import sys

# Определяем коды операций для команд УВМ
COMMANDS = {
    'LOAD_CONSTANT': 7,
    'READ_MEMORY': 23,
    'WRITE_MEMORY': 24,
    'POPCNT': 17
}


def parse_instruction(line):
    """
    Разбирает инструкцию из строки исходного кода, удаляет комментарии и возвращает команду и аргументы.
    """
    line = line.split('#', 1)[0].strip()
    if not line:
        return None, None

    parts = line.split()
    command = parts[0]
    args = [int(part) for part in parts[1:]]

    return command, args


def encode_instruction(command, args):
    """
    Кодирует команду в бинарный формат в зависимости от количества и типа аргументов.
    """
    opcode = COMMANDS.get(command)
    if opcode is None:
        raise ValueError(f"Неизвестная команда {command}")

    # Определение структуры упаковки в зависимости от команды и количества аргументов
    if command == 'LOAD_CONSTANT' and len(args) == 1:
        return struct.pack('<BH', opcode, args[0])
    elif command in ['READ_MEMORY', 'WRITE_MEMORY', 'POPCNT'] and len(args) == 1:
        return struct.pack('<BB', opcode, args[0])
    raise ValueError(f"Неверные аргументы для команды {command}: {args}")


def assemble(source_path, binary_path, log_path):
    """
    Считывает файл с исходным кодом, создает бинарный файл и лог с инструкциями в виде JSON.
    """
    log_data = []
    with open(source_path, 'r') as source_file, open(binary_path, 'wb') as binary_file:
        for line in source_file:
            command, args = parse_instruction(line)
            if command:
                try:
                    binary_instruction = encode_instruction(command, args)
                    binary_file.write(binary_instruction)
                    log_data.append({"command": command, "args": args, "binary": binary_instruction.hex()})
                except ValueError as e:
                    print(f"Ошибка в команде: {e}")

    with open(log_path, 'w') as log_file:
        json.dump(log_data, log_file, indent=4)


if __name__ == "__main__":
    source_path = sys.argv[1]
    binary_path = sys.argv[2]
    log_path = sys.argv[3]
    assemble(source_path, binary_path, log_path)
