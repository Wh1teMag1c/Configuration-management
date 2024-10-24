# Задача 0
### Формулировка задачи
Изучить основы языка утилиты make. Распаковать в созданный каталог make.zip, если у вас в в системе нет make.
Создать приведенный ниже Makefile и проверить его работоспособность.  
Визуализировать файл civgraph.txt.

### Решение
#### Создание и тестирование ```Makefile```
![image](https://github.com/user-attachments/assets/677443bc-c938-41ee-a10c-30059ccd7fa7)
#### Визуализация графа 
```Python
from graphviz import Source

input_file = 'civgraph.txt'

with open(input_file, 'r') as file:
    graph_data = file.read()

graph_source = Source(graph_data)
output_file = 'civgraph_output'
graph_source.render(output_file, format='png', cleanup=True)
```
![civgraph_output](https://github.com/user-attachments/assets/aa352f8b-a381-42ba-b97d-b44be10517f8)

# Задача 1
### Формулировка задачи
Написать программу на Питоне, которая транслирует граф зависимостей civgraph в makefile в духе примера выше. Для мало знакомых с Питоном используется упрощенный вариант civgraph: civgraph.json.
### Пример
```
> make mathematics
mining
bronze_working
sailing
astrology
celestial_navigation
pottery
writing
code_of_laws
foreign_trade
currency
irrigation
masonry
early_empire
mysticism
drama_poetry
mathematics
```
### Решение
```Python
import json


# Функция для записи зависимостей в Makefile
def write_makefile(dependency_graph, output_file='Makefile'):
    try:
        with open(output_file, 'w') as makefile:
            for rule, dependencies in dependency_graph.items():
                dependencies_line = ' '.join(dependencies)
                makefile.write(f'{rule}: {dependencies_line}\n')
                makefile.write(f'\t@echo "Processing {rule}"\n\n')
        print(f"Makefile успешно создан: {output_file}")
    except IOError as e:
        print(f"Ошибка при записи в файл: {e}")


# Функция для загрузки графа зависимостей из JSON файла
def load_dependency_graph(file_path):
    try:
        with open(file_path, 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return None
    except json.JSONDecodeError:
        print("Ошибка при чтении JSON данных.")
        return None


if __name__ == '__main__':
    dependencies = load_dependency_graph('civgraph.json')
    if dependencies:
        write_makefile(dependencies)
```
![image](https://github.com/user-attachments/assets/9f39e163-28cf-4510-a474-c90c05cb50e4)
