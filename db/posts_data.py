from db_init import *
from user_data import getUserId

def createNewPost(username,title,text,keywords,categories=[], image=None,isOffAnn=False,):
	user_id=getUserId(username)
	print("Creating new post for ",user_id," username ",username)
	if(user_id):
		mydict = { "post_id":str(int(last_inserted_post_id)+1),
				"user_id": user_id,
				"title":title,
				"text":text,
				"keywords":keywords,
				"categories":categories,
				"creation_time":datetime.datetime.utcnow(),
				"status":"Posted",
				"affects_me_votes":0,
				"support_votes":0,
				"no_support_votes":0,
				"image":image,
				"comments":[],
				"isOffAnn":isOffAnn}
		x = PostsCol.insert_one(mydict)
		print("Created new post : ",x)


def voteAffectsMe(post_id,username):

	myquery = { "post_id": post_id}	
	post=list(PostsCol.find(myquery))[0]
	affects_me_votes=post["affects_me_votes"]
	newvalues = { "$set": { "affects_me_votes": affects_me_votes+1} }
	PostsCol.update_one(myquery, newvalues)

	user_id=getUserId(username)
	myquery = {"user_id":user_id}
	user=list(UsersCol.find(myquery))[0]
	#print(user)
	affect_me_posts=user["affect_me_posts"]
	newvalues = { "$set": { "affect_me_posts": affect_me_posts+[post_id]}}
	UsersCol.update_one(myquery, newvalues)


def voteSupport(post_id,username):

	post_id=post_id.encode('ascii','ignore')
	myquery = { "post_id": str(post_id)}	
	post=list(PostsCol.find(myquery))[0]
	affects_me_votes=post["support_votes"]
	newvalues = { "$set": { "support_votes": affects_me_votes+1} }
	PostsCol.update_one(myquery, newvalues)

	user_id=getUserId(username)
	myquery = {"user_id":user_id}
	print(user_id,type(user_id))
	user=list(UsersCol.find(myquery))[0]
	print(user)
	affect_me_posts=user["support_posts"]
	newvalues = { "$set": { "support_posts": affect_me_posts+[post_id]}}
	UsersCol.update_one(myquery, newvalues)

def downvoteSupport(post_id,username):

	myquery = { "post_id": post_id}	
	post=list(PostsCol.find(myquery))[0]
	affects_me_votes=post["no_support_votes"]
	newvalues = { "$set": { "no_support_votes": affects_me_votes+1} }
	PostsCol.update_one(myquery, newvalues)

	user_id=getUserId(username)
	myquery = {"user_id":user_id}
	user=list(UsersCol.find(myquery))[0]
	#print(user)
	affect_me_posts=user["no_support_posts"]
	newvalues = { "$set": { "no_support_posts": affect_me_posts+[post_id]}}
	UsersCol.update_one(myquery, newvalues)

def getAllPosts():
	return list(PostsCol.find())

def getPost(post_id):
	post_id=post_id.encode('ascii','ignore')
	print(post_id,type(post_id))
	myquery = { "post_id": str(post_id)}	
	post=list(PostsCol.find(myquery))
	print(post)
	if len(post)>0:
		return post[0]


def getPostForUser(username):
	user_id=getUserId(username)
	myquery = { "user_id": str(user_id)}	
	post=list(PostsCol.find(myquery))
	print(post)
	return post

# createNewPost("Person1","NEW ISSUE","OMG",["Sewage","Dump"])

# a

#voteAffectsMe("1","1")