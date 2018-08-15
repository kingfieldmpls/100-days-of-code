# notes and notes
# {
#   "id": 5037649,
#   "name": "Minneapolis",
#   "country": "US",
#   "coord": {
#     "lon": -93.26384,
#     "lat": 44.979969
#   }
# }
# list.rain
#   list.rain.3h Rain volume for last 3 hours, mm
# 1mm = (1/25.4) inches
# "rain": {"3h": 0.15}
# list.dt Time of data forecasted, unix, UTC
# Need to figure out what to do with these forecast times


import os
import requests
import json
import sqlite3

# Open or create Canoeing database
conn = sqlite3.connect('canoeing.db')
c = conn.cursor()

# # Create or refresh table
c.executescript('''
DROP TABLE IF EXISTS Forecast;
CREATE TABLE Forecast ("Date" DATE, Hour DATE, Precip REAL, Temp REAL, PRIMARY KEY ("DATE", Hour))''')

open_weather_key = os.environ['openweather']
url = 'https://api.openweathermap.org/data/2.5/forecast'
cityID = 5037649

payload = {
'id': cityID, 'units': 'imperial', 'APPID': open_weather_key
}

r = requests.get(url, params = payload)
data = r.json()

for item in data['list']:
	temp = item['main']['temp']
	if bool(item['rain']):
		precip = round(item['rain']['3h'] / 25.4, 4)
	else:
		precip = 0.000
	date = item['dt_txt']
	c.execute('INSERT OR REPLACE INTO Forecast ("Date", Hour, Precip, Temp) VALUES (?,?,?,?)',(date[:10], date[11:], precip, temp))

conn.commit()
c.close()






