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
# To Do:
# - Double check what kind of time is coming in - it's supposed to be local
# - Comments
# - Docstrings
# - Unit tests
# - Deal with null rows
# - Add a function that deals with all of the conversions

import logging
import sys

import requests
import sqlite3


def temp_conversion(celsius):
    tempF = int(round(float(celsius) * 9/5 + 32))
    return tempF


def length_conversion(mm):
    lengthInch = float(mm * 0.0393700787)
    return lengthInch


def setup_request():
    # Create response object in includes station code and gridpoints
    r = requests.get('https://api.weather.gov/gridpoints/MPX/109,67')

    # Decode JSON
    data = r.json()

    return data


def get_data(data, metrics):

    rows = []

    if "ForecastGridExpired" in data['type']:
        logger.warning("Weather forecast has expired.")
        sys.exit()
    else:
        for prop in data['properties']:
            if prop in list(metrics.keys()):
                    for val in range(len(data['properties'][prop]['values'])):
                        Date = data['properties'][prop]['values'][val]['validTime']
                        Value = data['properties'][prop]['values'][val]['value']
                        rows.append([prop, Date, Value])
    return rows


def send_to_database(rows):
    # Open Canoeing database
    conn = sqlite3.connect('canoeing.db')
    c = conn.cursor()

    # Create or refresh table
    c.execute('DROP TABLE IF EXISTS NWSForecast')

    # Create or refresh table
    c.execute('''
    CREATE TABLE NWSForecast ("Date" DATE, "Time" DATE, TempF REAL,
        PrecipChance REAL, PrecipInches REAL, IceAccumInches REAL,
        SnowAccumInches REAL, SnowLevelFeet REAL,
        PRIMARY KEY("Date","Time"))''')

    logger.info('Writing rows to the database')

    for row in rows:
        column = metrics[row[0]]

        if row[0] == "temperature":
            row[2] = temp_conversion(row[2])
        elif row[0] == "snowLevel":
            # converts meters to feet
            row[2] = length_conversion(row[2]) * 1000 / 12
        elif row[0] in ["quantitativePrecipitation",
                        "iceAccumulation",
                        "snowfallAmount"]:
            row[2] = length_conversion(row[2])

        # Check if update or new row
        c.execute('''
            SELECT "Date" from NWSForecast WHERE "Date" = ? AND "Time" = ?''',
                  (row[1][:10], row[1][11:19]))

        # Write data to the DB
        check = c.fetchone()
        if check is None:
            c.execute('''
                INSERT INTO NWSForecast ("Date", "Time",''' + column + ''')
                VALUES (?,?,?)''', (row[1][:10], row[1][11:19], row[2]))
        else:
            c.execute('''
                UPDATE NWSForecast SET ''' + column + ''' = ?
                WHERE "Date" = ? and "Time" = ?''', (row[2], row[1][:10],
                                                     row[1][11:19]))
        conn.commit()

    c.close()


if __name__ == "__main__":

    # Setup logging to file and stdout
    logging.basicConfig(filename='creek.log', level=logging.INFO,
                        format='%(asctime)-.19s : %(module)s :'
                               '%(levelname)s : %(message)s')
    logger = logging.getLogger(__file__)
    logger.addHandler(logging.StreamHandler())

    metrics = {'temperature': 'TempF',
               'probabilityOfPrecipitation': 'PrecipChance',
               'quantitativePrecipitation': 'PrecipInches',
               'iceAccumulation': 'IceAccumInches',
               'snowfallAmount': 'SnowAccumInches',
               'snowLevel': 'SnowLevelFeet'}

    data = setup_request()
    rows = get_data(data, metrics)
    send_to_database(rows)
