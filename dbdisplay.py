import mysql.connector as a
mydb=a.connect(host="localhost",user="root",password="root")
mycursor=mydb.cursor()
#mycursor.execute("Create Database Hospital")
mycursor.execute("show databases")
for db in mycursor:
    print(db)