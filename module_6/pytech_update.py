# Andrew Niemann, 4/15/21, Module 6.2
# updates one document

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

# change 1007's last name
update = db.students.update_one({"student_id": 1007}, {"$set": {"last_name": "Mapleshield"}})
print("-- STUDENT DOCUMENT 1007 UPDATED --\n")

# print 1007's record
print("-- DISPLAYING STUDENT DOCUMENT 1007 --")
student = db.students.find_one({"student_id": 1007})
print("Student ID: " + str(student["student_id"]))
print("First name: " + student["first_name"])
print("Last name: " + student["last_name"])
print()

input("\nEnd of program, press Enter to continue...")
