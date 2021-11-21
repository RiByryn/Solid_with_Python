# Solid with Python
Программа для автоматического создания детали в SolidWorks.

## Установка

Окружение:
'conda env create -f .\requirements\conda-env.yaml'

Было бы неплохо ещё и солид установить.

## Что делать?

1. Положить в файл table.xlsx в каталоге table_data координаты отверстий.
2. Запустить в окне Debug конфигурацию "Make part".
3. Получить файл детали в каталоге output.


## CLI
--path_to_table - указать путь к таблице с данными

--save_path - указать путь к файлу

--part_name - указать название детали

--export_to_parasolid - экспортировать ли в parasolid?

--height_of_boss - указать толщину бобышки

--diameter_of_cuts" - указать диаметр отверстий
