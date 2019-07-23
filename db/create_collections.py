from db_init import *
import datetime





mycol = mydb["Users"]
mycol.drop()
mydict = { "user_id": "0",
			"name":"Test",
			"password":"ABC",
			"city":"Bangalore",
			"area":"Bellandur",
			"voter_id":"ABC",
			"isGovtEmp":False,
			"designation":"Citizen",
			"department":None,
			"affect_me_posts":[],
			"support_posts":[],
			"no_support_posts":[]}
x = mycol.insert_one(mydict)
print("collections :",mydb.list_collection_names())

for x in mycol.find():
	print(x)


mycol = mydb["Posts"]
mycol.drop()
mydict = { "post_id":0,
			"user_id": "0",
			"title":"Test",
			"text":"This is a test post",
			"keywords":["test1","test2"],
			"categories":[],
			"creation_time":datetime.datetime.utcnow(),
			"status":"Posted",
			"affects_me_votes":0,
			"support_votes":0,
			"no_support_votes":0,
			"image":None,
			"comments":[],
			"isOffAnn":False}
x = mycol.insert_one(mydict)
print("collections :",mydb.list_collection_names())

for x in mycol.find():
	print(x)


mycol = mydb["Comments"]
mycol.drop()
mydict = { "comment_id":0,
			"post_id":0,
			"user_id": 0,
			"text":"This is a test post",
			}
x = mycol.insert_one(mydict)
print("collections :",mydb.list_collection_names())

for x in mycol.find():
	print(x)


