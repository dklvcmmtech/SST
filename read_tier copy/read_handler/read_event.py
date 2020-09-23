import mysql.connector
import connect_db
from connect_db import MySqlConn
from connect_db1 import MySqlConn_1

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="db1"
)

#print(db)

current_cursor = db.cursor()
current_cursor.execute("SHOW TABLES")
for d in current_cursor:
	print(d)

mysqlConnObj = MySqlConn()
mysqlConnector = mysqlConnObj.mysql_conn
cursor = mysqlConnector.cursor()
cursor.execute("SHOW TABLES")
print(cursor.fetchone())

mysqlConnObj = MySqlConn_1()
mysqlConnector = mysqlConnObj.mysql_conn
cursor1 = mysqlConnector.cursor()
cursor1.execute("SHOW TABLES;")
for d in cursor1:
	print(d)
