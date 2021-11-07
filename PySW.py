import win32com.client
from pandas import read_excel
from logger import logger
import os

try:
    data = read_excel("table.xlsx")
except Exception as e:
    logger.exception(e)
    exit(-1)

try:
    swApp = win32com.client.Dispatch("SldWorks.Application.28" )
except Exception as e:
    logger.error("Can't dispatch SldWorks.Application")
    exit(-1)

try:
    Part = swApp.ActiveDoc
except Exception as e:
    logger.error("Нет активного документа в SW. Создайте новый документ")
    exit(-1)

try:
    vSkLines = Part.SketchManager.CreateCornerRectangle(0, 0, 0, 0.1, 0.1, 0)
    myFeature = Part.FeatureManager.FeatureExtrusion2(True, False, False, 0, 0, 0.01, 0.01, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02,
        False, False, False, False, True, True, True, 0, 0, False)
except Exception as e:
    logger.error("Не можем создать элемент бобышка")
    exit(-1)

for i, row in data.iterrows():
    try:
        skSegment = Part.SketchManager.CreateCircle(row.x*0.001, row.y*0.001, 0, row.x*0.001+0.005, row.y*0.001, 0)
        myFeature = Part.FeatureManager.FeatureCut4(True, False, True, 0, 0, 0.01, 0.01, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, False, True, True, True, True, False, 0, 0, False, False)
    except Exception as e:
        logger.error(f"{row.x}, {row.y}")
        exit(-1)
    
file_path = os.path.realpath(__file__).rsplit('\\', 1)[0]
longstatus = Part.SaveAs3(f"{file_path}/1details/detail.sldprt", 0, 0)
print(longstatus)

if longstatus != 0:
    logger.error("Проблема с адресом файла")