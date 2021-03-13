// from pymongo import MongoClient
// import pprint
// client =MongoClient()
// db=client.klu
// student={"regno": "1099","name":"RAM"}
students.insert_many(student)
for i in student.insert():
    print()