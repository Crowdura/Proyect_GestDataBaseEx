import pymysql

class conexMysq:
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        return
    def conexMysql(self):
        try:
            self.conex = pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db)
            print("Conexión exito en a la base de datos : ",self.db )
        except pymysql.DatabaseError:
            print("Error con la conexión descript")
        return

    def consultCamMysql(self, nameTab):
        lo_cur = self.conex.cursor()

        lo_cur.execute(f"SHOW COLUMNS from {nameTab}")

        lv_dataCol = lo_cur.fetchall() 

        lo_cur.close()

        return lv_dataCol
    
    def contrucBaseExcel(self, namBase):
        lo_cur = self.conex.cursor()

        lo_cur.execute(f"CREATE BASE {namBase}")
        
        lo_cur.close()
        return
    
    def contrucTablesExcel(self, namTabs):
        lo_cur = self.conex.cursor()
        for i in namTabs:
            lo_cur.execute(f"CREATE TABLE {i}")
        lo_cur.close()
        return

try:
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='12345678',
        db='base_excel'
    )

    cur = conn.cursor()

    cur.execute(f"SHOW COLUMNS FROM userbasic")

    lv_data = cur.fetchall()

    print(lv_data)

    for row in lv_data:
        print(row)

    cur.close()

    print("Entro_1")
except pymysql.DataError:
    print("Error")