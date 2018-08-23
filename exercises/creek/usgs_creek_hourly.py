import requests
import sqlite3

# Open or create Creek database
conn = sqlite3.connect('canoeing.db')
c = conn.cursor()

# Create or refresh table
c.execute('''
CREATE TABLE IF NOT EXISTS CreekHourly ("Date" DATE PRIMARY KEY, Temp REAL, Precip REAL, FlowRate REAL, GageHeight Real, SpecConductance Real)''')

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

# Enter any value for days back from current day - up to a max of 150. Set to None to run with specific dates
days = None

# Or define specific dates. For whatever reason there is a gap in data at the end of 2017 up to 3/15/18
start = '2010-01-01'
end = '2018-08-12'

# Define parameters for GET header
if days:
    payload = {'format': 'json', 'indent': 'on', 'sites': '05289800', 'period': 'P' + str(days) + 'D', 'siteStatus': 'all'}
else:
    payload = {'format': 'json', 'indent': 'on', 'sites': '05289800', 'startDT': start, 'endDT': end, 'siteStatus': 'all'}

# Create response object
r = requests.get('http://waterservices.usgs.gov/nwis/iv/', params=payload)
print(r.text)

# Decode JSON
data = r.json()

# Traverse and parse JSON output to prepare for writing to DB
for metric in metrics:
    column = metrics[metric]
    if "Temp" in data['value']['timeSeries'][metric]['variable']['variableDescription']:
        for day in range(len(data['value']['timeSeries'][metric]['values'][0]['value'])):
            Date = data['value']['timeSeries'][metric]['values'][0]['value'][day]['dateTime']
            Temp = data['value']['timeSeries'][metric]['values'][0]['value'][day]['value']
            Temp = (float(Temp) * 9/5) + 32  # Convert to Farhrenheit
            c.execute('REPLACE INTO CreekHourly ("Date", Temp) VALUES (?,?)',(Date[:16], Temp))
    else:
        for day in range(len(data['value']['timeSeries'][metric]['values'][0]['value'])):
            Date = data['value']['timeSeries'][metric]['values'][0]['value'][day]['dateTime']
            value = data['value']['timeSeries'][metric]['values'][0]['value'][day]['value']
            c.execute('UPDATE CreekHourly SET ' + column + ' = ? WHERE "Date" = ?', (value, Date[:16]))

conn.commit()
c.close()
