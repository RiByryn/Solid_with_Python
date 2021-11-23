from win32com import client as sw_client

from pysolid.const import MM_TO_M
from pysolid.point import Point

class Boss():
    def __init__(self, p1: Point, p2: Point, h: float, part: sw_client.CDispatch) -> None:
        self.point1 = p1
        self.point2 = p2
        self.height = h
        self.part = part
    
    def create_boss(self) -> None:
        try:
            self.part.SketchManager.AddToDB = True
            self.part.SketchManager.CreateCornerRectangle(
                self.point1.x, 
                self.point1.y, 
                self.point1.z, 
                self.point2.x, 
                self.point2.y, 
                self.point2.z
            )
            self.part.SketchManager.AddToDB = False

            
            self.part.FeatureManager.FeatureExtrusion2(
                True, # SD: True for single ended, false for double ended
                False, 
                False, 
                0, 
                0,
                self.height*MM_TO_M,
                self.height*MM_TO_M,
                False, 
                False,
                False,
                False,
                0,
                0,
                False,
                False,
                False,
                False,
                True,
                True,
                True,
                0,
                0,
                False
            )
        except Exception as ex:
            print("Ошибка: Не можем создать элемент бобышка")
            exit(0)


