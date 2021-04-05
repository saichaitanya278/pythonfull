import json
from datetime import date

li = {
    "Result": {
        "Students": [
            {
                "Name": "Admin",
                "Roll Number": "123456789",
                "Section": "A",
                "Date": str(date.today())
            },
            {
                "Name": "Root",
                "Roll Number": "987654321",
                "Section": "C",
                "Date": str(date.today())
            }
        ]
    }
}

new_json = json.dumps(li)

f = open("new_json.json", "w+")
f.write(new_json)
f.close()
print(type(new_json))
