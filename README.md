# Geographic Information System API
#### RESTful API with Flask and PostgreSQL which supports basic CRUD operations such as adding a new location, fetching all nearby locations and determining which region a new location falls in.

### Dependencies

This project requires **Python 3.3+** and the following Python libraries installed:

* [Flask](http://flask.pocoo.org/)
* [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/installation.html)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Shapely](https://pypi.python.org/pypi/Shapely)
* [GeoPy](https://pypi.python.org/pypi/geopy)
* [Requests](http://docs.python-requests.org/en/master/user/install/)

### Running

* Paste **Database URI** in **init.py**  
* Run **models.py**  
	It will create the required tables in the database.
* Run **loadData.py**  
	It will read the CSV file and load the data to the table.
* Run **loadShapes.py**  
	It will parse the JSON file and load the data to the table.
* Run **app.py**  
	You can now open a new tab and interact with the API from the command line.

### Interacting with API

You can make following GET and POST requests.

* *__post_location__*  
	Add new data to the table by providing Latitude, Longitude, Pin Code, Address and City.  
	Replace LATITUDE, LONGITUDE, PINCODE, ADDRESS and CITY in the command below.  
	``` 
	curl -d "lat=LATITUDE&lon=LONGITUDE&pin=PINCODE&address=ADDRESS&city=CITY" 
	-X POST http://127.0.0.1:5000/post_location/ 
	```  
	It returns:  
	* 'Successful': The data was added successfully.
	* 'Unsuccessful': The data was added not successfully because it was already present or there was some discrepancy in the data.

* *__get_using_self__*  
	Given location and radius, it fetches all the nearby pin codes within the radius. It uses Haversine formula.  
	Replace LATITUDE, LONGITUDE and RADIUS in the command below.  
	```
	curl -X GET http://127.0.0.1:5000/get_using_self/LATITUDE/LONGITUDE/RADIUS/ 
	```
	It returns list of all pincodes within the radius.  

* *__get_using_postgres__*  
	Given location and radius, it fetches all the nearby pin codes within the radius. It uses geopy library.  
	Replace LATITUDE, LONGITUDE and RADIUS in the command below.  
	``` 
	curl -X GET http://127.0.0.1:5000/get_using_postgres/LATITUDE/LONGITUDE/RADIUS/
	```  
	It returns list of all pincodes within the radius.

* *__find_place__*  
	Given latitude and longitude, it will tell you which place it falls within.  
	Replace LATITUDE and LONGITUDE in the command below.  
	``` 
	curl -X GET http://127.0.0.1:5000/find_place/LATITUDE/LONGITUDE/
	```  
	It returns location of the place.  

## Running the tests
* Run **tests.py**
