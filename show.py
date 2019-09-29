from pymongo import MongoClient 

client = MongoClient("mongodb://localhost:27017/")
mydatabase = client['teste']
mycol = mydatabase['col']

for x in mycol.find({},{ "user_id": 0 }):
  print(x)