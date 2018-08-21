# https://www.ncdc.noaa.gov/cdo-web/webservices/v2
# https://www.ncdc.noaa.gov/cdo-web/api/v2/{endpoint}
# Minneapolis CITY:US270013
# "name": "LOWER ST. ANTHONY FALLS, MN US",
# "id": "GHCND:USC00214884"
# Run linter
# Figure out line breaks

# "name": "MINNEAPOLIS ST PAUL INTERNATIONAL AIRPORT, MN US",
# "datacoverage": 1,
# "id": "GHCND:USW00014922",
# While sweet, this data has some problems, first of all lag:
# If observed, the station dataset includes max and minimum temperatures,
# total precipitation, snowfall, and depth of snow on ground. Some U.S.
# station data are typically delayed only 24 hours.
# Second, lag again. It's the 15th and the most recent data point is the 6th.
# Still, I think it's useful for broad trends and snowmelt and other geological
# observations that could be baked into our model.

import os
import requests
import json
import sqlite3

# Open or create Canoeing database
conn = sqlite3.connect('canoeing.db')
c = conn.cursor()

# Create or refresh table
c.execute('''
CREATE TABLE IF NOT EXISTS Weather ("Date" DATE PRIMARY KEY, Precip REAL, Temp REAL, Snowfall REAL, SnowAccum REAL, Evaporation REAL)''')

noaa_key = os.environ['NOAA']
offset = 1
limit = 250
count = 0
startdate = '2018-08-08'
enddate = '2018-08-08'
url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data'

# PRCP = Precipitation (mm or inches as per user preference, inches to hundredths 
# SNOW = Snowfall (mm or inches as per user preference inches to tenths
# SNWD = Snow depth (mm or inches as per user preference inches
# TMAX  =  Maximum  temperature  (Fahrenheit  or  Celsius  as  per  user  preference,  Fahrenheit  to  tenths
metrics = ['PRCP', 'TMAX', 'SNOW', 'SNWD']

# Time to write to the DB - might need to handle pagination
print("Getting report ... ")
while count is 0 or offset <= count:
	headers = {'token': noaa_key}
	payload = {
	'stationid': 'GHCND:USC00214884', 'datasetid': 'GHCND',
	'datatypeid': metrics, 'startdate': startdate,
	'enddate': enddate, 'units': 'standard', 'limit': limit,
	'offset': offset
	}

	r = requests.get(url, headers = headers, params = payload)
	data = json.loads(r.text)
	count = data['metadata']['resultset']['count']

	print(f'Grabbing {offset} through {offset + limit - 1} of {count} records')

	for result in data['results']: #BROKE - properly iterate to grab the correct column names.
		for metric in metrics:
			if "PRCP" in result['datatype']:
				date = result['date']
				precip = result['value']
				c.execute('REPLACE INTO Weather ("Date", Precip) VALUES (?,?)',(date[:10], precip))
			else: 
				date = result['date']
				val = result['value']
				c.execute('UPDATE Weather SET ' + metric + ' = ? WHERE "Date" = ?', (val, date[:10]))

	offset += limit

conn.commit()
c.close()
