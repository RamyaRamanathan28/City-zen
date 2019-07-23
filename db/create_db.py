from db_init import *


mycol = mydb["test"]
mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)




print("collections :",mydb.list_collection_names())

