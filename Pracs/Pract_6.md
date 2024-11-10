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

# Задача 3
### Формулировка задачи
Добавить цель clean, не забыв и про "животное".
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
    all_targets = set()
    all_dependencies = collect_dependencies(dependency_graph, target)
    all_dependencies.add(target)

    with open('Makefile', 'w') as makefile:
        makefile.write("all: " + " ".join(sorted(all_dependencies)) + "\n\n")
        for target in sorted(all_dependencies):
            if target not in completed:
                completed.add(target)
                target_dependencies = " ".join(dependency_graph.get(target, []))
                all_targets.add(target)
                makefile.write(f'{target}: {target_dependencies}\n')
                makefile.write(f'\t@echo "Processing {target}"\n\n')

        makefile.write(".PHONY: " + " ".join(sorted(all_targets)) + "\n")

    save_completed_tasks(completed)


def load_completed_tasks():
    if os.path.exists("completed_tasks.txt"):
        with open("completed_tasks.txt", 'r') as file:
            return set(file.read().splitlines())
    return set()


def save_completed_tasks(completed):
    with open("completed_tasks.txt", 'w') as file:
        file.write('\n'.join(completed))


def clean():
    if os.path.exists("completed_tasks.txt"):
        os.remove("completed_tasks.txt")
        print("Cleaned completed tasks.")


if __name__ == '__main__':
    with open('civgraph.json') as json_file:
        dependency_graph = json.load(json_file)
    target_task = input('Введите задачу: ')
    if target_task == "clean":
        clean()
    else:
        create_makefile(dependency_graph, target_task)
        print("Makefile успешно создан.")
```
Пример содержимого Makefile для цели `mathematics`:
```Makefile
all: astrology bronze_working celestial_navigation code_of_laws currency drama_poetry early_empire foreign_trade irrigation masonry mining mysticism pottery sailing writing

astrology: 
	@echo "Processing astrology"

bronze_working: mining
	@echo "Processing bronze_working"

celestial_navigation: sailing astrology
	@echo "Processing celestial_navigation"

code_of_laws: 
	@echo "Processing code_of_laws"

currency: writing foreign_trade
	@echo "Processing currency"

drama_poetry: astrology irrigation masonry early_empire mysticism
	@echo "Processing drama_poetry"

early_empire: foreign_trade
	@echo "Processing early_empire"

foreign_trade: code_of_laws
	@echo "Processing foreign_trade"

irrigation: pottery
	@echo "Processing irrigation"

masonry: mining
	@echo "Processing masonry"

mining: 
	@echo "Processing mining"

mysticism: foreign_trade
	@echo "Processing mysticism"

pottery: 
	@echo "Processing pottery"

sailing: 
	@echo "Processing sailing"

writing: pottery
	@echo "Processing writing"

.PHONY: astrology bronze_working celestial_navigation code_of_laws currency drama_poetry early_empire foreign_trade irrigation masonry mining mysticism pottery sailing writing
```
<img width="700" alt="Picture_3" src="https://github.com/user-attachments/assets/792fd90d-7665-47a7-858b-6b64d83d1998">

# Задача 4
### Формулировка задачи
Написать makefile для следующего скрипта сборки:
```
gcc prog.c data.c -o prog
dir /B > files.lst
7z a distr.zip *.*
```
Вместо gcc можно использовать другой компилятор командной строки, но на вход ему должны подаваться два модуля: prog и data. Если используете не Windows, то исправьте вызовы команд на их эквиваленты из вашей ОС. В makefile должны быть, как минимум, следующие задачи: all, clean, archive. Обязательно покажите на примере, что уже сделанные подзадачи у вас не перестраиваются.
### Решение
prog.c:
```c
#include <stdio.h>
#include "data.h"

int main() {
    printf("Main program\n");
    print_data();
    return 0;
}
```
data.c:
```c
#include <stdio.h>

void print_data() {
    printf("Data module\n");
}
```
Makefile:
```Makefile
CC = gcc
OUT = prog
SRC = prog.c data.c
ARCHIVE = distr.zip

all: $(OUT)

$(OUT): $(SRC)
	$(CC) $(SRC) -o $(OUT)

clean:
	rm -f $(OUT) files.lst $(ARCHIVE)

archive:
	ls > files.lst
	7z a $(ARCHIVE) *.*

.PHONY: all clean archive
```
Выполнение команды `make all`:

<img width="700" alt="Picture_3" src="https://github.com/user-attachments/assets/771b0fab-0438-469d-86e7-2a3252c4d1db">

Выполнение команды `make archive`:

<img width="700" alt="Picture_3" src="https://github.com/user-attachments/assets/56a92944-40cb-4b2a-8357-bf8401d5def4">

Выполнение команды `make clean`:

<img width="700" alt="Picture_3" src="https://github.com/user-attachments/assets/0eb10eeb-0280-49ca-9de5-98325cd78266">
