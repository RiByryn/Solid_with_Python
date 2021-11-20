from win32com import client as sw_client
from pandas.core import frame
from pandas.core.frame import DataFrame

from pysolid import logger
from pysolid.const import (
    MM_TO_M,
    R_CUT_MM,
    HEIGHT
)
from pysolid.point import Point


class Cut():
    
    def __init__(self, part: sw_client.CDispatch, cuts:DataFrame, radius: float, height: float) -> None:
        self.part = part
        self.list_of_cuts = cuts
        self.radius = radius
        self.height = height
        
        
    def create_cuts(self) -> None:
        
        for i, row in self.list_of_cuts.iterrows():
            cut_point_center = Point(row.x * MM_TO_M, row.y * MM_TO_M, 0)
            cut_point_on_circle = Point(
                row.x * MM_TO_M + MM_TO_M * self.radius, 
                row.y * MM_TO_M,
                0
            )
            
            try:
                skSegment = self.part.SketchManager.CreateCircle(
                    cut_point_center.x, 
                    cut_point_center.y, 
                    cut_point_center.z, 
                    cut_point_on_circle.x,
                    cut_point_on_circle.y,
                    cut_point_on_circle.z
                )
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
            except Exception as ex:
                logger.error(f"{cut_point_center.x}, {cut_point_center.y}")
                exit(-1)
        
    
