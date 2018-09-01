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
#
# To Do Here:
# - Write docstrings
# - Write various unit tests
# - Write helpful comments
# - Write methods for command line arguments

import json
import os

import requests
import sqlite3

# Add metrics:
# PRCP = Precipitation mm or inches as per user preference,
#        inches to hundredths
# SNOW = Snowfall mm or inches as per user preference inches to tenths
# SNWD = Snow depth mm or inches as per user preference inches
# TMAX = Maximum  temperature  (Fahrenheit  or  Celsius  as  per
#        user  preference,  Fahrenheit  to  tenths
metrics = {'PRCP': 'PrecipInches', 'TMAX': 'TempF', 'SNOW': 'SnowfallInches',
           'SNWD': 'SnowAccumInches'}


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
    print('Getting report ... ')
    r = requests.get(url, headers=headers, params=payload)
    data = json.loads(r.text)

    return data


def getData(data):

    if count < limit + offset:
        print(f'Grabbing {offset} through {count} of {count} records')
    else:
        print(f'Grabbing {offset} through {offset + limit - 1} of {count} records')

    rows = []

    for result in data['results']:
        line = []
        line.append(result['date'])
        line.append(result['datatype'])
        line.append(result['value'])
        rows.append(line)

    return rows


def sendToDatabase(rows):

    # Open Canoeing database
    conn = sqlite3.connect('canoeing.db')
    c = conn.cursor()

    # Create or refresh table
    c.execute('''
    CREATE TABLE IF NOT EXISTS NOAAWeatherHistorical
    ("Date" DATE PRIMARY KEY, PrecipInches REAL,
    TempF REAL, SnowfallInches REAL, SnowAccumInches REAL)''')

    print('Writing rows to the database')

    for row in rows:
        column = metrics[row[1]]

        # Check if update or new row
        c.execute('''
            SELECT "Date" from NOAAWeatherHistorical WHERE "Date" = ?''',
                  (row[0][:10],))

        # Write data to the DB
        check = c.fetchone()
        if check is None:
            c.execute('''
                INSERT INTO NOAAWeatherHistorical ("DATE",''' + column + ''')
                VALUES (?,?)''', (row[0][:10], row[2]))
        else:
            c.execute('''
                UPDATE NOAAWeatherHistorical SET ''' + column + ''' = ?
                WHERE "DATE" = ?''', (row[2], row[0][:10]))
        conn.commit()

    c.close()


# Run my main program here
startdate = '2018-08-01'
enddate = '2018-08-31'

data = setupRequest(startdate, enddate)

count = data['metadata']['resultset']['count']
offset = data['metadata']['resultset']['offset']
limit = data['metadata']['resultset']['limit']

if count <= limit:
    rows = getData(data)
    sendToDatabase(rows)

else:
    rows = getData(data)
    sendToDatabase(rows)
    offset += limit
    while offset <= count:
        data = setupRequest(startdate, enddate, offset)
        rows = getData(data)
        sendToDatabase(rows)
        offset += limit

print(f'Finished writing to database.\nCompleted {count} records')
