# Solid with Python
Программа для автоматического создания детали в SolidWorks.

## Установка

Установить солид.

Для разработки:
Окружение:
'conda env create -f .\requirements\conda-env.yaml'

Для использования:
'pip install https://github.com/RiByryn/Solid_with_Python'


## Что делать?

1. Создать файл table.xlsx с координатами отверстий в формате: 
| x           | y           |
| ----------- | ----------- |
| 0           | 3           |
| 1,2         | 33,6        |
| 8,5         | 99          |


2. Создать каталог details 
3. Запустить модуль командой:
'python -m pysolid c ключами запуска.'
Ключи запуска указаны ниже.
3. Получить файл детали в каталоге details.

Пример запуска программы:

'python -m pysolid --path_to_table table.xlsx --save_path ./details --part_name test_part --export_to_parasolid --height_of_boss 9 --diameter_of_cuts 2'

В этом примере берётся файл таблицы из каталога, откуда запускается модуль и сохраняется в каталог details.

## CLI
--path_to_table - указать путь к таблице с данными.

--save_path - указать путь к файлу.

--part_name - указать название детали. По умолчанию "part"

--export_to_parasolid - экспортировать ли в parasolid? По умолчанию "Да"

--height_of_boss - указать толщину бобышки. По умолчанию 10 мм

--diameter_of_cuts - указать диаметр отверстий. По умолчанию 1 мм

--version - вывести номер версии

--help - вывести Справку
