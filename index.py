from flask import Flask, render_template, request
from flask_pymongo import PyMongo
from datetime import timedelta
from datetime import datetime
from flask import session, redirect, url_for

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb+srv://user:1234@cluster0.pplyymz.mongodb.net/myweb?"
                            # 클라우드(atlas)
mongo = PyMongo(app)     #mongo 변수를 통해 DB(myweb)에 접근 가능

app.config["SECRET_KEY"]= "abcd"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(seconds=500)

comments = []

@app.route('/index')
def index():
    return render_template('index.html',comments=comments)
   
@app.route('/post', methods=['GET','POST'])
def post():
    if request.method =='POST':
        comment = request.form.get('comment')
        if comment != "":
            comments.append(comment)
    return render_template('post.html', comments=comments)