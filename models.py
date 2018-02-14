from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from math import sqrt,radians,sin,cos,atan2
from json import loads
import json
from sqlalchemy.types import TypeDecorator, PickleType
from init import getUrl

path = getUrl()
db = create_engine(path)
base = declarative_base()

class data(base):
	__tablename__ = 'data'
	pin = Column(String, primary_key=True)
	place_name = Column(String)
	city_name = Column(String)
	latitude = Column(Float)
	longitude = Column(Float)
	accuracy = Column(Float)

	def __init__(self, pin, place_name, city_name, latitude, longitude, accuracy):
		self.pin = pin
		self.place_name = place_name
		self.city_name = city_name
		self.latitude = latitude
		self.longitude = longitude
		self.accuracy = accuracy

class region(base):
	__tablename__ = 'region'
	id = Column(Integer, primary_key = True)
	name = Column(String)
	type = Column(String)
	parent = Column(String)
	polygon = Column(PickleType)
	def __init__(self, name, type, parent, polygon):
		self.name = name
		self.type = type
		self.parent = parent
		self.polygon = polygon


if __name__ == "__main__":
	base.metadata.create_all(db)
