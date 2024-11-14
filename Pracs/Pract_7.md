# Задача 1
### Формулировка задачи
Реализовать с помощью математического языка LaTeX нижеприведенную формулу:
![image](https://github.com/user-attachments/assets/e6e4738f-bc1d-4221-91d1-10aadd16d8cc)
Прислать код на LaTeX и картинку-результат, где, помимо формулы, будет указано ФИО студента.
### Решение
```latex
\documentclass{article}
\usepackage{amsmath}

\begin{document}

\begin{equation*}
\int_{x}^{\infty} \frac{dt}{t(t^2 - 1) \log t} = \int_{x}^{\infty} \frac{1}{t \log t} \left( \sum_{m} t^{-2m} \right) dt = \sum_{m} \int_{x}^{\infty} \frac{t^{-2m}}{t \log t} \, dt \overset{(u = t^{-2m})}{=} - \sum_{m} \operatorname{li}(x^{-2m})
\end{equation*}

\vspace{1cm}

Барташевский Дмитрий Дмитриевич

\end{document}
```
![image](https://github.com/user-attachments/assets/b08a07fe-c1be-453e-b415-be1347259fbb)

# Задача 2
### Формулировка задачи
На языке PlantUML реализовать диаграмму на рисунке ниже. Прислать текст на PlantUML и картинку-результат, в которой ФИО студента заменены Вашими собственными. Обратите внимание на оформление, желательно придерживаться именно его, то есть без стандартного желтого цвета и проч. Чтобы много не писать используйте псевдонимы с помощью ключевого слова "as".

Используйте [онлайн-редактор](https://plantuml-editor.kkeisuke.com/).
### Решение
```plantuml
@startuml
skinparam lifelineStrategy solid
actor Student as "Студент Барташевский Д.Д."
database Piazza as "Piazza"
actor Teacher as "Преподаватель"

Teacher -> Piazza: Публикация задачи
activate Piazza
Piazza --> Teacher: Задача опубликована
deactivate Piazza

Student -> Piazza: Поиск задач
activate Piazza
Piazza --> Student: Получение задачи
deactivate Piazza

Student -> Piazza: Публикация решения
activate Piazza
Piazza --> Student: Решение опубликовано
deactivate Piazza

Teacher -> Piazza: Поиск решений
activate Piazza
Piazza --> Teacher: Решение найдено

Teacher -> Piazza: Публикация оценки
Piazza --> Teacher: Оценка опубликована
deactivate Piazza

Student -> Piazza: Проверка оценки
activate Piazza
Piazza --> Student: Оценка получена
deactivate Piazza
@enduml
```
![image](https://github.com/user-attachments/assets/130e1453-993a-4b8a-8f9e-c523105f9891)
