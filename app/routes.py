import os
from app import app
from flask import render_template, request, redirect, session, url_for
# from bson.objectid import ObjectID

from flask_pymongo import PyMongo
#
app.secret_key = "sdjfhbj;"
# name of database
app.config['MONGO_DBNAME'] = 'advance'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://William_Lu:C5V1vvx7OLjks3qz@cluster0-h4hvy.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')

@app.route("/menu")
def menu():
    return render_template('menu.html')


@app.route('/index')

def index():
    session['username'] = "William"
    # connect to the database
    collection = mongo.db.events
    #query the database to all events
    events = list(collection.find({}))
    # store events as a dictionary call events
    for x in events:
        print(x["event_name"])
    # print event
    return render_template('index.html', events = events)


# CONNECT TO DB, ADD DATA

@app.route('/results', methods = ["get","post"])

def results():
    # shore userinf from the form
    userinfo = dict(request.form)
    print(userinfo)
    # get the event name and date and store them
    event_name = userinfo["event_name"]
    event_date = userinfo["event_date"]
    event_type = userinfo["category"]
    # connect to the database
    collection = mongo.db.events
    # insert new data
    collection.insert({"event_name": event_name, "event_date": event_date,"event_type": event_type})
    # collection.insert({"event_name":"test", "event_date":"today"})
    # return a message to the user
    return redirect("/index")

@app.route("/secret")
def secret():
    #connect to the database
    collection = mongo.db.events
    #delete everything from the database
    #invoke the delete_many method on the collection
    collection.delete_many({})
    return redirect('/index')

@app.route("/test")
def sorted():
    collection = mongo.db.events
    test = list(collection.find({"event_type": "test"}))
    print (test)
    return render_template('index.html', events = test)

@app.route("/project")
def project():
    collection = mongo.db.events
    project = list(collection.find({"event_type": "project"}))
    print (project)
    return render_template('index.html', events = project)

@app.route("/classwork")
def classwork():
    collection = mongo.db.events
    classwork = list(collection.find({"event_type": "classwork"}))
    print (classwork)
    return render_template('index.html', events = classwork)

@app.route("/homework")
def homework():
    collection = mongo.db.events
    homework = list(collection.find({"event_type": "homework"}))
    print (homework)
    return render_template('index.html', events = homework)
