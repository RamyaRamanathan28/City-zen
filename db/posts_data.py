from db_init import *
from user_data import getUserId

def createNewPost(username,title,text,keywords,image=None,isOffAnn=False):
	user_id=getUserId(username)
	if(user_id):
		mydict = { "post_id":str(int(last_inserted_post_id)+1),
				"user_id": user_id,
				"title":title,
				"text":text,
				"keywords":keywords,
				"categories":[],
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


def voteAffectsMe(post_id,user_id):

	myquery = { "post_id": post_id}	
	post=list(PostsCol.find(myquery))[0]
	affects_me_votes=post["affects_me_votes"]
	newvalues = { "$set": { "affects_me_votes": affects_me_votes+1} }
	PostsCol.update_one(myquery, newvalues)


	myquery = {"user_id":user_id}
	user=list(UsersCol.find(myquery))[0]
	#print(user)
	affect_me_posts=user["affect_me_posts"]
	newvalues = { "$set": { "affect_me_posts": affect_me_posts+[post_id]}}
	UsersCol.update_one(myquery, newvalues)


def voteSupport(post_id,user_id):

	myquery = { "post_id": post_id}	
	post=list(PostsCol.find(myquery))[0]
	affects_me_votes=post["support_votes"]
	newvalues = { "$set": { "support_votes": affects_me_votes+1} }
	PostsCol.update_one(myquery, newvalues)


	myquery = {"user_id":user_id}
	user=list(UsersCol.find(myquery))[0]
	#print(user)
	affect_me_posts=user["support_posts"]
	newvalues = { "$set": { "support_posts": affect_me_posts+[post_id]}}
	UsersCol.update_one(myquery, newvalues)

def downvoteSupport(post_id,user_id):

	myquery = { "post_id": post_id}	
	post=list(PostsCol.find(myquery))[0]
	affects_me_votes=post["no_support_votes"]
	newvalues = { "$set": { "no_support_votes": affects_me_votes+1} }
	PostsCol.update_one(myquery, newvalues)


	myquery = {"user_id":user_id}
	user=list(UsersCol.find(myquery))[0]
	#print(user)
	affect_me_posts=user["no_support_posts"]
	newvalues = { "$set": { "no_support_posts": affect_me_posts+[post_id]}}
	UsersCol.update_one(myquery, newvalues)

#createNewPost("Person1","Test title","Test text",["keyword1","keyword2"])

for x in PostsCol.find():
  print(x)

#voteAffectsMe("1","1")