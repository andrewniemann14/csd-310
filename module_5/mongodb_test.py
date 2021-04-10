# Andrew Niemann, 4/10/21, Module 5.2
# connects to MongoDB database and displays collections

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.sfjid.mongodb.net/pytech"
client = MongoClient(url)
db = client.pytech

print("-- Pytech Collection List --")
print(db.list_collection_names())

input("\n\n\tEnd of program, press any key to exit...")
