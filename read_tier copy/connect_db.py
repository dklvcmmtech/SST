import mysql.connector as connector


class MySqlConn:

	def __init__(self):

		config = {
			"host":"localhost",
			"user":"root",
			"password":"root",
			"database":"db1"
		}

		self.mysql_conn = connector.connect(**config)
		

	def __del__(self):
		self.mysql_conn.close()




def connect_db(*argc):

	db = mysql.connector.connect(
  		host="localhost",
  		user="root",
  		password="root",
  		database="db1"
	)

	#current_cursor = 
	
	return db.cursor()


