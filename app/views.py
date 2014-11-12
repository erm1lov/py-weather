# -*- coding: utf-8 -*-
from app import app
from flask import render_template

import pyowm
from datetime import datetime, timedelta

from config import OWID
from models import City, Weather, Moscow

import testdata

class TestCity(testdata.DictFactory):
    date = testdata.DateIntervalFactory(datetime.now() - timedelta(days=365), timedelta(hours=24))
    status = testdata.RandomSelection(['clouds', 'clear', 'rain'])

@app.route('/')
@app.route('/index')
def index():
	owm = pyowm.OWM(OWID)	
	history = owm.weather_history_at_place('Moscow')
	return render_template("index.html",
		weather = history,
		datetime = datetime)

# @app.route('/grabcities/')
# def grabcities():
# 	owm = pyowm.OWM(OWID)
# 	registry = owm.city_id_registry()

# 	cities = City.query.filter(City.city_id.exists(False))
# 	result = 'All cities has an id'
# 	for c in cities:
# 		result = ''
# 		city = City.query.filter(City.name == c.name).one()
# 		city.city_id = registry.id_for(str(city.name))
# 		city.save()
# 		result += 'Add id %s for %s <br />' % str(city.city_id), str(city.name)

# 	return result


# @app.route('/grabweather')
# def grabweather():
# 	owm = pyowm.OWM(OWID)
# 	dt = datetime.now()
# 	history = owm.weather_history_at_place('Moscow', dt.replace(month = dt.month-1), datetime.now())

# 	return render_template("index.html",
# 		weather = history,
# 		datetime = datetime)

@app.route('/testdata')
def testdata():
	result = ''
	for data in TestCity().generate(365):
		moscow = Moscow(date=data['date'], status=data['status'])
		result += str(data['status'])
		moscow.save()

	return result



