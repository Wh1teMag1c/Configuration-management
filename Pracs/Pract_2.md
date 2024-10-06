![image](https://github.com/user-attachments/assets/ac512a21-2b29-4ceb-b632-224ce73aa0a2)# Задача 1
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
```Python
pipdeptree --package matplotlib --graph-output pdf > dependencies.pdf
```
![image](https://github.com/user-attachments/assets/6980e933-5f1a-47fa-9b6d-7c07ba7b23a0)


Создадим .dot файл для зависимостей express:
```dot
digraph ExpressDependencies {
    rankdir=LR;
    node [shape=box];

    "express (4.18.2)" -> "qs (6.11.0)";
    "express (4.18.2)" -> "depd (2.0.0)";
    "express (4.18.2)" -> "etag (1.8.1)";
    "express (4.18.2)" -> "send (0.17.1)";
    "express (4.18.2)" -> "vary (1.1.2)";
    "express (4.18.2)" -> "fresh (0.5.2)";
    "express (4.18.2)" -> "cookie (0.5.0)";
    "express (4.18.2)" -> "accepts (1.3.8)";
    "express (4.18.2)" -> "methods (1.1.2)";
    "express (4.18.2)" -> "type-is (1.6.18)";
    "express (4.18.2)" -> "parseurl (1.3.3)";
    "express (4.18.2)" -> "statuses (1.5.0)";
    "express (4.18.2)" -> "encodeurl (1.0.2)";
    "express (4.18.2)" -> "proxy-addr (2.0.7)";
    "express (4.18.2)" -> "body-parser (1.20.2)";
    "express (4.18.2)" -> "escape-html (1.0.3)";
    "express (4.18.2)" -> "http-errors (2.0.0)";
    "express (4.18.2)" -> "on-finished (2.4.1)";
    "express (4.18.2)" -> "safe-buffer (5.2.1)";
    "express (4.18.2)" -> "utils-merge (1.0.1)";
    "express (4.18.2)" -> "content-type (1.0.4)";
    "express (4.18.2)" -> "finalhandler (1.2.0)";
    "express (4.18.2)" -> "range-parser (1.2.1)";
    "express (4.18.2)" -> "serve-static (1.15.0)";
    "express (4.18.2)" -> "array-flatten (1.1.1)";
    "express (4.18.2)" -> "path-to-regexp (6.2.0)";
    "express (4.18.2)" -> "setprototypeof (1.2.0)";
    "express (4.18.2)" -> "cookie-signature (1.0.6)";
    "express (4.18.2)" -> "merge-descriptors (1.0.1)";
    "express (4.18.2)" -> "content-disposition (0.5.4)";

    "qs (6.11.0)" -> "stringify (0.0.1)";
    "qs (6.11.0)" -> "parse (0.0.1)";
    
    "body-parser (1.20.2)" -> "bytes (3.1.0)";
    "body-parser (1.20.2)" -> "content-type (1.0.4)";
    
    "send (0.17.1)" -> "destroy (1.0.4)";
    "send (0.17.1)" -> "mime (3.0.0)";
    
    "proxy-addr (2.0.7)" -> "ip (1.1.5)";
    
    "cookie-signature (1.0.6)" -> "cookie (0.5.0)";
}
```
![express_d](https://github.com/user-attachments/assets/d878400d-8025-4fef-b132-c1112a9b8f0c)

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

% Определяем переменные для каждой цифры билета
array[1..6] of var 0..9: digits;

% Ограничение: все цифры должны быть разными
constraint all_different(digits);

% Сумма первых трех цифр должна равняться сумме последних трех цифр
constraint sum(digits[1..3]) = sum(digits[4..6]);

% Найдем минимальное решение для суммы первых трех цифр
var int: sum1 = sum(digits[1..3]);
solve minimize sum1;

% Читаем вывод
output [
    "Digits: ", show(digits), "\n",
    "Sum of first three digits: ", show(sum1), "\n"
];
```
### Ответ
![image](https://github.com/user-attachments/assets/61b48110-d888-488a-a52c-3d66392658bd)

# Задача 5
### Формулировка задачи
Решить на MiniZinc задачу о зависимостях пакетов для рисунка, приведенного ниже.
![image](https://github.com/user-attachments/assets/fee5e211-23b4-46a8-86b8-508047ca42d5)

### Решение
```MiniZinc
int: totalMenu = 6;
int: totalDropdown = 5;
int: totalIcon = 2;

var 1..totalMenu: menu;
var 1..totalDropdown: dropdown;
var 1..totalIcon: icon;

array[1..totalMenu] of tuple(int, int, int): menuVersions = 
  [(1,0,0), (1,1,0), (1,2,0), (1,3,0), (1,4,0), (1,5,0)];
  
array[1..totalDropdown] of tuple(int, int, int): dropdownVersions = 
  [(1,8,0), (2,0,0), (2,1,0), (2,2,0), (2,3,0)];
  
array[1..totalIcon] of tuple(int, int, int): iconVersions = 
  [(1,0,0), (2,0,0)];

constraint (menuVersions[menu] == (1,0,0) \/ menuVersions[menu] == (1, 5, 0) /\ iconVersions[icon] == (1, 0, 0));
constraint (menuVersions[menu].2 >= 1 /\ menuVersions[menu].2 <= 5) -> (dropdownVersions[dropdown] == (2, 3, 0) \/ dropdownVersions[dropdown] == (2, 0, 0));
constraint menuVersions[menu] == (1, 0, 0) -> dropdownVersions[dropdown] == (1, 8, 0);
constraint (dropdownVersions[dropdown].2 >= 0 /\ dropdownVersions[dropdown].2 <= 3) -> iconVersions[icon] == (2, 0, 0);

solve satisfy;

output [
  "Selected Menu Version: ", show(menuVersions[menu]), "\n",
  "Selected Dropdown Version: ", show(dropdownVersions[dropdown]), "\n",
  "Selected Icon Version: ", show(iconVersions[icon]), "\n"
];
```
### Ответ
![image](https://github.com/user-attachments/assets/1f93feba-be97-42c7-945d-c7065393fc0a)

# Задача 6
### Формулировка задачи
Решить на MiniZinc задачу о зависимостях пакетов для следующих данных:
```
root 1.0.0 зависит от foo ^1.0.0 и target ^2.0.0.
foo 1.1.0 зависит от left ^1.0.0 и right ^1.0.0.
foo 1.0.0 не имеет зависимостей.
left 1.0.0 зависит от shared >=1.0.0.
right 1.0.0 зависит от shared <2.0.0.
shared 2.0.0 не имеет зависимостей.
shared 1.0.0 зависит от target ^1.0.0.
target 2.0.0 и 1.0.0 не имеют зависимостей.
```

### Решение
```MiniZinc
% Определяем количество версий для каждого пакета
int: num_foo = 2;         % foo имеет 2 версии: 1.0.0 и 1.1.0
int: num_left = 1;        % left имеет 1 версию: 1.0.0
int: num_right = 1;       % right имеет 1 версию: 1.0.0
int: num_shared = 2;      % shared имеет 2 версии: 1.0.0 и 2.0.0
int: num_target = 2;      % target имеет 2 версии: 1.0.0 и 2.0.0

set of int: VersionsFoo = 1..num_foo;
set of int: VersionsLeft = 1..num_left;
set of int: VersionsRight = 1..num_right;
set of int: VersionsShared = 1..num_shared;
set of int: VersionsTarget = 1..num_target;

% Переменные для хранения выбранной версии каждого пакета
var VersionsFoo: foo_version;
var VersionsLeft: left_version;
var VersionsRight: right_version;
var VersionsShared: shared_version;
var VersionsTarget: target_version;

% Задаем зависимости между пакетами

% root 1.0.0 зависит от foo ^1.0.0 и target ^2.0.0
constraint foo_version >= 1 /\ target_version == 2;

% foo 1.1.0 зависит от left ^1.0.0 и right ^1.0.0
constraint 
    (foo_version == 2 -> left_version == 1 /\ right_version == 1);

% left 1.0.0 зависит от shared >=1.0.0
constraint 
    (left_version == 1 -> shared_version >= 1);

% right 1.0.0 зависит от shared <2.0.0
constraint 
    (right_version == 1 -> shared_version < 2);

% shared 1.0.0 зависит от target ^1.0.0
constraint 
    (shared_version == 1 -> target_version >= 1);

% Оптимизация: выбираем наиболее новые версии пакетов
solve satisfy;
```
### Ответ
![image](https://github.com/user-attachments/assets/429ee7e0-1363-43d4-a5df-499c7493b22d)
