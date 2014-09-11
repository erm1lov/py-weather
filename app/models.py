from app import db, app
from flask import Flask
from flask.ext.mongoalchemy import MongoAlchemy

class City(db.Document):
	name = db.StringField()
	city_id = db.IntField()

class Weather(db.Document):
	city = db.DocumentField(City)
	date = db.DateTimeField()
	status = db.StringField()
