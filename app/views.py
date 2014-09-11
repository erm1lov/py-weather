# -*- coding: utf-8 -*-
from app import app
from flask import render_template

import pyowm
from datetime import datetime

from config import OWID
from models import City, Weather

@app.route('/')
@app.route('/index')
def index():
	owm = pyowm.OWM(OWID)
	history = owm.weather_history_at_place('Moscow')
	return render_template("index.html",
		weather = history,
		datetime = datetime)

@app.route('/grabcities/')
def grabcities():
	owm = pyowm.OWM(OWID)
	registry = owm.city_id_registry()

	cities = City.query.filter(City.city_id.exists(False))
	result = 'All cities has an id'
	for c in cities:
		result = ''
		city = City.query.filter(City.name == c.name).one()
		city.city_id = registry.id_for(str(city.name))
		city.save()
		result += 'Add id %s for %s <br />' % str(city.city_id), str(city.name)

	return result


@app.route('/grabweather/<int:city_id>')
def grabweather(city_id):
	owm = pyowm.OWM(OWID)
	history = owm.weather_history_at_place(city_id)
