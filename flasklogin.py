import mysql.connector as b
mydb=b.connect(host="localhost",user="root",password="root",database="login")
mycursor=mydb.cursor()
#mycursor.execute("create Database Login")
mycursor.execute("Create table Account(id int(11) NOT NULL AUTO_INCREMENT,username varchar(50),password varchar(100),email varchar(20),PRIMARY KEY(id))")