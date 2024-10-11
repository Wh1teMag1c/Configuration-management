# Задача 1
### Формулировка задачи
Реализовать на Jsonnet приведенный ниже пример в формате JSON. Использовать в реализации свойство программируемости и принцип DRY.
### Пример
```JSON
{
  "groups": [
    "ИКБО-1-20",
    "ИКБО-2-20",
    "ИКБО-3-20",
    "ИКБО-4-20",
    "ИКБО-5-20",
    "ИКБО-6-20",
    "ИКБО-7-20",
    "ИКБО-8-20",
    "ИКБО-9-20",
    "ИКБО-10-20",
    "ИКБО-11-20",
    "ИКБО-12-20",
    "ИКБО-13-20",
    "ИКБО-14-20",
    "ИКБО-15-20",
    "ИКБО-16-20",
    "ИКБО-17-20",
    "ИКБО-18-20",
    "ИКБО-19-20",
    "ИКБО-20-20",
    "ИКБО-21-20",
    "ИКБО-22-20",
    "ИКБО-23-20",
    "ИКБО-24-20"
  ],
  "students": [
    {
      "age": 19,
      "group": "ИКБО-4-20",
      "name": "Иванов И.И."
    },
    {
      "age": 18,
      "group": "ИКБО-5-20",
      "name": "Петров П.П."
    },
    {
      "age": 18,
      "group": "ИКБО-5-20",
      "name": "Сидоров С.С."
    },
    {
      "age": 19,
      "group": "ИКБО-10-23",
      "name": "Барташевский Д.Д."
    }
  ],
  "subject": "Конфигурационное управление"
} 
```
### Решение
```Jsonnet
local generateGroups = [ 
  std.format("ИКБО-%d-20", i) for i in 1..24 
];

local createStudent = function(name, age, groupIdx) {
  name: name,
  age: age,
  group: generateGroups[groupIdx]
};

local studentsList = [
  createStudent("Иванов И.И.", 19, 3),
  createStudent("Петров П.П.", 18, 4),
  createStudent("Сидоров С.С.", 18, 4),
  createStudent("Барташевский Д.Д.", 19, 9)
];

local course = "Конфигурационное управление";

{
  groups: generateGroups,
  students: studentsList,
  subject: course
}
```
![image](https://github.com/user-attachments/assets/aa0f1652-bd62-4610-8005-f48c01e730de)

# Задача 2
### Формулировка задачи
Реализовать на Dhall приведенный ниже пример в формате JSON. Использовать в реализации свойство программируемости и принцип DRY.
### Пример
```JSON
{
  "groups": [
    "ИКБО-1-20",
    "ИКБО-2-20",
    "ИКБО-3-20",
    "ИКБО-4-20",
    "ИКБО-5-20",
    "ИКБО-6-20",
    "ИКБО-7-20",
    "ИКБО-8-20",
    "ИКБО-9-20",
    "ИКБО-10-20",
    "ИКБО-11-20",
    "ИКБО-12-20",
    "ИКБО-13-20",
    "ИКБО-14-20",
    "ИКБО-15-20",
    "ИКБО-16-20",
    "ИКБО-17-20",
    "ИКБО-18-20",
    "ИКБО-19-20",
    "ИКБО-20-20",
    "ИКБО-21-20",
    "ИКБО-22-20",
    "ИКБО-23-20",
    "ИКБО-24-20"
  ],
  "students": [
    {
      "age": 19,
      "group": "ИКБО-4-20",
      "name": "Иванов И.И."
    },
    {
      "age": 18,
      "group": "ИКБО-5-20",
      "name": "Петров П.П."
    },
    {
      "age": 18,
      "group": "ИКБО-5-20",
      "name": "Сидоров С.С."
    },
    {
      "age": 19,
      "group": "ИКБО-10-23",
      "name": "Барташевский Д.Д."
    }
  ],
  "subject": "Конфигурационное управление"
} 
```
### Решение
```Dhall
let Group = Text

let Student = { name : Text, age : Natural, group : Group }

let students =
      [ { name = "Иванов И.И.", age = 19, group = "ИКБО-4-20" }
      , { name = "Петров П.П.", age = 18, group = "ИКБО-5-20" }
      , { name = "Сидоров С.С.", age = 18, group = "ИКБО-5-20" }
      , { name = "Барташевский Д.Д.", age = 19, group = "ИКБО-10-23" }
      ]

let groups = [ "ИКБО-${Natural/show i}-20" | i <- [1..24] ]

let subject = "Конфигурационное управление"

in  { groups, students, subject }
```

# Задача 3
### Формулировка задачи
Язык нулей и единиц.
```
10
100
11
101101
000
```
Для решения дальнейших задач потребуется программа на Питоне, представленная ниже. Разбираться в самом языке Питон при этом необязательно.
Реализовать грамматики, описывающие следующие языки (для каждого решения привести БНФ). Код решения должен содержаться в переменной BNF:
```Python
import random


def parse_bnf(text):
    '''
    Преобразовать текстовую запись БНФ в словарь.
    '''
    grammar = {}
    rules = [line.split('=') for line in text.strip().split('\n')]
    for name, body in rules:
        grammar[name.strip()] = [alt.split() for alt in body.split('|')]
    return grammar


def generate_phrase(grammar, start):
    '''
    Сгенерировать случайную фразу.
    '''
    if start in grammar:
        seq = random.choice(grammar[start])
        return ''.join([generate_phrase(grammar, name) for name in seq])
    return str(start)


BNF = '''
E = a
'''

for i in range(10):
    print(generate_phrase(parse_bnf(BNF), 'E'))
```
### Решение
```bnf
BNF = '''
E = 0 | 1 | 0 E | 1 E
'''
```

![image](https://github.com/user-attachments/assets/7d262239-23a3-4bf2-97d5-de87a91a825c)

# Задача 4
### Формулировка задачи
Язык правильно расставленных скобок двух видов.
```
(({((()))}))
{}
{()}
()
{}
```
### Решение
```bnf
BNF = '''
E = ( ) | { } | ( E ) | { E }
'''
```

![image](https://github.com/user-attachments/assets/aa78d9ba-3922-40b1-bd17-b24aa36f3e81)

# Задача 5
### Формулировка задачи
Язык выражений алгебры логики.
```
((~(y & x)) | (y) & ~x | ~x) & x
y & ~(y)
(~(y) & y & ~y)
~x
~((x) & y | (y) | (x)) & x | x | (y & ~y)
```
### Решение
```bnf
BNF = '''
E = ( ) | { } | ( E ) | { E }
'''
```

