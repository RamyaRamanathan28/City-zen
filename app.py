from flask import Flask, render_template, request, json, session, url_for, redirect, flash
# from passlib.hash import sha256_crypt
import time
import datetime
import os
app = Flask(__name__)
# import MySQLdb

app.secret_key = 'many random bytes'
app.config['APPLICATION_ROOT'] = True

@app.route("/", methods = ['POST', 'GET'])
def home():
        dirpath = os.getcwd()
        return render_template("index.html")

@app.route("/category", methods = ['POST', 'GET'])
def category():
        return render_template("listing.html")

                         
if __name__ == "__main__":
    app.run(debug = True)