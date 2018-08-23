import requests
import json
import sqlite3

from datetime import datetime

# Key of metric values:
# 0: Temperature, water, degrees Celsius
# 1: Precipitation, total, inches
# 2: Discharge, cubic feet per second
# 3: Gage height, feet
# 4: Specific conductance, water, unfiltered, microsiemens per centimeter at 25 degrees Celsius

metrics = {
	0: "Temp",
	1: "Precip",
	2: "FlowRate",
	3: "GageHeight",
	4: "SpecConductance"
}

#Enter any value for days back from current day - up to a max of 150. Set to None to run with specific dates
days = 14


#Define parameters for GET header
headers = {'Accept-Encoding': 'gzip, compress'}
payload = {'format': 'json', 'indent': 'on', 'sites': '05289800', 'period': 'P' + str(days) + 'D', 'siteStatus': 'all'}

#Create response object
r = requests.get('http://waterservices.usgs.gov/nwis/iv/', headers = headers, params = payload)

print(r.headers)
