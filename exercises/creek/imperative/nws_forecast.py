# NWS
# 30
# id    "https://api.weather.gov/stations/KMSP"
# type  "Feature"
# geometry
# type  "Point"
# coordinates
# 0 -93.22889
# 1 44.88306
# properties
# @id   "https://api.weather.gov/stations/KMSP"
# @type "wx:ObservationStation"
# elevation
# value 256.03200000000004
# unitCode  "unit:m"
# stationIdentifier "KMSP"
# name  "Minneapolis, Minneapolis-St. Paul International Airport"
# timeZone  "America/Chicago"
# https://api.weather.gov/gridpoints/MPX/109,67
# It looks like forecast grids can expire. Not sure what to do then.

import requests
import sqlite3

# Open or create Canoeing database
conn = sqlite3.connect('canoeing.db')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS Forecast')

metrics = {'temperature': 'temp', 'probabilityOfPrecipitation': 'PrecipChance', 'quantitativePrecipitation': 'Precip', 'iceAccumulation': 'IceAccum', 'snowfallAmount': 'SnowAccum', 'snowLevel': 'SnowLevel'}


# Create or refresh table
c.execute('''
CREATE TABLE IF NOT EXISTS Forecast ("Date" DATE PRIMARY KEY, Temp REAL, PrecipChance REAL, Precip REAL, IceAccum REAL, SnowAccum REAL, SnowLevel REAL)''')

# Create response object
r = requests.get('https://api.weather.gov/gridpoints/MPX/109,67')

# Decode JSON
data = r.json()

if "ForecastGridExpired" in data['type']:
    print("Weather forecase has expired.")
else:
    for prop in data['properties']:
        if prop in list(metrics.keys()):
            if prop == 'temperature':
                for val in range(len(data['properties'][prop]['values'])):
                    Date = data['properties'][prop]['values'][val]['validTime']
                    Value = data['properties'][prop]['values'][val]['value']
                    c.execute('REPLACE INTO Forecast ("Date", Temp) VALUES (?,?)', (Date[:25], Value))
            else:
                for val in range(len(data['properties'][prop]['values'])):
                    Date = data['properties'][prop]['values'][val]['validTime']
                    Value = data['properties'][prop]['values'][val]['value']
                    Column = metrics[prop]
                    c.execute('UPDATE Forecast SET ' + Column + ' = ? WHERE "Date" = ?', (Value, Date[:25]))

conn.commit()
c.close()
