from pymongo import MongoClient 
import pprint

pp = pprint.PrettyPrinter(indent=4)
client = MongoClient("mongodb://localhost:27017/")
mydatabase = client['teste']
mycol = mydatabase['col']

cont = 0
#apresenta valores
for x in mycol.find():
  #apresenta todos
  pp.pprint(x)
  if x["request_method"] == "POST":
    cont+=1
  #apresenta apenas id
  pp.pprint(x["_id"])
#resultado da quantidade de resquisições do método POST
print(cont)
