import mysql.connector
mydb =mysql.connector.connect(host="localhost", user="root", passwd="root", database="hospital")
mycursor =mydb.cursor()
sql = "Update patient SET age =139 WHERE name='nikhila'"
mycursor.execute(sql)
mydb.commit()
