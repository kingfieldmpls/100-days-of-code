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

import os
import requests
import json
import sqlite3

# Open or create Canoeing database
conn = sqlite3.connect('canoeing.db')
c = conn.cursor()

# Create or refresh table
c.execute('''
CREATE TABLE IF NOT EXISTS Weather ("Date" DATE PRIMARY KEY, Precip REAL, Temp REAL)''')

noaa_key = os.environ['NOAA']

headers = {'token': noaa_key}
payload = {
    'stationid': 'GHCND:USC00214884', 'datasetid': 'GHCND',
    'datatypeid': ['PRCP', 'TMAX'], 'startdate': '2018-07-01',
    'enddate': '2018-07-03', 'units': 'standard'
}

# https://www.ncdc.noaa.gov/cdo-web/api/v2/stations?datatypeid=EMNT&datatypeid=EMXT&datatypeid=HTMN

url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data'

r = requests.get(url, headers = headers, params = payload)

# Time to write to the DB - might need to handle pagination

data = json.loads(r.text)

print(json.dumps(data, indent=4))
