import pymongo
import datetime 
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["CityZen"]


UsersCol=mydb["Users"]
PostsCol = mydb["Posts"]
CommentsCol = mydb["Comments"]


last_inserted_user=UsersCol.find_one({},sort=[( '_id', pymongo.DESCENDING )])
last_inserted_user_id=last_inserted_user["user_id"]


last_inserted_post=PostsCol.find_one({},sort=[( '_id', pymongo.DESCENDING )])
last_inserted_post_id=last_inserted_post["post_id"]


last_inserted_comment=CommentsCol.find_one({},sort=[( '_id', pymongo.DESCENDING )])
last_inserted_comment_id=last_inserted_comment["comment_id"]