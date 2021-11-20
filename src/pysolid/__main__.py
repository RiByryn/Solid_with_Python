import subprocess
import argparse
from pysolid.const import (
    FIRST_POINT,
    HEIGHT,
    PATH_TO_SOLID, 
    PATH_TO_TABLE, 
    PART_NAME,
    R_CUT_MM,
    SAVE_PATH,
    SECOND_POINT
)
from pysolid.logger import logger
from pysolid.part_maker import PartMaker

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="PySW")

    parser.add_argument("--path_to_table", dest="path_to_table", default=PATH_TO_TABLE)
    parser.add_argument("--save_path", dest="save_path", default=SAVE_PATH)
    parser.add_argument("--part_name", dest="part_name", default=PART_NAME)
    parser.add_argument("--export_to_parasolid", dest="export_to_parasolid", action='store_true')
    
    parser.add_argument("--height_of_boss", dest="height_of_boss", default=HEIGHT, type=float, help="Height in mm")
    parser.add_argument("--diameter_of_cuts", dest="d_of_cuts", default=R_CUT_MM*2, type=float, help="Diameter of cuts in mm")
    
    # parser.add_argument("--help", dest="help")
    # parser.add_argument("--version", dest="version")
    
    args = parser.parse_args()
    
    logger.debug("Start of main program")
    
    try:
        swProcess = subprocess.Popen(PATH_TO_SOLID)
    except Exception as ex:
        logger.error(ex)
        exit(-1)
    
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
    