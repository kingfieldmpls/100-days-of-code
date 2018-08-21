# NWS
# 30	
# id	"https://api.weather.gov/stations/KMSP"
# type	"Feature"
# geometry	
# type	"Point"
# coordinates	
# 0	-93.22889
# 1	44.88306
# properties	
# @id	"https://api.weather.gov/stations/KMSP"
# @type	"wx:ObservationStation"
# elevation	
# value	256.03200000000004
# unitCode	"unit:m"
# stationIdentifier	"KMSP"
# name	"Minneapolis, Minneapolis-St. Paul International Airport"
# timeZone	"America/Chicago"
# https://api.weather.gov/gridpoints/MPX/109,67

import json
import requests
import sqlite3

# Open or create Canoeing database
conn = sqlite3.connect('canoeing.db')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS Forecast')

metrics = [temperature, probabilityOfPrecipitation, quantitativePrecipitation, iceAccumulation, snowfallAmount, snowLevel]


# Create or refresh table
c.execute('''
CREATE TABLE IF NOT EXISTS Forecast ("Date" DATE PRIMARY KEY, Temp REAL, PrecipChance REAL, Precip REAL, IceAccum REAL, SnowAccum REAL, SnowLevel REAL)''')

for metric in metrics:
	if "Temp" in data['value']['timeSeries'][metric]['variable']['variableDescription']:
		for day in range(len(data['value']['timeSeries'][metric]['values'][0]['value'])):
			Date = data['value']['timeSeries'][metric]['values'][0]['value'][day]['dateTime']
			Temp = data['value']['timeSeries'][metric]['values'][0]['value'][day]['value']
			Temp = (float(Temp) * 9/5) + 32 #Convert to Farhrenheit
			c.execute('REPLACE INTO Forecast ("Date", Temp) VALUES (?,?)',(Date[:16], Temp))
	else:
		for day in range(len(data['value']['timeSeries'][metric]['values'][0]['value'])):
			Date = data['value']['timeSeries'][metric]['values'][0]['value'][day]['dateTime']
			value = data['value']['timeSeries'][metric]['values'][0]['value'][day]['value']
			c.execute('UPDATE CreekHourly SET ' + column + ' = ? WHERE "Date" = ?', (value, Date[:16]))

[properties][metric][values][timeiter][validTime|value]
