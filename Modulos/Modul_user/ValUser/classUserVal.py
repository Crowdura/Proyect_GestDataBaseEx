from ...Conect_database.connect_mysql import lo_mysqlConect
import os
path = "//"
os.chdir(path)
print(os.getcwd())
#%%
import numpy as np
from numpy import savez_compressed

class classUserVal:
    def __init__(self, id_user, password):
        self.lv_passWord = password
        self.lv_status = False
        return
    
    def valUser(self):
        
        return
    
    def valPassword(self):
        return
    
    def valFinger(self):
        return