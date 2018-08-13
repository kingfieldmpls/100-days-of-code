# minnehaha creek flow data
# This flow data retrieval is super awesome - here are the resources:
# https://help.waterdata.usgs.gov/faq/automated-retrievals
# https://waterservices.usgs.gov/rest/
#
# Site #05289800
#
# Functionality
# Grab daily
# How do I want to visualize the output?
# Probably something where I color code based on whether or not it's good for canoeing
# Then try to make predictions based on how much rain falls, how high the creek is going to be for how long
# Then look at the weather forecast and predict (based on where the creek is now) how high it will be in the future
# Then compare those quesses to reality to improve the model
# Choose to back fill or just to grab updated since when making the request
#
# Note: Is there a good time of day to retrieve data?
# Yes.  If possible, we prefer that you retrieve information during "off peak" hours. Midnight to 6 AM Eastern Time is ideal.

import requests
import json

# Key of metric values:
# 0: Max water temp
# 1: Min water temp
# 2: Mean water temp
# 3: Mean Discharge, cubic feet per second
# 4: Max Specific conductance, water, unfiltered, microsiemens per centimeter
# 5: Min Specific conductance, water, unfiltered, microsiemens per centimeter
# 6: Mean Specific conductance, water, unfiltered, microsiemens per centimeter

metrics = [2,3]
days = 7

#Define parameters
payload = {'format': 'json', 'indent': 'on', 'sites': '05289800', 'period': 'P' + str(days) + 'D', 'siteStatus': 'all'}

#Create response object
r = requests.get('https://waterservices.usgs.gov/nwis/dv/', params = payload)

#Decode JSON
data = r.json()

#Traverse and parse JSON output to prepare for writing to DB
for metric in metrics:
	column = data['value']['timeSeries'][metric]['variable']['variableDescription']
	degree = data['value']['timeSeries'][metric]['variable']['options']['option'][0]['value']
	print(degree + ' ' + column)
	for day in range(days):
		val = data['value']['timeSeries'][metric]['values'][0]['value'][day]['value']
		day = data['value']['timeSeries'][metric]['values'][0]['value'][day]['dateTime']
		print(val, day[:10])

