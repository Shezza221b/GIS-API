from models import data, region
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.request import urlopen, Request
from csv import reader
from sys import stdout
from sqlalchemy.ext.declarative import declarative_base
from utilities import createNewEntry
from init import getUrl

path = getUrl()
db = create_engine(path)

def loadData():
	Session = sessionmaker(db)
	session = Session()
	url = 'https://raw.githubusercontent.com/sanand0/pincode/master/data/IN.csv'
	csv_data = urlopen(Request(url)).read().decode('utf-8').split('\n')
	csv_reader = reader(csv_data, delimiter=',', quotechar='|')
	csv_reader.__next__()
	for d in csv_reader:
		new = createNewEntry(d)
		if new :
			session.add(new)
	session.commit()

if __name__ == "__main__":
	loadData()
