import mysql.connector as b
mydb=b.connect(host="localhost",user="root",password="root")
if(mydb):
    print("connection successful")
else:
    print("connection unsuccessful")