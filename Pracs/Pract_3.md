# Задача 1
### Формулировка задачи
Реализовать на Jsonnet приведенный ниже пример в формате JSON. Использовать в реализации свойство программируемости и принцип DRY.
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
### Решение
