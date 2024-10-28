# Задача 1
### Формулировка задачи
На сайте https://onlywei.github.io/explain-git-with-d3 или http://git-school.github.io/visualizing-git/ (цвета могут отличаться, есть команды undo/redo) с помощью команд эмулятора git получить следующее состояние проекта (сливаем master с first, перебазируем second на master): см. картинку ниже. Прислать свою картинку.
<img width="700" alt="Picture_1" src="https://github.com/user-attachments/assets/332eea25-74f8-43d9-b9c9-81b99ee39f49">
### Решение
```bash
git commit
git branch first
git branch second
git commit
git commit
git checkout first
git commit
git commit
git checkout master
git merge first
git checkout second
git commit
git commit
git rebase master
git checkout master
git merge second
git checkout [in_hash]
git tag in 
```
<img width="700" alt="Picture_1" src="https://github.com/user-attachments/assets/6f8a79fa-f76a-497a-86e7-23e87da0a012">
