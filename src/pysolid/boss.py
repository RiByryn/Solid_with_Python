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
                True,                # SD: True for single ended, false for double ended
                False,               #Flip: True to flip side to cut
                False,               #Dir: True to flip the direction to extrude
                0,                   #T1: Termination type for first end as defined in swEndConditions_e
                0,                   #T2: Termination type for second end as defined in swEndConditions_e
                self.height*MM_TO_M, #D1: Depth of extrusion for first end in meters
                self.height*MM_TO_M, #D2: Depth of extrusion for second end in meters
                False,               #Dchk1: True allows draft angle in first direction, false does not allow drafting
                False,               #Dchk2: True allows draft angle in second direction, false does not allow drafting
                False,               #Ddir1: True for first draft angle to be inward, false to be outward
                False,               #Ddir2: True for second draft angle to be inward, false to be outward
                0,                   #Dang1: Draft angle for first end
                0,                   #Dang2: Draft angle for second end
                False,               #OffsetReverse1: If you chose to offset the first end condition from another face or plane, then True specifies offset in direction away from the sketch, false specifies offset from the face or plane in direction toward the sketch
                False,               #OffsetReverse2: If you chose to offset the second end condition from another face or plane, then True specifies offset in direction away from the sketch, false specifies offset from the face or plane in direction toward the sketch
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


