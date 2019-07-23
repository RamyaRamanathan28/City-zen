from db_init import *

def createNewUser(username,password,city,area,voter_id,created_by_Admin=False,designation="Citizen",department=None):
	mydict = { "user_id": str(int(last_inserted_user_id)+1),
			"name":username,
			"password":password,
			"city":city,
			"area":area,
			"voter_id":voter_id,
			"isGovtEmp":created_by_Admin,  #If user was created by admin, he is a govt employee
			"designation":designation,
			"department":department,
			"affect_me_posts":[],
			"support_posts":[],
			"no_support_posts":[]}
	x = UsersCol.insert_one(mydict)
	print("Created new user : ",x)


def getUserId(username):
	myquery = { "name": username}
	result=list(UsersCol.find(myquery))
	#print(result)
	if len(result)>0:
		return result[0]["user_id"]
	return False

def userIsGovtEmp(username):
	myquery = { "name": username,"isGovtEmp":True}
	result=list(UsersCol.find(myquery))
	#print(result)
	if len(result)>0:
		return True
	return False

def validUserPassword(username,entered_password):
	myquery = { "name": username,"password":entered_password}
	result=list(UsersCol.find(myquery))
	print(len(result))
	if len(result)>0:
		return True
	return False

def getUserData(username):
	myquery = { "name": username}
	result=list(UsersCol.find(myquery))
	return result


# createNewUser("Person1","password","Bangalore","ABC","VOTERID",created_by_Admin=False,designation="Citizen",department=None)

# a

# print(validUserPassword("Sruthi","password"))
# print(validUserPassword("Sruthi","ABC"))