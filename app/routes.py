import os
from app import app
from flask import render_template, request, redirect




from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'advance'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://William_Lu:C5V1vvx7OLjks3qz@cluster0-h4hvy.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)


# INDEX

@app.route('/')
@app.route('/index')

def index():
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

@app.route('/add')

def add():
    # connect to the database
    collection = mongo.db.events
    # insert new data
    collection.insert({"event_name":"test", "event_date":"today"})

    # return a message to the user
    return "You added an event to database!"
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

@app.route("/social")
def sorted():
    collection = mongo.db.events
    social = list(collection.find({"event_type": "social"}))
    print (social)
    return render_template('index.html', events = social)

@app.route("/family")
def family():
    collection = mongo.db.events
    family = list(collection.find({"event_type": "family"}))
    print (family)
    return render_template('index.html', events = family)

@app.route("/friends")
def friends():
    collection = mongo.db.events
    friends = list(collection.find({"event_type": "friends"}))
    print (friends)
    return render_template('index.html', events = friends)

@app.route("/work")
def work():
    collection = mongo.db.events
    work = list(collection.find({"event_type": "work"}))
    print (work)
    return render_template('index.html', events = work)
