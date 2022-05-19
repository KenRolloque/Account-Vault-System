import mysql.connector as mysql

def connection():
	connect = mysql.connect(
		host = "sql6.freemysqlhosting.net",
		user = "sql6493637",
		password = "KUWrYfSEsz",
		database = "sql6493637",
		port = "3306"
	)

	return connect