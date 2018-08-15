# https://darksky.net/dev/docs#time-machine-request
# Maybe rebuild forecast using Dark Sky? Seems so much better than Open Weather
# https://darksky.net/dev/docs
# The header has number of requests remaining info
# https://api.darksky.net/forecast/[key]/[latitude],[longitude]
# This table doesn't collect rain amounts, wtf
# I might be able to use precip intensity to model historical rainfall as long as I can match up dt stuff

import os
import requests
import json
import sqlite3

# Open or create Canoeing database
# conn = sqlite3.connect('canoeing.db')
# c = conn.cursor()

# # # Create or refresh table
# c.executescript('''
# DROP TABLE IF EXISTS ForecastDS;
# CREATE TABLE ForecastDS ("Date" DATE, Hour DATE, Precip REAL, Temp REAL, PRIMARY KEY ("DATE", Hour))''')

#I'm not really sure how to format the URL with sub-directories, I'll figure it out
dark_sky_key = os.environ['darksky']
latitude = 44.910925
longitude = -93.298157
exclude = ['currently','minutely','flags']
time = '1506945600' #'2018-08-01T12:00:00'

url = 'https://api.darksky.net/forecast/' + str(dark_sky_key) + '/' + str(latitude) + ',' + str(longitude) + ',' + time
payload = {'exclude': exclude}

r = requests.get(url, params = payload)
print(r.url)

data = r.json()

print(json.dumps(data, indent =4))

# conn.commit()
# c.close()