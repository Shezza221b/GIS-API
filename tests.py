import unittest
from requests import post
from json import loads
from urllib.request import Request, urlopen


class test(unittest.TestCase):

	def test_post_location(self):
		url = "http://127.0.0.1:5000/post_location/"
		testCases = [ {"input":{"lat":"aaa","lon":"bbb","pin":"999999","address":"aaaaaa","city":"bbbbb"}, "output":'Unsuccessful'},\
					  {"input":{"lat":"1111","lon":"2222","pin":"aaaaa","address":"aaaaaa","city":"bbbbb"}, "output":'Unsuccessful'},\
					  #{"input":{"lat":"28.5733056","lon":"77.0122136","pin":"IN/110075","address":"Dwarka","city":"New Delhi"}, "output":'Successful'},\
					  {"input":{"lat":"111","lon":"100","pin":"111","address":"random","city":"random"}, "output":'Unsuccessful'},\
					  {"input":{"lat":"57","lon":"220","pin":"123","address":"random","city":"random"}, "output":'Unsuccessful'}]
		for T in testCases:
			self.assertEqual(loads(post(url, data=T['input']).text), T["output"])


	def test_pin_using_postgres(self):
		url = "http://127.0.0.1:5000/get_using_postgres/"
		testCases = [ {"input":"26.5/70.2/100", "output":["IN/344013", "IN/344014", "IN/344015", "IN/345030"]},\
					  {"input":"20.2/70.2/100/","output":["IN/362256", "IN/362257", "IN/362259", "IN/362515", "IN/362520", "IN/362530", "IN/362540", "IN/362550", "IN/362560"]},\
					  {"input":"26.41/87.25/100/", "output":["IN/854325", "IN/854326", "IN/854327", "IN/854328"]},\
					  {"input":"20.5/73.2/10/", "output":[]}]
		for T in testCases:
			self.assertEqual(loads(urlopen(Request(url+T["input"])).read().decode('utf8')),T["output"])


	def test_pin_using_self(self):
		url = "http://127.0.0.1:5000/get_using_self/"
		testCases = [ {"input":"26.5/70.2/100", "output":["IN/344013", "IN/344014", "IN/344015", "IN/345030"]},\
					  {"input":"20.2/70.2/100/","output":["IN/362256", "IN/362257", "IN/362259", "IN/362515", "IN/362520", "IN/362530", "IN/362540", "IN/362550", "IN/362560"]},\
					  {"input":"26.41/87.25/100/", "output":["IN/854325", "IN/854326", "IN/854327", "IN/854328"]},\
					  {"input":"20.5/73.2/10/", "output":[]}]
		for T in testCases:
			self.assertEqual(loads(urlopen(Request(url+T["input"])).read().decode('utf8')),T["output"])


	def test_find_place(self):
		url = "http://127.0.0.1:5000/find_place/"
		testCases = [ {"input":"19.15/72.83","output":{"Region":'Maharashtra', "City":'Mumbai'}},\
					  {"input":"28.51/77.38","output":{"Region":'Uttar Pradesh', "City":'Noida'}},\
					  {"input":"28.56/76.92","output":{"Region":'Delhi', "Zone":"South West Delhi"}},\
					  {"input":"18.96/72.93/","output":{"Region":'Mumbai', "Island":"Elephanta Island"}},\
					  {"input":"11.1/11.1","output":'Nowhere'}]
		for T in testCases:
			self.assertEqual(loads(urlopen(Request(url+T["input"])).read().decode('utf8')),T["output"])


if __name__ == "__main__":
	unittest.main(verbosity=2)
