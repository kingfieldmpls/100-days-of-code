# https://www.ncdc.noaa.gov/cdo-web/webservices/v2
# https://www.ncdc.noaa.gov/cdo-web/api/v2/{endpoint}
# Minneapolis CITY:US270013
# "name": "LOWER ST. ANTHONY FALLS, MN US",
# "id": "GHCND:USC00214884"
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
#
# start/end dates: Required. Accepts valid ISO formated date (YYYY-MM-DD) or
# date time (YYYY-MM-DDThh:mm:ss). Data returned will be before the specified
# date. Annual and Monthly data will be limited to a ten year range while all
# other data will be limted to a one year range.
# To Do Here:
# - Write docstrings
# - Write various unit tests
# - Write helpful comments
# - Write methods for command line arguments

import json
import os

import requests
import sqlite3

# What are my steps:
# 1. Startup the Requests service
# 2. Grab all of the data
# 3. Sort all of the data
# 4. Write everything to the DB

# Define start and end dates
startdate = '2018-08-01'
enddate = '2018-08-31'

# Setup variables for pagination
offset = 1
limit = 250

# Add metrics:
# PRCP = Precipitation mm or inches as per user preference,
#        inches to hundredths
# SNOW = Snowfall mm or inches as per user preference inches to tenths
# SNWD = Snow depth mm or inches as per user preference inches
# TMAX = Maximum  temperature  (Fahrenheit  or  Celsius  as  per
#        user  preference,  Fahrenheit  to  tenths
metrics = {'PRCP': 'Precip', 'TMAX': 'Temp', 'SNOW': 'Snowfall',
           'SNWD': 'SnowAccum'}


def setupRequest(fromDate=None, toDate=None, offset=1, limit=250):

    # Grab API key from environment variable
    noaa_key = os.environ['NOAA']

    # NOAA endpoint for grabbing historical data
    url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data'

    # Setup Request object arguments
    headers = {'token': noaa_key}
    payload = {'stationid': 'GHCND:USC00214884', 'datasetid': 'GHCND',
               'datatypeid': list(metrics.keys()), 'startdate': fromDate,
               'enddate': toDate, 'units': 'standard', 'limit': limit,
               'offset': offset
               }

    # Run Requests, grab one chunk of data
    print("Getting report ... ")
    r = requests.get(url, headers=headers, params=payload)
    data = json.loads(r.text)

    return data


def getData(data):

    count = data['metadata']['resultset']['count']

    print(f'Grabbing {offset} through {offset + limit - 1} \
            of {count} records')

    if count <= limit:
        pass
    else:
        rows = []
        while offset + limit - 1 <= count:
            for result in data['results']:
                line.append(result['date'])
                line.append(result['value'])
            offset += limit

def sendToDatabase(rows):

    # Open or create Canoeing database
    conn = sqlite3.connect('canoeing.db')
    c = conn.cursor()

    # Create or refresh table
    c.execute('''
    CREATE TABLE IF NOT EXISTS Weather ("Date" DATE PRIMARY KEY, Precip REAL,
    Temp REAL, Snowfall REAL, SnowAccum REAL)''')

    c.execute('REPLACE INTO Weather ("Date", Precip) VALUES (?,?)',
              (date[:10], precip))

    c.execute('UPDATE Weather SET ' + metrics[result['datatype']]
              + ' = ? WHERE "Date" = ?', (val, date[:10]))

    conn.commit()
    c.close()
