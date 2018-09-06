# Should I aggregate this data at all?

import logging

import requests
import sqlite3


def tempConversion(celsius):
    tempF = int(round(float(celsius) * 9/5 + 32))
    return tempF


def setupRequest(days=7, startDate=None, endDate=None):
    # Define parameters for GET header
    if startDate:
        payload = {'format': 'json',
                   'indent': 'on',
                   'sites': '05289800',
                   'startDT': start,
                   'endDT': end,
                   'siteStatus': 'all'}

    else:
        payload = {'format': 'json',
                   'indent': 'on',
                   'sites': '05289800',
                   'period': 'P' + str(days) + 'D',
                   'siteStatus': 'all'}

    # Create response object
    r = requests.get('http://waterservices.usgs.gov/nwis/iv/', params=payload)

    # Decode JSON
    data = r.json()

    return data


def getData(data):

    rows = []

    # Traverse and parse JSON output to prepare for writing to DB
    for metric in metrics:
        for day in range(len(data['value']['timeSeries'][metric]
                                 ['values'][0]['value'])):
            Date = (data['value']['timeSeries'][metric]
                        ['values'][0]['value'][day]['dateTime'])
            Value = (data['value']['timeSeries'][metric]
                         ['values'][0]['value'][day]['value'])
            rows.append([metrics[metric], Date, Value])

    return rows


def sendToDatabase(rows):

    # Open or create Creek database
    conn = sqlite3.connect('canoeing.db')
    c = conn.cursor()

    logger.info('Writing rows to the database')

    for row in rows:

        if row[0] == "WaterTempF":
            row[2] = tempConversion(row[2])

        # Create or refresh table
        c.execute('''
            CREATE TABLE IF NOT EXISTS USGSCreekHourly
            ("Date" DATE, "Time" DATE, WaterTempF REAL, PrecipInches REAL,
            StreamFlowCubicFtSec REAL, GageHeightFt Real,
            PRIMARY KEY("Date", "Time"))''')

        # Check if update or new row
        c.execute('''
            SELECT "Date" from USGSCreekHourly
            WHERE "Date" = ? AND "Time" = ?''',
                  (row[1][:10], row[1][11:19]))

        # Write data to the DB
        check = c.fetchone()
        if check is None:
            c.execute('''
                INSERT INTO USGSCreekHourly
                ("Date", "Time", ''' + row[0] + ''')
                VALUES (?,?,?)''', (row[1][:10], row[1][11:19], row[2]))
        else:
            c.execute('''
                UPDATE USGSCreekHourly SET ''' + row[0] + ''' = ?
                WHERE "Date" = ? and "Time" = ?''',
                      (row[2], row[1][:10], row[1][11:19]))
        conn.commit()

    c.close()


if __name__ == "__main__":

    # Setup logging to file and stdout
    logging.basicConfig(filename='creek.log', level=logging.INFO,
                        format='%(asctime)-.19s : %(module)s :'
                               '%(levelname)s : %(message)s')
    logger = logging.getLogger(__file__)
    logger.addHandler(logging.StreamHandler())

    # Key of metric values:
    # 0: Temperature, water, degrees Celsius
    # 1: Precipitation, total, inches
    # 2: Discharge, cubic feet per second
    # 3: Gage height, feet
    # 4: Specific conductance, water, unfiltered,
    #    microsiemens per centimeter at 25 degrees Celsius
    metrics = {
        0: "WaterTempF",
        1: "PrecipInches",
        2: "StreamFlowCubicFtSec",
        3: "GageHeightFt",
    }

    # Enter any value for days back from current day
    # up to a max of 150. Set to None to run with specific dates
    days = None

    # Or define specific dates. For whatever reason there
    # is a gap in data at the end of 2017 up to 3/15/18
    start = '2018-08-12'
    end = '2018-09-04'

    data = setupRequest(startDate=start, endDate=end)
    rows = getData(data)
    sendToDatabase(rows)
