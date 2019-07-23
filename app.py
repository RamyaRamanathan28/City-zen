from flask import Flask, render_template, request, json, session, url_for, redirect, flash
# from passlib.hash import sha256_crypt
import time
import datetime
import os
import sys
sys.path.append("db/")
import user_data 
import posts_data
app = Flask(__name__)
# import MySQLdb

app.secret_key = 'many random bytes'
app.config['APPLICATION_ROOT'] = True

	# @app.route("/", methods = ['POST', 'GET'])
	# def home():
	#         dirpath = os.getcwd()
	#         return render_template("index.html")

@app.route("/detail", methods = ['POST', 'GET'])
def detail():

	username = request.args.get('username')
	post_id = request.args.get('post_id')
	print("POST ID:"+ post_id)
	data = posts_data.getPost(post_id)
	print(data)
 	return render_template("detail.html", data=data)

@app.route("/explore", methods = ['POST', 'GET'])
def explore():
	if request.method == 'POST':
		username = request.args.get('username')
		post_id = request.args.get('post_id')
		print("POST")
		if 'up' in request.form:
			
			print("UP")
	data = posts_data.getAllPosts()
	username = request.args.get('username')
	print(username)
	print(data)
 	return render_template("explore.html", data = data, username = username)

@app.route("/post", methods = ['POST', 'GET'])
def post():
	print(request.method)
	username = request.args.get('username')
	post_id = request.args.get('post_id')
	if request.method == 'POST':
		if 'up' in request.form:
			posts_data.voteSupport(post_id, username)
		if 'down' in request.form: 
			posts_data.downvoteSupport(post_id, username)
		if 'affects' in request.form:
			posts_data.voteAffectsMe(post_id, username)
 		return redirect(url_for("explore", username=username))

@app.route("/login", methods = ['POST', 'GET'])
def login():
	if request.method == 'POST':
		if 'uname' in request.form:
			username= str(request.form["uname"])
			password= str(request.form["password"])
			# print(username)
			# print(password)
			if user_data.validUserPassword(username,password):
				print("VALID password")
				
				return redirect(url_for("explore", username=username))
			else:
				return redirect(url_for("login"))
	return render_template("signin.html")

@app.route("/createPost", methods = ['POST', 'GET'])
def createPost():
	username = request.args.get('username')
	print(username)
	if request.method=='POST':
		print('POST')
		if 'Title' in request.form:
			Title= str(request.form["Title"])
			Category= str(request.form["Category"])
			Description = str(request.form["Category"])
			Keywords = str(request.form["Keywords"]).split(", ")
			posts_data.createNewPost(username,Title,Description, Keywords, Category)
			return redirect(url_for("Account", username=username))



	
	return render_template("createPost.html", username=username)


@app.route("/Account", methods = ['POST', 'GET'])
def Account():
	username = request.args.get('username')
	data = posts_data.getPostForUser(username)
	userData = user_data.getUserData(username)
	print(userData)
	return render_template("myAccount.html", data=data, userData=userData)



@app.route("/", methods = ["POST", "GET"])
def index():
        return redirect(url_for("login"))
                         
if __name__ == "__main__":
    app.run(debug = True)