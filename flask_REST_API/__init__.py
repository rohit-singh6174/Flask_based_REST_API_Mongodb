
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['SECRET_KEY']='ThisisRohitTestAPI'    #CSRF for wtform
app.config["MONGO_URI"] = "mongodb://localhost:27017/FlaskUser"
db = PyMongo(app).db

from flask_REST_API import routes