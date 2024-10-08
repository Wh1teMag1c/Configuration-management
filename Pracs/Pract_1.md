# Задача 1
### Формулировка задачи
Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd (вам понадобится grep).
### Решение
```bash
cut -d: -f1 /etc/passwd | sort
```
![photo_2024-09-04_19-40-57](https://github.com/user-attachments/assets/8578a882-d1e4-450d-b274-3b7beb0fed80)
# Задача 2
### Формулировка задачи
Вывести данные /etc/protocols в отформатированном и отсортированном порядке для 5 наибольших портов, как показано в примере ниже:
```
[root@localhost etc]# cat /etc/protocols ...
142 rohc
141 wesp
140 shim6
139 hip
138 manet
```
### Решение
```bash
awk '{print $2, $1}' /etc/protocols | sort -n -r | head -n 5
```
![image](https://github.com/user-attachments/assets/9824a142-541c-4e32-85ef-65a2d0b6b596)
# Задача 3
### Формулировка задачи
Написать программу banner средствами bash для вывода текстов, как в следующем примере (размер баннера должен меняться!):
```
[root@localhost ~]# ./banner "Hello from RTU MIREA!"
+-----------------------+
| Hello from RTU MIREA! |
+-----------------------+
```
### Решение
```bash
#!/bin/bash
text="$1"
text_len=${#text}
echo -n "+"
for ((i=-2;i<text_len;i++))
do
echo -n "-"
done
echo "+"
echo "| $text |"
echo -n "+"
for ((i=-2;i<text_len;i++))
do
echo -n "-"
done
echo "+"
```
![image](https://github.com/user-attachments/assets/e67c8032-8a5a-4829-b97f-2d95907402a9)
# Задача 4
### Формулировка задачи
Написать программу для вывода всех идентификаторов (по правилам C/C++ или Java) в файле (без повторений).
Пример для hello.c:
```
h hello include int main n printf return stdio void world
```
### Решение
```bash
grep -o -E '\b[a-zA-Z_][a-zA-Z0-9_]*\b' hello.c | sort -u
```
![image](https://github.com/user-attachments/assets/f762181c-d3c4-4adf-b864-be1a0410a499)
# Задача 5
### Формулировка задачи
Написать программу для регистрации пользовательской команды (правильные права доступа и копирование в /usr/local/bin).
Например, пусть программа называется reg:
```
./reg banner
```
В результате для banner задаются правильные права доступа и сам banner копируется в /usr/local/bin.
![image](https://github.com/user-attachments/assets/2ad01d22-a26a-4c3a-ada0-83577a64e206)

![image](https://github.com/user-attachments/assets/d5ad146a-eb6a-4eef-93ab-50b63aa47c72)
### Решение
```bash
#!/bin/bash
chmod +x "$1"
sudo cp "$1" /usr/local/bin/
```
# Задача 6
### Формулировка задачи
Написать программу для проверки наличия комментария в первой строке файлов с расширением c, js и py.
### Решение
```bash
#!/bin/bash
for file in *.c *.js *.py; do
    first_line=$(head -n 1 "$file")
    if [[ "$first_line" == \#* ]] || [[ "$first_line" == ///* ]] || [[ "$first_line" == /* ]]; then
        echo "$file: Есть комментарий"
    else
        echo "$file: Комментария нет"
    fi
done
```
![image](https://github.com/user-attachments/assets/d9de4203-cbff-42fb-94bf-f541f5b83c76)
# Задача 7
### Формулировка задачи
Написать программу для нахождения файлов-дубликатов (имеющих 1 или более копий содержимого) по заданному пути (и подкаталогам).
### Решение
```bash
find "$1" -type f -exec md5sum {} + | sort | uniq -w32 -d | awk '{print "Файл с дубликатом: " $2}'
```
![image](https://github.com/user-attachments/assets/5d414c61-d27b-484c-bdac-f799d3975af5)
# Задача 8
### Формулировка задачи
Написать программу, которая находит все файлы в данном каталоге с расширением, указанным в качестве аргумента и архивирует все эти файлы в архив tar.
### Решение
```bash
tar -czvf archive.tar.gz $(find . -type f -name "*.$1")
```
![image](https://github.com/user-attachments/assets/8e7b749d-9207-4cc1-91ef-8b88f989d845)
# Задача 9
### Формулировка задачи
Написать программу, которая заменяет в файле последовательности из 4 пробелов на символ табуляции. Входной и выходной файлы задаются аргументами.
### Решение
```bash
sed 's/ \{4\}/\t/g' "$1" > "$2"
```
![image](https://github.com/user-attachments/assets/3af24e6c-3ac9-4762-8aaa-9f32c4b3446c)

# Задача 10
### Формулировка задачи
Написать программу, которая выводит названия всех пустых текстовых файлов в указанной директории. Директория передается в программу параметром.
### Решение
```bash
find "$directory" -type f -name "*.txt" -exec bash -c 'if [ ! -s "$1" ]; then echo "$(basename "$1")"; fi' _ {} \;
```
![image](https://github.com/user-attachments/assets/17e1615a-8816-48f0-bee2-1f334611bcd5)
