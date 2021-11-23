from win32com import client as sw_client
from pandas.core.frame import DataFrame

from pysolid.const import (
    MM_TO_M,
    SECOND_POINT,
)
from pysolid.point import Point


class Cut():
    
    def __init__(self, part: sw_client.CDispatch, cuts:DataFrame, radius: float, height: float) -> None:
        self.part = part
        self.list_of_cuts = cuts
        self.radius = radius
        self.height = height
        
        
    def create_cuts(self) -> None:
        
        sketch = self.part.SketchManager
        
        for i, row in self.list_of_cuts.iterrows():
            
            cut_point_center = Point(row.x * MM_TO_M, row.y * MM_TO_M, 0)
            cut_point_on_circle = Point(
                row.x * MM_TO_M + MM_TO_M * self.radius, 
                row.y * MM_TO_M,
                0
            )
            
            if cut_point_center.x == self.radius*MM_TO_M or cut_point_center.y == self.radius*MM_TO_M or SECOND_POINT.x - cut_point_center.x == self.radius*MM_TO_M or SECOND_POINT.y - cut_point_center.y == self.radius*MM_TO_M:
                print("С данными параметрами отверстия сделать невозможно:")   
                print("Получится бесконечно тонкая линия")   
                print("Пожалуйста, измените параметры")
                continue         
            
            self.part.SketchManager.AddToDB = True
            skSegment = sketch.CreateCircle(
                cut_point_center.x, 
                cut_point_center.y, 
                cut_point_center.z, 
                cut_point_on_circle.x,
                cut_point_on_circle.y,
                cut_point_on_circle.z
            )
            self.part.SketchManager.AddToDB = False
                
        myFeature = self.part.FeatureManager.FeatureCut4(
            True, 
            False, 
            True, 
            0, 
            0, 
            self.height * MM_TO_M, 
            self.height * MM_TO_M, 
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
            False, 
            True, 
            True, 
            True, 
            True, 
            False, 
            0, 
            0, 
            False, 
            False
        )
        
        
    
