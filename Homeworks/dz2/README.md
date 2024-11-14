# Визуализатор графа зависимостей коммитов Git

## Описание
Этот проект представляет собой инструмент для анализа и визуализации графа зависимостей коммитов в Git-репозитории. Программа считывает данные из репозитория, строит граф зависимости между коммитами и отображает его в формате Graphviz. Граф сохраняется как исходный файл `.dot` и как изображение `.png`.

## Установка

1. **Клонируйте репозиторий:**
  ```bash
  git clone <URL репозитория>
  cd <директория проекта>>
  ```
2. **Установите зависимости**
  ```bash
  pip install -r requirements.txt
  ```
## Использование
Для запуска основного скрипта используйте следующую команду:
```bash
python main.py --repo <путь_к_репозиторию> --output <путь_к_файлу_для_сохранения> --date <дата_в_формате_dd.mm.yyyy>
```
Пример использования:
```bash
python main.py --repo D:\Programming\MIREA\Frontend\Frontend_1 --output output_graph.dot --date 01.11.2024
```
Это создаст граф зависимостей коммитов до указанной даты и сохранит его в файле `output_graph.dot`, а также сгенерирует изображение `output.png`.

Пример вывода текста в консоль:

<img width="800" alt="Picture_1" src="https://github.com/user-attachments/assets/d40de5ab-1155-4df7-b4e9-3100aead3f66">

Файл output_graph.dot:

<img width="800" alt="Picture_1" src="https://github.com/user-attachments/assets/9a604028-9e2c-4925-bb52-b78595b1bcea">

Изображение графа output.png:

<img width="800" alt="Picture_1" src="https://github.com/user-attachments/assets/16575a99-03e9-4053-9e69-32e59364d410">

## Тестирование
Для запуска тестов используйте модуль unittest:
```bash
python -m unittest tests.py
```

Пример тестирования:

<img width="800" alt="Picture_1" src="https://github.com/user-attachments/assets/61a770cd-7459-4a9a-9aeb-4e703dcd5adc">