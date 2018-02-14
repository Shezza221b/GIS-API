from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from models import region
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.request import urlopen, Request
from sqlalchemy.ext.declarative import declarative_base
import _pickle as cPickle
from json import loads
from init import getUrl

path = getUrl()
db = create_engine(path)

def parse():
    Session = sessionmaker(db)
    session = Session()
    url = 'https://gist.githubusercontent.com/ramsingla/6202001/raw/1dc42df3c6d8f4db95b7f7b65add1f520578ab33/map.geojson'
    data = loads(urlopen(Request(url)).read().decode('utf-8'))
    for f in data['features']:
        pickledPolygon = cPickle.dumps(Polygon(f['geometry']['coordinates'][0]))
        new = region(f['properties']['name'], f['properties']['type'], f['properties']['parent'], pickledPolygon)
        session.add(new)
    session.commit()

if __name__ == "__main__":
    parse()
