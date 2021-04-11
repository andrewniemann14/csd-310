# Andrew Niemann, 4/10/21, Module 5.3
# inserts a few documents into the "students" collection

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.sfjid.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech

thorin = {
  "student_id": 1007,
  "first_name": "Thorin",
  "last_name": "Oakenshield",
  "enrollments": [
    {
      "term": 2,
      "gpa": 4.0,
      "start_date": 20210315,
      "end_date": 20210523,
      "courses": [
        {
          "course_id": "CSD310",
          "description": "Database",
          "instructor": "Chris Soriano",
          "grade": "A",
        },
        {
          "course_id": "CSD320",
          "description": "Java",
          "instructor": "Darrel Payne",
          "grade": "A",
        }
      ]
    }
  ]
}

bilbo = {
  "student_id": 1008,
  "first_name": "Bilbo",
  "last_name": "Baggins",
  "enrollments": [
    {
      "term": 2,
      "gpa": 4.0,
      "start_date": 20210315,
      "end_date": 20210523,
      "courses": [
        {
          "course_id": "CSD310",
          "description": "Database",
          "instructor": "Chris Soriano",
          "grade": "A",
        },
        {
          "course_id": "CSD320",
          "description": "Java",
          "instructor": "Darrel Payne",
          "grade": "A",
        }
      ]
    }
  ]
}

frodo = {
  "student_id": 1009,
  "first_name": "Nasty",
  "last_name": "Hobbitses",
  "enrollments": [
    {
      "term": 2,
      "gpa": 4.0,
      "start_date": 20210315,
      "end_date": 20210523,
      "courses": [
        {
          "course_id": "CSD310",
          "description": "Database",
          "instructor": "Chris Soriano",
          "grade": "A",
        },
        {
          "course_id": "CSD320",
          "description": "Java",
          "instructor": "Darrel Payne",
          "grade": "A",
        }
      ]
    }
  ]
}

db.students.delete_many({})
id_1007 = db.students.insert_one(thorin).inserted_id
id_1008 = db.students.insert_one(bilbo).inserted_id
id_1009 = db.students.insert_one(frodo).inserted_id

print("-- INSERT STATEMENTS --")
print(f"Inserted student record Thorin Oakenshield into the students collection with document id {id_1007}")
print(f"Inserted student record Bilbo Baggins into the students collection with document id {id_1008}")
print(f"Inserted student record Nasty Hobbitses into the students collection with document id {id_1009}")
input("\nEnd of program, press any key to exit... ")