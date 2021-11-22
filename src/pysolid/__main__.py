import subprocess
import argparse
from pysolid.const import (
    HEIGHT,
    PATH_TO_SOLID, 
    PATH_TO_TABLE, 
    PART_NAME,
    R_CUT_MM,
    SAVE_PATH,
)
from pysolid.part_maker import PartMaker
from pathlib import Path
from pysolid import __version__

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="PySW")

    parser.add_argument("--path_to_table", 
                        dest="path_to_table", 
                        default=PATH_TO_TABLE, 
                        help="Указать путь к таблице с данными, Если путь не указан, файл по умолчанию берется из папки table_data"
    )
  
    parser.add_argument("--save_path", 
                        dest="save_path",
                        default=SAVE_PATH,
                        help="Указать путь к файлу. Если не указан, по умолчанию это папка Details"
    )
    
    parser.add_argument("--part_name", 
                        dest="part_name", 
                        default=PART_NAME, 
                        help="Указать название детали. По умолчанию \"part\""
    )
    
    parser.add_argument("--export_to_parasolid", 
                        dest="export_to_parasolid",
                        action='store_true',
                        help="Экспортировать ли в parasolid?"
    )
    
    parser.add_argument("--height_of_boss", 
                        dest="height_of_boss",
                        default=HEIGHT,
                        type=float,
                        help="Указать толщину бобышки в мм. По умолчанию 10 мм"
    )
    
    parser.add_argument("--diameter_of_cuts",
                        dest="d_of_cuts",
                        default=R_CUT_MM*2,
                        type=float,
                        help="Указать диаметр отверстий в мм. По умолчанию 1 мм"
    )

    parser.add_argument("--version", 
                        action="version",
                        version="{version}".format(version=__version__)
    )
    
    args = parser.parse_args()
    
    args.path_to_table = Path(args.path_to_table)
    args.save_path = Path(args.save_path)
    
    if Path.exists(args.path_to_table) is False:
        print("Ошибка: Неправильный путь до файла с таблицей")
        exit(0)
    
    if Path.exists(args.save_path) is False:
        print("Ошибка: Неправильный путь до каталога, куда будет сохранятся деталь")
        exit(0)
    
    print("Start of main program")
    
    try:
        swProcess = subprocess.Popen(PATH_TO_SOLID)
    except Exception as ex:
        print(str(ex))
        exit(0)
    
    part = PartMaker(
        path_to_table=args.path_to_table,
        save_path=args.save_path, 
        part_name=args.part_name,
        is_need_export_to_parasolid=args.export_to_parasolid,
        part_height=args.height_of_boss,
        cut_diameter=args.d_of_cuts
    )
    
    part.make_part()
    part.save_part()