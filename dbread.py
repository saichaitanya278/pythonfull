import mysql.connector as b
mydb=b.connect(host="localhost",user="root",password="password123")
mycursor=mydb.cursor()
myresult=mycursor.fetcahall()
for row in myresult:
        print(row)