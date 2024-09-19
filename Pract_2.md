# Задача 1
### Формулировка задачи
Вывести служебную информацию о пакете matplotlib (Python). Разобрать основные элементы содержимого файла со служебной информацией из пакета.
### Решение
```
pip show matplotlib
```
![image](https://github.com/user-attachments/assets/ea1afb39-b332-40f4-9212-38f696c2ecf3)

#### Основные элементы содержимого файла со служебной информацией из пакета:
* Name: matplotlib (имя пакета)
* Version: 3.9.2 (версия пакета по стандарту семантического версионирования (SemVer). В данном случае 3.9.2 указывает на третью основную версию (MAJOR — 3), с девятым минорным обновлением (MINOR — 9), а патч (PATCH — 2) включает исправления ошибок без изменения функциональности)
* Summary: Python plotting package (краткое описание пакета. В этом случае пакет matplotlib — это библиотека для построения графиков в Python)
* Home-page: https://matplotlib.org (ссылка на официальный сайт или документацию пакета)
* Author: John D. Hunter, Michael Droettboom (авторы пакета)
* Author-email: Unknown matplotlib-users@python.org (контактная информация автора)
* License: License agreement for matplotlib versions 1.3.0 and later (лицензия, по которой распространяется пакет)
### Формулировка задачи
Как получить пакет без менеджера пакетов, прямо из репозитория?
### Решение
Чтобы скачать и установить пакет без использования менеджера пакетов, можно получить его исходный код напрямую из репозитория, например, с GitHub.
```
git clone https://github.com/matplotlib/matplotlib.git
cd matplotlib
pip install .
```
![image](https://github.com/user-attachments/assets/53e27b28-3cf7-4f08-b2e3-96487a833296)

![image](https://github.com/user-attachments/assets/a5270a79-7869-49d4-9642-6e343ea1a214)

# Задача 2
### Формулировка задачи
Вывести служебную информацию о пакете express (JavaScript). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?
### Решение
```
npm view express
```
![image](https://github.com/user-attachments/assets/0460a3b5-0ce2-4eee-8cca-6fb45270ea3a)

#### Основные элементы содержимого файла со служебной информацией из пакета:
* express (имя пакета)
* 4.21.0 (Версия пакета по стандарту семантического версионирования (SemVer). В данном случае 4.21.0 указывает на четвёртую основную версию (MAJOR — 4), с двадцать первым минорным обновлением (MINOR — 9), а патч (PATCH — 0) включает исправления ошибок без изменения функциональности)
* MIT (лицензия, по которой распространяется пакет (в данном случае MIT, одна из самых открытых лицензий)
* deps: 31 (количество зависимостей. Пакет Express требует 31 внешнюю библиотеку для работы)
* versions: 279 (количество опубликованных версий Express.js)
* Fast, unopinionated, minimalist web framework (краткое описание пакета: Express — это быстрый, минималистичный веб-фреймворк для Node.js)
* http://expressjs.com/ (ссылка на официальный сайт, где можно найти документацию и другие ресурсы, связанные с пакетом)
* keywords: express, framework, sinatra, web, http, rest, restful, router, app, api (список ключевых слов, по которым можно найти пакет)
* dist (информация о дистрибуции пакета)
  * .tarball: https://registry.npmjs.org/express/-/express-4.21.0.tgz (ссылка на архив пакета в формате .tgz, который можно скачать)
  * .shasum: d57cb706d49623d4ac27833f1cbc466b668eb915 (контрольная сумма (SHA-1) для проверки целостности пакета)
  * .integrity: sha512-VqcNGcj/Id5ZT1LZ/cfihi3ttTn+NJmkli2eZADigjq29qTlWi/hAQ43t/VLPq8+UX06FCEx3ByOYet6ZFblng== (контрольная сумма по алгоритму SHA-512 для подтверждения целостности)
  * .unpackedSize: 220.8 kB (размер распакованного пакета)
* dependencies (список зависимостей пакета и их версии)
* maintainers (список мейнтейнеров пакета и их контактные данные)
* dist-tags (теги дистрибуции)
  * latest: 4.21.0 (стабильная версия пакета)
  * next: 5.0.0 (следующая версия, которая еще не является стабильной)
### Формулировка задачи
Как получить пакет без менеджера пакетов, прямо из репозитория?
### Решение
Чтобы скачать и установить пакет без использования менеджера пакетов, можно получить его исходный код напрямую из репозитория, например, с GitHub.
```
git clone https://github.com/expressjs/express.git
cd express
npm install
```
![image](https://github.com/user-attachments/assets/e52b58d8-a8c1-4933-8b18-71edef6c9e28)

# Задача 3
### Формулировка задачи
Сформировать graphviz-код и получить изображения зависимостей matplotlib и express.
### Решение
```
pip show matplotlib
```
# Задача 4
### Формулировка задачи
Следующие задачи можно решать с помощью инструментов на выбор:

Решатель задачи удовлетворения ограничениям (MiniZinc).
SAT-решатель (MiniSAT).
SMT-решатель (Z3).
Изучить основы программирования в ограничениях. Установить MiniZinc, разобраться с основами его синтаксиса и работы в IDE.

Решить на MiniZinc задачу о счастливых билетах. Добавить ограничение на то, что все цифры билета должны быть различными (подсказка: используйте all_different). Найти минимальное решение для суммы 3 цифр.
### Решение
```MiniZinc
include "alldifferent.mzn";

% Массив цифр билета
array[1..6] of var 0..9: digits;

% Ограничение на то, что все цифры различны
constraint all_different(digits);

% Ограничение на счастливый билет: сумма первых 3 цифр равна сумме последних 3
constraint digits[1] + digits[2] + digits[3] = digits[4] + digits[5] + digits[6];

% Ограничение для поиска минимального возможного решения
solve minimize digits[1] * 100000 + digits[2] * 10000 + digits[3] * 1000 + digits[4] * 100 + digits[5] * 10 + digits[6];
```
### Ответ
![image](https://github.com/user-attachments/assets/603e60e6-386c-43b0-ba9c-b0cb6ab62cd1)

# Задача 5
### Формулировка задачи
Решить на MiniZinc задачу о зависимостях пакетов для рисунка, приведенного ниже.
![image](https://github.com/user-attachments/assets/fee5e211-23b4-46a8-86b8-508047ca42d5)

### Решение
```MiniZinc
% Определяем количество версий для каждого пакета
int: num_menu = 6;        % Количество версий меню
int: num_dropdown = 5;    % Количество версий dropdown
int: num_icons = 2;       % Количество версий icons

set of int: VersionsMenu = 1..num_menu;
set of int: VersionsDropdown = 1..num_dropdown;
set of int: VersionsIcons = 1..num_icons;

% Переменные для хранения выбранной версии каждого пакета
var VersionsMenu: menu_version;
var VersionsDropdown: dropdown_version;
var VersionsIcons: icons_version;

% Задаем зависимости между пакетами

% Зависимости пакета menu от пакетов dropdown и icons
constraint 
    (menu_version == 6 -> dropdown_version == 5 /\ icons_version == 2) /\
    (menu_version == 5 -> dropdown_version == 4 /\ icons_version == 2) /\
    (menu_version == 4 -> dropdown_version == 3 /\ icons_version == 2) /\
    (menu_version == 3 -> dropdown_version == 2 /\ icons_version == 2) /\
    (menu_version == 2 -> dropdown_version == 2 /\ icons_version == 2) /\
    (menu_version == 1 -> dropdown_version == 1 /\ icons_version == 1);

% Зависимости пакета dropdown от icons
constraint
    (dropdown_version == 5 -> icons_version == 2) /\
    (dropdown_version == 4 -> icons_version == 2) /\
    (dropdown_version == 3 -> icons_version == 2) /\
    (dropdown_version == 2 -> icons_version >= 1) /\
    (dropdown_version == 1 -> icons_version >= 1);

% Оптимизация: выбираем наиболее новые версии пакетов
solve maximize menu_version + dropdown_version + icons_version;
```
### Ответ
![image](https://github.com/user-attachments/assets/f34e4804-80e4-46ae-aedc-f889b6835696)
