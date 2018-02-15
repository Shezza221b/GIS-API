from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from flask import Flask, request
from flask_restful import Resource, Api
from models import data, region
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from geopy.distance import great_circle
from urllib.request import urlopen, Request
from utilities import distance, check, createNewEntry
import _pickle as cPickle
from init import getUrl

app = Flask(__name__)
api = Api(app)

path = getUrl()
db = create_engine(path)
base = declarative_base()

class post_location(Resource):
	def post(self):
		Session = sessionmaker(db)
		session = Session()
		new = createNewEntry([request.form['pin'], request.form['address'], request.form['city'], request.form['lat'], request.form['lon'], 0])
		if new and check(new):
			session.add(new)
			session.commit()
			return ('Successful')
		else:
			return ('Unsuccessful')

class get_using_self(Resource):
	def get(self, lat, lon, radius):
		Session = sessionmaker(db)
		session = Session()
		allData = session.query(data).all()
		new = data('-', '-', '-', lat, lon, 0)
		result = [i.pin for i in allData if distance(new, i) <= radius]
		return result

class get_using_postgres(Resource):
	def get(self, lat, lon, radius):
		Session = sessionmaker(db)
		session = Session()
		allData = session.query(data).all()
		result = []
		givenLocation = (lat, lon)
		for i in allData:
			currentLocation = (i.latitude, i.longitude)
			dis = great_circle(currentLocation, givenLocation).kilometers
			if dis <= radius:
				result.append(i.pin)
		return result

class find_place(Resource):
	def get(self, lat, lon):
		Session = sessionmaker(db)
		session = Session()
		allData = session.query(region).all()
		givenLocation = Point(lon, lat)
		for i in allData:
			unpickledPolygon = cPickle.loads(i.polygon)
			if unpickledPolygon.contains(givenLocation):
				return {i.type:i.name, 'Region':i.parent}
		return ('Nowhere')

api.add_resource(post_location, '/post_location/')
api.add_resource(get_using_self, '/get_using_self/<float:lat>/<float:lon>/<int:radius>/')
api.add_resource(get_using_postgres, '/get_using_postgres/<float:lat>/<float:lon>/<int:radius>/')
api.add_resource(find_place, '/find_place/<float:lat>/<float:lon>/')

if __name__ == "__main__":
	app.run(debug=True)
