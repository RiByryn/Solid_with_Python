from pathlib import Path
from win32com import client as sw_client
from pandas import read_excel

from pysolid.logger import logger
from pysolid.boss import Boss
from pysolid.cut import Cut
from pysolid.const import (
    PATH_TO_TEMPLATE,
    FIRST_POINT,
    SAVE_PATH,
    SECOND_POINT,
    HEIGHT,
)


class PartMaker():
    
    def __init__(self, 
        path_to_table: str, 
        save_path:str, 
        part_name: str, 
        is_need_export_to_parasolid:bool,
        part_height: float,
        cut_diameter: float
    ) -> None:
        # D:\code\Solid_with_Python\table_data\table.xlsx
        try:
            self.data = read_excel(str(Path(path_to_table)))
        except Exception as ex:
            logger.exception(ex)
            exit(-1)
        
        self.save_path = str(Path(save_path).joinpath(part_name)) + ".sldprt"
        
        if is_need_export_to_parasolid is True:
            self.save_path_parasolid = str(Path(save_path).joinpath(part_name)) + ".x_t"
        else:
            self.save_path_parasolid = None
        try:
            self.swApp = sw_client.Dispatch("SldWorks.Application")
        except Exception as e:
            logger.error("Can't dispatch SldWorks.Application")
            exit(0)
        
        self.swApp.newpart
        swSheetWidth = 0    
        swSheetHeight = 0    
        self.swApp.NewDocument(str(PATH_TO_TEMPLATE), 0, swSheetWidth, swSheetHeight)

        try:
            self.part = self.swApp.ActiveDoc
        except Exception as e:
            logger.error("Нет активного документа в SW. Создайте новый документ")
            exit(-1)
            
        self.height = part_height
        self.cut_radius = cut_diameter/2
    
    def make_part(self) -> None:
        
        new_boss = Boss(
            p1=FIRST_POINT, 
            p2=SECOND_POINT, 
            h=self.height,
            part=self.part
            )
        new_boss.create_boss()
        
        new_cut = Cut(part=self.part, cuts=self.data, radius=self.cut_radius, height=self.height)
        new_cut.create_cuts()

    def save_part(self) -> None:

        save_status = self.part.SaveAs3(self.save_path, 0, 0)
        print(save_status)

        if save_status != 0:
            logger.error("Проблема с адресом файла")
        
        if self.save_path_parasolid is not None:        
            save_status_parasolid = self.part.SaveAs3(self.save_path_parasolid, 0, 2)
            if save_status_parasolid != 0:
                logger.error("Проблема с адресом файла parasolid")








