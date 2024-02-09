from flask_sqlalchemy import SQLAlchemy
from flask import Flask 

app = Flask(__name__)
app.secret_key = "kya kr rahe hai hum ye"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy()

class Buyer(db.Model):
    __tablename__ = 'buyers'
    email = db.Column(db.String(100),unique=True,primary_key=True,nullable=False)
    name = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(100),nullable=False)
    latitude = db.Column(db.String(100),nullable=False)
    longitude = db.Column(db.String(100),nullable=False)
    state = db.Column(db.String(100),nullable=False)
    city = db.Column(db.String(100),nullable=False)
    phone = db.Column(db.String(100),nullable=False)
    def __init__(self,email,name,password,latitude,longitude,state,city,phone):
        self.email = email
        self.name = name
        self.phone = phone
        self.password = password
        self.latitude = latitude
        self.longitude = longitude
        self.state = state
        self.city = city


class Seller(db.Model):
    __tablename__ = 'sellers'
    email = db.Column(db.String(100),unique=True,primary_key=True,nullable=False)
    name = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(100),nullable=False)
    latitude = db.Column(db.String(100),nullable=False)
    longitude = db.Column(db.String(100),nullable=False)
    shop_state = db.Column(db.String(100),nullable=False)
    shop_city = db.Column(db.String(100),nullable=False)
    shop_name = db.Column(db.String(100),nullable=False)
    phone = db.Column(db.String(100),nullable=False)
    category = db.Column(db.String(100),nullable=False)
    views = db.Column(db.Integer)
    def __init__(self,email,name,password,latitude,longitude,shop_state,shop_city,shop_name,phone,category):
        self.email = email
        self.name = name
        self.password = password
        self.latitude = latitude
        self.longitude = longitude
        self.shop_name = shop_name
        self.shop_state = shop_state
        self.shop_city = shop_city
        self.phone = phone
        self.category = category
        self.views = 0


    







    





