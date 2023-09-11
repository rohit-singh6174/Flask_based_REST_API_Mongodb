from flask import Flask, render_template, url_for, redirect, request, jsonify
from flask_REST_API import app,db
from flask_REST_API.RESTAPI import *

# App CRUD Operation
@app.route('/')
def welcome():
    user=user_all()  #GET user API
    return render_template('welcome.html',user=user)


@app.route('/initialdata', methods=['POST','GET']) #Initial Data Btn
def initialdata():
    data = [
        {"_id": 1, "name": "Rohit Singh", "email": "rohit@example.com","password":"rohit@123"},
        {"_id": 2, "name": "Soham Sawant", "email": "soham@example.com","password":"soham@123"},
        {"_id": 3, "name": "Rohan Shahabaje", "email": "rohan@example.com","password":"rohan@123"}
    ]
    db.inventory.insert_many(data)

    return redirect(url_for('welcome'))

@app.route('/addnewuser', methods=['POST'])
def addnewuser():
    #print("Hello")
    if request.method == "POST":
        name = request.form.get("name")
        email= request.form.get("email")
        password=request.form.get("password")
        
        #print(name,email,password)
        count = db.inventory.count_documents({})
        id=count+1
        print(id)
        insert=db.inventory.insert_one(
        {'_id':id,
         'name':name,
         'email':email,
         'password':password})
        
        if insert:
            print("Record Inserted")
            return redirect(url_for('welcome'))
        else:
            return "<p>Insertion Failed</p>"
       
    return redirect(url_for('welcome'))

@app.route("/update_btn/<int:id>", methods=['GET'])
def update_btn(id):
    data= get_user(id)  #users/id API
    if data:
        return redirect(url_for('updatepage',id=id))
    else:
        print("Error")
        return redirect(url_for('welcome'))

@app.route("/updatepage/<int:id>", methods=["GET","POST"])
def updatepage(id):
    data=get_user(id)
    #print(type(data))


    if request.method == "POST":
        name = request.form.get("name")
        email= request.form.get("email")
        password=request.form.get("password")
        
        update_data= {
            "name":name,
            "email":email,
            "password":password
            }
        update=db.inventory.update_one({"_id": id}, {"$set": update_data})
        if update:
            print("Updated")
            return redirect(url_for('welcome'))
        else:
            print("Failed")
    
    
    return render_template('update.html',data=data)

@app.route("/deletebtn/<int:id>",methods=['GET'])
def deletebtn(id):
    delete=db.inventory.delete_one({'_id':id})
    
    if delete:
        return redirect(url_for('welcome'))
    else:
        return "<p>Not Deleted</p>"

