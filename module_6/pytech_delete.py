# Andrew Niemann, 4/15/21, Module 6.3
# inserts and then deletes one document

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.sfjid.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech

# print all student records
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
students = db.students.find({})
for student in students:
  print("Student ID: " + str(student["student_id"]))
  print("First name: " + student["first_name"])
  print("Last name: " + student["last_name"])
  print()

gandalf = {
  "student_id": 1010,
  "first_name": "Gandalf",
  "last_name": "Gray",
}

# insert the 1010 document
id_1010 = db.students.insert_one(gandalf).inserted_id
print("-- INSERT STATEMENTS --")
print(f"Inserted student record Gandalf the Gray into the students collection with document id {id_1010}\n")

# print 1010's record
print("-- DISPLAYING STUDENT DOCUMENT 1010 --")
student = db.students.find_one({"student_id": 1010})
print("Student ID: " + str(student["student_id"]))
print("First name: " + student["first_name"])
print("Last name: " + student["last_name"])
print()

# delete the 1010 record
db.students.delete_one({"student_id": 1010})
print("-- RECORD DELETED - FLY YOU FOOLS --\n")

# print all student records
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
students = db.students.find({})
for student in students:
  print("Student ID: " + str(student["student_id"]))
  print("First name: " + student["first_name"])
  print("Last name: " + student["last_name"])
  print()

input("\nEnd of program, press Enter to continue...")
