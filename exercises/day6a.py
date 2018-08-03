# The program will prompt for a location, contact a web service and
# retrieve JSON for the web service and parse that data, and retrieve
# the first place_id from the JSON. A place ID is a textual identifier
# that uniquely identifies a place as within Google Maps. 

from urllib import request, parse, error
import json


address = "BITS Pilani"

url = "http://py4e-data.dr-chuck.net/geojson?"
param = parse.urlencode({"address": address})

with request.urlopen(url+param) as source:	
	source = source.read()
	source = json.loads(source)
	source = source["results"][0]["place_id"]
	print(source)



