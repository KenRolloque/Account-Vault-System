import mysql.connector as mysql

def connection():
	connect = mysql.connect(
		host = "localhost",
		user = "root",
		password = "",
		database = "accountstorage",
		port = "3306"
	)

	return connect