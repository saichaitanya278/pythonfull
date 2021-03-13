from pymongo import MongoClient # import mongo client to connect
import pprint
# Creating instance of mongoclient
client = MongoClient()
# Creating database
db = client.klu
student = [{"regno": "10",
"name": "sham",
"dept": "CSE"
},{"regno":"12",
"name": "zoro",
"dept":"CSE"},{"regno":"11",
"name": "soot",
"dept":"CSE"}]

students = db.students
# Inserting data
students.insert_many(student)
# Fetching data
#pprint.pprint(students.find_one())
for i in students.find():
    pprint.pprint(i)