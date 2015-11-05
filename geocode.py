##############################################
### Geocode an adress for an author recovered from ADS
##############################################

import numpy as np 
import json
from urllib2 import urlopen
import requests

def geocode(address):
	url = (u"http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address={0}".format(address.replace(" ", "+")))
	result = requests.get(url).json()
	if result["status"]==u'OK':
		res = result.get("results")[0]
		return res["geometry"]["location"]["lat"], res["geometry"]["location"]["lng"]
	else:
		pass
