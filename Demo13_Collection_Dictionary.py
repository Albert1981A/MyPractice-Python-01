student = {"name": "Avi",
            "age": 30,
            "grades": [90,80,70,95],
            "address": {
                "city": "Bat-Yam",
                "street": {
                    "name": "Josef-Tal",
                    "number": 3
                }
            }
}

# Get student name
print('Student name:', student["name"])

# Get student street name:
print('Student Street name:', student["address"]["street"]["name"])

# get student second grade:
print('Student second grade is:', student["grades"][1])

