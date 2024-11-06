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
<img width="800" alt="Picture_1" src="https://github.com/user-attachments/assets/6f8a79fa-f76a-497a-86e7-23e87da0a012">

# Задача 2
### Формулировка задачи
Создать локальный git-репозиторий. Задать свои имя и почту (далее – coder1). Разместить файл prog.py с какими-нибудь данными. Прислать в текстовом виде диалог с git.
### Решение
<img width="700" alt="Picture_1" src="https://github.com/user-attachments/assets/df96207c-d666-41bf-a513-475f1431907f">

# Задача 3
### Формулировка задачи
Создать рядом с локальным репозиторием bare-репозиторий с именем server. Загрузить туда содержимое локального репозитория. Команда git remote -v должна выдать информацию о server! Синхронизировать coder1 с server.

Клонировать репозиторий server в отдельной папке. Задать для работы с ним произвольные данные пользователя и почты (далее – coder2). Добавить файл readme.md с описанием программы. Обновить сервер.

Coder1 получает актуальные данные с сервера. Добавляет в readme в раздел об авторах свою информацию и обновляет сервер.

Coder2 добавляет в readme в раздел об авторах свою информацию и решает вопрос с конфликтами.

Прислать список набранных команд и содержимое git log.

Пример лога коммитов:
```
*   commit a457d748f0dab75b4c642e964172887de3ef4e3e
|\  Merge: 48ce283 d731ba8
| | Author: Coder 2 <coder2@corp.com>
| | Date:   Sun Oct 11 11:27:09 2020 +0300
| | 
| |     readme fix
| | 
| * commit d731ba84014d603384cc3287a8ea9062dbb92303
| | Author: Coder 1 <coder1@corp.com>
| | Date:   Sun Oct 11 11:22:52 2020 +0300
| | 
| |     coder 1 info
| | 
* | commit 48ce28336e6b3b983cbd6323500af8ec598626f1
|/  Author: Coder 2 <coder2@corp.com>
|   Date:   Sun Oct 11 11:24:00 2020 +0300
|   
|       coder 2 info
| 
* commit ba9dfe9cb24316694808a347e8c36f8383d81bbe
| Author: Coder 2 <coder2@corp.com>
| Date:   Sun Oct 11 11:21:26 2020 +0300
| 
|     docs
| 
* commit 227d84c89e60e09eebbce6c0b94b41004a4541a4
  Author: Coder 1 <coder1@corp.com>
  Date:   Sun Oct 11 11:11:46 2020 +0300
  
      first commit
```
# Задача 4
### Формулировка задачи
Написать программу на Питоне (или другом ЯП), которая выводит список содержимого всех объектов репозитория. Воспользоваться командой "git cat-file -p". Идеальное решение – не использовать иных сторонних команд и библиотек для работы с git.
### Решение
```Python
import subprocess


def list_git_objects():
    try:
        result = subprocess.run(
            ["git", "rev-list", "--all", "--objects"],
            capture_output=True, text=True, check=True
        )
        return [line.split()[0] for line in result.stdout.splitlines()]
    except subprocess.CalledProcessError:
        print("Ошибка при получении списка объектов")
        return []


def main():
    for obj in list_git_objects():
        print(f"\n{'=' * 45}\nHash {obj}\n{'=' * 45}")
        subprocess.run(["git", "cat-file", "-p", obj], check=True)


if __name__ == "__main__":
    main()
```
<img width="600" alt="Picture_1" src="https://github.com/user-attachments/assets/61c6d21b-707a-4a19-a0aa-6816f48df216">
