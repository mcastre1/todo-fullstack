from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__) # Init flask app
CORS(app) # Used to disable cors errors when sending cross origin requests to app.

# Using local sqlite database.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app) # Creates database instance, which gives us access to the database above.
