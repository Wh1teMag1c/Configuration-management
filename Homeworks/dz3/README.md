# Конвертер XML в учебный конфигурационный язык

## Описание
Этот проект представляет собой инструмент командной строки для преобразования текста из формата XML в специальный учебный конфигурационный язык.

Инструмент поддерживает сохранение результата в виде исходного файла .dot, который можно использовать для дальнейшей работы с Graphviz, а также вывод изображения графа в формате .png для визуального анализа.

### Основные структуры
1. Комментарии:
    * Однострочные комментарии начинаются с символа # и продолжаются до конца строки.
    ```bash
    # Это однострочный комментарий
    ```
    * Многострочные комментарии заключены в (* ... *) и могут занимать несколько строк.
    ```bash
    (*
    Это многострочный
    комментарий
    *)
    ```
2. Словари:
    основная структура для хранения данных, записывается в фигурных скобках {} и содержит пары имя = значение;.
    ```bash
    {
        имя1 = значение1;
        имя2 = значение2;
    }
    ```
3. Имена:
   допустимые идентификаторы, которые могут использоваться в качестве ключей в словаре. Они состоят из букв латинского алфавита и символа подчеркивания: [_a-zA-Z]+.
4. Значения:
   * Поддерживаются числовые значения (целые числа).
   ```bash
   value = 42;
   ```
   * Словари могут быть вложены в качестве значений.
   ```bash
   nested = {
   sub_key = 100;
   }
   ```
5. Константы на этапе трансляции:
   * Объявление константы через оператор ->.
   ```bash
   123 -> myConst
   ```
   * Вычисление значения константы с использованием |имя|.
   ```bash
   result = |myConst|
   ```

## Установка

**Клонируйте репозиторий:**
```bash
git clone <URL репозитория>
cd <директория проекта>>
```

## Использование
Для запуска основного скрипта используйте следующую команду:
```bash
python main.py <путь_к_файлу_xml>
```
Пример использования:
```bash
python main.py example_input.xml
```

## Пример работы
Пример входного файла example_1.xml
```xml
<application>
    <appName>WeatherApp</appName>
    <comment>Это приложение для прогноза погоды</comment>
    <version>1.5</version>
    <developer>OpenAI</developer>
    <features>
        <feature>Real-time weather updates</feature>
        <feature>Weekly forecasts</feature>
    </features>
</application>
```
Вывод программы:

<img width="800" alt="Picture_1" src="https://github.com/user-attachments/assets/9e03072f-b37b-411b-ae55-b9609987a2e7">


Пример входного файла example_2.xml
```xml
<databaseConfig>
    <dbName>testDB</dbName>
    <comment multiline="true">Эта конфигурация предназначена
    для тестовой базы данных</comment>
    <connection>
        <host>localhost</host>
        <port>5432</port>
        <user>admin</user>
        <password>secret</password>
    </connection>
</databaseConfig>
```
Вывод программы:

<img width="800" alt="Picture_1" src="https://github.com/user-attachments/assets/4eb2ac8c-b590-42c5-97ff-ba76b3c5b34b">

Пример входного файла example_3.xml
```xml
<mobileAppConfig>
    <constants>
        <MIN_SUPPORTED_VERSION>1.0</MIN_SUPPORTED_VERSION>
        <MAX_SUPPORTED_VERSION>5.0</MAX_SUPPORTED_VERSION>
        <DEFAULT_THEME>Light</DEFAULT_THEME>
    </constants>
    <appName>MyMobileApp</appName>
    <supportedVersions>
        <minVersion>|MIN_SUPPORTED_VERSION|</minVersion>
        <maxVersion>|MAX_SUPPORTED_VERSION|</maxVersion>
    </supportedVersions>
    <theme>|DEFAULT_THEME|</theme>
    <developerNotes>Проверить совместимость с Android и iOS</developerNotes>
</mobileAppConfig>
```
Вывод программы:

<img width="800" alt="Picture_1" src="https://github.com/user-attachments/assets/00de9396-15ac-4b82-ab5e-6254ed0046e5">

## Тестирование
Для запуска тестов используйте модуль unittest:
```bash
python -m unittest tests.py
```
Пример тестирования:

<img width="800" alt="Picture_1" src="https://github.com/user-attachments/assets/697421e3-3847-492c-bcb3-c5472dc8c850">
