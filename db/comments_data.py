from db_init import *
from user_data import getUserId


def createNewComment(username,post_id,text):
	user_id=getUserId(username)
	if(user_id):
		mydict = { "comment_id":str(int(last_inserted_comment_id)+1),
				"post_id": post_id,
				"user_id": user_id,
				"text":text}
		x = CommentsCol.insert_one(mydict)
		print("Created new comment : ",x)


createNewComment("Person1","1","Test comment")