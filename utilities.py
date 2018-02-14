from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from flask import Flask, request
from flask_restful import Resource, Api
from models import data, region
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.request import urlopen, Request
from math import radians, sin, cos, atan2, sqrt
from init import getUrl

path = getUrl()
db = create_engine(path)
base = declarative_base()

def distance(a, b):
    lat1 = float(a.latitude)
    lat2 = float(b.latitude)
    lon1 = float(a.longitude)
    lon2 = float(b.longitude)
    phi_1 = radians(lat1)
    phi_2 = radians(lat2)
    delta_phi = radians(lat2-lat1)
    delta_lambda = radians(lon2-lon1)
    x = sin(delta_phi/2.0)**2 + cos(phi_1)*cos(phi_2)*sin(delta_lambda/2.0)**2
    y=2*atan2(sqrt(x),sqrt(1-x))
    R = 6371
    return R*y

def check(new):
    Session = sessionmaker(db)
    session = Session()
    allData = session.query(data).all()
    for d in allData:
        if new.pin==d.pin or distance(d, new) < 0.01:
            return False
    if new.latitude > 90 or new.longitude > 180:
        return False
    return True

def createNewEntry(new):
	try:
		float(new[3])
		float(new[4])
	except Exception as e:
		return None
	try:
		accuracy = int(new[5])
	except Exception as e:
		accuracy = 0
	return data(new[0], new[1], new[2], float(new[3]), float(new[4]), accuracy)
