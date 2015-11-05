##############################################
### Geocode an adress for an author recovered from ADS
##############################################

import numpy as np 
import json
from urllib2 import urlopen
import requests

def geocode(address):
	#url = (u"http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address={0}".format(address.replace(" ", "+")))
	query_terms = dict()
	query_terms["key"]="Ai4Hluuw58D5pakGOmh5zwFr4yLY-bN7E2EGnJc2aMxbUUdJPzlRbg8kjiWMtrFP"
	query_terms["q"] = address
	#url = (u"http://dev.virtualearth.net/REST/v1/Locations?".format(address.replace(" ", "+"))."&key=BingMapsKey")
	url = "http://dev.virtualearth.net/REST/v1/Locations"
	result = requests.get(url, params=query_terms).json()
	try:
		if result["resourceSets"][0]["estimatedTotal"] > 0:
			return result["resourceSets"][0]["resources"][0]["geocodePoints"][0]["coordinates"]
	except:
		print('Location not found, sorry :(')
		return None
	print('Location not found')
	return None