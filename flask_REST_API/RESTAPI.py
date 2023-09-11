import json
from flask import Flask, render_template, url_for, redirect, request, jsonify
from flask_REST_API import app,db
from flask_REST_API.routes import *

#REST API Operation 
@app.route('/users', methods=['GET'])
def user_all():
    users= db.inventory.find()
    user_list = []

    for user in users:
        user_list.append({
            '_id': user['_id'],
            'name': user['name'],
            'email': user['email'],
            'password': user['password']
        })
    return user_list
    
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = db.inventory.find_one({'_id':id})   
    return user

@app.route('/users', methods=['POST'])
def add_user():
    #Data Directly Add from POSTMAN
    user_data = request.get_json()
    name=user_data['name']
    email=user_data['email']
    password=user_data['password']

    count = db.inventory.count_documents({})
    id=count+1
    print(id)

    insert=db.inventory.insert_one(
        {'_id':id,
         'name':name,
         'email':email,
         'password':password})
    
    if insert:
        new_data=db.inventory.find_one({'_id':id})
        return jsonify({'users': new_data})
    else:
        return "<p>Insertion Failed</p>"

@app.route('/users/<int:id>', methods=["PUT"])
def update_user(id):
    data= request.get_json()
    data['_id']=id
    update=db.inventory.replace_one({'_id':id}, data)

    if update:
        return jsonify({'message':'Updated Successfully'})
    else:
        return jsonify({'message':'Not Updated'})

@app.route('/users/<int:id>',methods=["DELETE"])
def delete_user(id):
    data=request.get_json()
    data['_id']=id
    delete=db.inventory.delete_one({'_id':id})

    if delete:
        return jsonify({'message':'Record Deleted'})
    else:
        return jsonify({'message':'Not Deleted'})

