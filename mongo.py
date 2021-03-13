from pymongo import MongoClient # import mongo client to connect
import pprint
# Creating instance of mongoclient
client = MongoClient()
# Creating database
db = client.klu
student = {"regno": "1099",
"name": "RAM",
"dept": "CSE",
}
# Creating document
students = db.students
# Inserting data
students.insert_one(student)
# Fetching data
pprint.pprint(students.find_one())