import mysql.connector

import mysql.connector as connector


class MySqlConn_1:

    def __init__(self):
        db = mysql.connector.connect(host="localhost",user="root",password="root",database="db1")
        self.mysql_conn = db
		

    def __del__(self):
        self.mysql_conn.close()




