#Оставлено здесь для позора и истории

import subprocess

from win32com import client as sw_client
from pandas import read_excel
from pathlib import Path

from pysolid.logger import logger
from pysolid.const import PATH_TO_SOLID

swProcess = subprocess.Popen(PATH_TO_SOLID)
try:
    data = read_excel("table_data\\table.xlsx")
except Exception as e:
    logger.exception(e)
    exit(-1)

try:
    swApp = sw_client.Dispatch("SldWorks.Application")
except Exception as e:
    logger.error("Can't dispatch SldWorks.Application")
    exit(0)

swApp.newpart

swSheetWidth = 0    
swSheetHeight = 0    
swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2021\templates\\gost-part.prtdot", 0, swSheetWidth, swSheetHeight)


try:
    Part = swApp.ActiveDoc
except Exception as e:
    logger.error("Нет активного документа в SW. Создайте новый документ")
    exit(-1)

try:
    vSkLines = Part.SketchManager.CreateCornerRectangle(0, 0, 0, 0.1, 0.1, 0)
    myFeature = Part.FeatureManager.FeatureExtrusion2(True, False, False, 0, 0, 0.01, 0.01, False, False, False, False, 0, 0,
        False, False, False, False, True, True, True, 0, 0, False)
except Exception as e:
    logger.error("Не можем создать элемент бобышка")
    exit(-1)

for i, row in data.iterrows():
    try:
        skSegment = Part.SketchManager.CreateCircle(row.x*0.001, row.y*0.001, 0, row.x*0.001+0.005, row.y*0.001, 0)
        myFeature = Part.FeatureManager.FeatureCut4(True, False, True, 0, 0, 0.01, 0.01, False, False, False, False, 0, 0, False, False, False, False, False, True, True, True, True, False, 0, 0, False, False)
    except Exception as e:
        logger.error(f"{row.x}, {row.y}")
        exit(-1)

name = "part2"    
save_Path = Path.cwd().joinpath("details").joinpath(f"{name}.sldprt")




longstatus = Part.SaveAs3(str(save_Path), 0, 0)
print(longstatus)

if longstatus != 0:
    logger.error("Проблема с адресом файла")