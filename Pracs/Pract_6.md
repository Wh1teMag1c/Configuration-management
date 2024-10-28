# Задача 0
### Формулировка задачи
Изучить основы языка утилиты make. Распаковать в созданный каталог make.zip, если у вас в в системе нет make.
Создать приведенный ниже Makefile и проверить его работоспособность.  
Визуализировать файл civgraph.txt.

### Решение
#### Создание и тестирование ```Makefile```
<img width="500" alt="Picture_1" src="https://github.com/user-attachments/assets/677443bc-c938-41ee-a10c-30059ccd7fa7">

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
<img width="700" alt="Picture_2" src="https://github.com/user-attachments/assets/aa352f8b-a381-42ba-b97d-b44be10517f8">

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
<img width="700" alt="Picture_3" src="https://github.com/user-attachments/assets/9f39e163-28cf-4510-a474-c90c05cb50e4">

# Задача 2
### Формулировка задачи
Реализовать вариант трансляции, при котором повторный запуск make не выводит для civgraph на экран уже выполненные "задачи".
### Решение
```Python
import json
import os


def collect_dependencies(dependency_graph, target):
    all_dependencies = set(dependency_graph.get(target, []))
    for dependency in dependency_graph.get(target, []):
        all_dependencies.update(collect_dependencies(dependency_graph, dependency))
    return all_dependencies


def create_makefile(dependency_graph, target):
    completed = load_completed_tasks()
    dependencies = collect_dependencies(dependency_graph, target)
    completed.add(target)

    with open('Makefile', 'w') as makefile:
        makefile_entries = ""
        for dependency in dependencies:
            if dependency not in completed:
                completed.add(dependency)
                makefile_entries += f'\t@echo "Processing {dependency}"\n'

        if makefile_entries:
            makefile.write(f'{target}:\n')
            makefile.write(makefile_entries)

    save_completed_tasks(completed)


def load_completed_tasks():
    if os.path.exists("completed_tasks.txt"):
        with open("completed_tasks.txt", 'r') as file:
            return set(file.read().splitlines())
    return set()


def save_completed_tasks(completed):
    with open("completed_tasks.txt", 'w') as file:
        file.write('\n'.join(completed))


if __name__ == '__main__':
    with open('civgraph.json') as json_file:
        dependency_graph = json.load(json_file)
    target_task = input('Введите задачу: ')
    create_makefile(dependency_graph, target_task)
    print("Makefile успешно создан.")
```
<img width="700" alt="Picture_3" src="https://github.com/user-attachments/assets/aeb53965-bb0c-4533-a546-5c494b2bd929">
