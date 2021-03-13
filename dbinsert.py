import mysql.connector as b
mydb=b.connect(host="localhost",user="root",password="root",database="hospital")
mycursor=mydb.cursor()
sqlform= "Insert into patient(name, age) values(%s,%s)"
patients =[("nikhila", 192), ("amit", 183),("ankita",200), ]
mycursor.executemany(sqlform, patients)
mydb.commit()
