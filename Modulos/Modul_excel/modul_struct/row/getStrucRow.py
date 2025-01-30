import openpyxl

class structRow:
    def __init__(self, urlDirExcel):
        lo_workSheet = openpyxl.load_workbook(urlDirExcel)
        lv_idUser = 0
    def createRow(self):
        return