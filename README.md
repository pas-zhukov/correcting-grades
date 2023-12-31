# Correcting Grades Scripts

---

Скрипт для исправления оценок, замечаний и похвал учителей на сайте электронного дневника.

## Введение

Скрипт предназначен для работы с электронным дневником на базе Django, уже развёрнутым и запущенным на сервере. 
При желании, Вы можете развернуть такой сервер локально на своём компьютере, исходный код дневника - [ссылка](https://github.com/devmanorg/e-diary). В таком случае Вам также понадобится файл БД школы.

## Установка

1. Перейдите в консоли в папку, где располагается приложение сайта электронного дневника.
2. Если ввести в терминал команду `ls`, то среди отобразившихся файлов будет `manage.py`.
3. Скачайте скрипт командой:
```shell
git clone https://github.com/pas-zhukov/correcting-grades.git
```

## Начало работы

1. В консоли прописать команду:
```shell
python manage.py shell
```
2. Откроется консоль Python. Теперь необходимо сохранить в переменную свою карточку из БД.
Для этого последовательно вводим следующие команды:
```python
from scripts import *
```
```python
schoolkid = select_schoolkid("<Ваше ФИО>")
```
_ФИО может быть неполным, например, без отчества: "Фролов Иван". Однако, если найдется несколько учеников с такими Фамилией и отчеством, придётся уточнить и Отчество._
3. Если всё было сделано правильно, программа выдаст такого вида сообщение:
```
Выбран ученик 6А класса Фролов Иван Игоревич.
```

## Исправление оценок

Для исправления оценок необходимо прописать следующую команду:
```python
fix_marks(schoolkid)
```
После этого все плохие оценки будут исправлены на пятёрки.

## Удаление замечаний учителей

Чтобы избавиться от навязчивых замечаний от учителей, используйте следующую команду:
```python
remove_chastisements(schoolkid)
```

## Добавление похвалы от учителей

Чтобы добавить похвальный комментарий от учителя по определённому предмету, подойдет такая команда:
```python
create_commendation(schoolkid, "<Название предмета>")
```

## Цель проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте Devman.