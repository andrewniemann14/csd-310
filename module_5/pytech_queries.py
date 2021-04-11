# Andrew Niemann, 4/10/21, Module 5.3
# queries and displays information from the "students" collection

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.sfjid.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
students = db.students.find({})
for student in students:
  print("Student ID: " + str(student["student_id"]))
  print("First name: " + student["first_name"])
  print("Last name: " + student["last_name"])
  print()

print("\n-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
student = db.students.find_one({"student_id":1009})
print("Student ID: " + str(student["student_id"]))
print("First name: " + student["first_name"])
print("Last name: " + student["last_name"])
print()

input("\nEnd of program, press any key to continue...")