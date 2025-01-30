import openpyxl
import openpyxl.utils as tols
from ....ConfScreeen.udi.colorScreen import colorScreen

class classCreat:
    def __init__(self, urlExcel):
        self.urlExc = urlExcel
        return
    def createCell(self):
        self.lv_cellCre = tols.cell.cols_from_range
        return
    def createRow(self):
        self.lv_rowCre = tols.rows_from_range 
        return
    def colorCol(self):
        self.lo_color = colorScreen.confColor
        return