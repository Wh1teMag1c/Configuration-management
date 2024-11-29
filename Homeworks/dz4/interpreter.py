import json
import struct
import sys

# Загрузка кода операций
COMMANDS = {
    7: 'LOAD_CONST',
    23: 'READ_MEM',
    24: 'WRITE_MEM',
    17: 'POPCNT'
}

stack = [0]
memory = [0] * 1024


def load_const(binary_file):
    B = struct.unpack('<H', binary_file.read(2))[0]
    stack.append(B)


def read_mem(binary_file):
    B = struct.unpack('<B', binary_file.read(1))[0]
    node = stack.pop()
    stack.append(memory[node + B])


def write_mem(binary_file):
    B = struct.unpack('<B', binary_file.read(1))[0]
    node = stack.pop()
    memory[node + B] = node


def popcnt(binary_file):
    B = struct.unpack('<B', binary_file.read(1))[0]
    node = stack.pop()
    memory[node] = memory[node + B]


def execute(binary_path, result_path, memory_range):
    with open(binary_path, 'rb') as binary_file:
        while True:
            opcode_byte = binary_file.read(1)
            if not opcode_byte:
                break
            opcode = opcode_byte[0]
            if opcode == 7:  # LOAD_CONST
                load_const(binary_file)
            elif opcode == 23:  # READ_MEM
                read_mem(binary_file)
            elif opcode == 24:  # WRITE_MEM
                write_mem(binary_file)
            elif opcode == 17:  # POPCNT
                popcnt(binary_file)
            else:
                raise ValueError(f"Неизвестная команда с кодом: {opcode}")

    # Сохранение указанного диапазона памяти в результат
    with open(result_path, 'w') as result_file:
        json.dump(memory[memory_range[0]:memory_range[1]], result_file)


if __name__ == "__main__":
    binary_path = sys.argv[1]
    result_path = sys.argv[2]
    memory_range = list(map(int, sys.argv[3].split(',')))
    execute(binary_path, result_path, memory_range)
