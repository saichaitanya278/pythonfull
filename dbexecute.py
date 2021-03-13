import mysql.connector as a
mydb=a.connect(host="localhost",user="root",password="sai",database="hospital")
mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE patient (name VARCHAR(255), age INT(20))")
mycursor.execute("  ")
myresult=mycursor.fetchall()
for tb in mycursor:
    print(tb)