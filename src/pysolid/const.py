from pathlib import Path
  
from pysolid.point import Point        

FIRST_POINT = Point(0,0,0)
SECOND_POINT = Point(0.1,0.1,0)



MM_TO_M = 0.001

HEIGHT = 0.01/MM_TO_M
R_CUT_MM = 0.5

PART_NAME = "part"

PATH_TO_SOLID = Path("C:\Program Files\SOLIDWORKS Corp\SOLIDWORKS\SLDWORKS.exe")
PATH_TO_TEMPLATE = Path("C:\ProgramData\SolidWorks\SOLIDWORKS 2021\templates\gost-part.prtdot")
PATH_TO_TABLE = Path.cwd().joinpath("table_data").joinpath("table.xlsx")
SAVE_PATH = Path.cwd().joinpath("details")