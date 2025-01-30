from main import Main_process;
from Modulos.Modul_excel.modul_read.ClassRead import classRead
lo_init = Main_process()

lo_readExcel = classRead("C:/Users/Federico/Desktop/proyecto_gestion_ex/archi_excel", "Financial_Sample.xlsx")
print("prueba")
lo_readExcel.readExcel()
"""lo_init.creat_vist()"""