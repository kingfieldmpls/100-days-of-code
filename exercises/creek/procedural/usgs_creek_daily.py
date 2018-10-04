# This flow data retrieval is super awesome - here are the resources:
# https://help.waterdata.usgs.gov/faq/automated-retrievals
# https://waterservices.usgs.gov/rest/
#
# Site #05289800 - Lower St. Anthony Falls
#
# Functionality:
# + Visualize the output
#     -Color code based on whether or not it's good for canoeing
# + Try to make predictions based on how much rain falls, how high the creek is going to be for how long
#     -Then look at the weather forecast and predict (based on where the creek is now) how high it will be in the future
#     -Then compare those quesses to reality to improve the model
#
# FLOW                  CREEK CONDITION
# Less than 75 cfs      Poor
# 75 cfs - 150 cfs      Good
# Greater than 150 cfs  Dangerous
#
# 8/19/2017 - ~149 - we had to duck under some bridges
# 7/20/2016 - ~31.5 - we lost Cabe's phone, and it was very shallow in parts
#
# Obviously snow melt is a thing. The NOAA provides snow melt data that we could incoroporate
# or we could only look at data where all the snow has melted and look at how much the creek
# is likely to rise after a rainfall.
#
# How to model creek flow rate increases:
#    -https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2007WR006415
#    -https://www.researchgate.net/post/What_are_the_different_methods_to_calculate_discharge_of_a_catchment_area_using_rainfall_data
#
# TO DO:
# + Grab updated since when making the NOAA request
# + Move from procedural to OOP
# + Create another table with hourly granularity
#    - https://waterservices.usgs.gov/rest/IV-Service.html
#    - Returns 15 minute granularity
# + enable gzip
# + Grab snow melt from NOAA
# + Create a model using melt and rainfall to predict flow rate
# + A few bits of clean up from comments
# + Use NWS for forecast
# + change log level on geckodriver
# + add docstrings

import logging

import requests
import sqlite3


def temp_conversion(celsius):
    tempF = int(round(float(celsius) * 9/5 + 32))
    return tempF


def setup_request(days=7, startDate=None, endDate=None):
    # Define parameters for GET header
    if startDate:
        payload = {'format': 'json',
                   'indent': 'on',
                   'sites': '05289800',
                   'startDT': startDate,
                   'endDT': endDate,
                   'siteStatus': 'all'}
    else:
        payload = {'format': 'json',
                   'indent': 'on',
                   'sites': '05289800',
                   'period': 'P' + str(days) + 'D',
                   'siteStatus': 'all'}

    # Create response object
    r = requests.get('https://waterservices.usgs.gov/nwis/dv/', params=payload)

    # Decode JSON
    data = r.json()

    return data


def get_data(data):

    rows = []

    # Traverse and parse JSON output to prepare for writing to DB
    for metric in metrics.keys():
            for day in range(len(data['value']['timeSeries'][metric]
                                     ['values'][0]['value'])):
                Date = (data['value']['timeSeries'][metric]
                            ['values'][0]['value'][day]['dateTime'])
                Value = (data['value']['timeSeries'][metric]
                             ['values'][0]['value'][day]['value'])
                rows.append([metrics[metric], Date, Value])
    return rows


def send_to_database(rows):
    # Open or create Creek database
    conn = sqlite3.connect('canoeing.db')
    c = conn.cursor()

    logger.info('Writing rows to the database')

    # Create or refresh table
    c.execute('''
    CREATE TABLE IF NOT EXISTS USGSCreekDaily ("Date" DATE PRIMARY KEY,
        StreamFlowCubicFtSec REAL, WaterTempF REAL)''')

    for row in rows:

        if row[0] == "WaterTempF":
            row[2] = temp_conversion(row[2])

        # Check if update or new row
        c.execute('''
            SELECT "Date" from USGSCreekDaily WHERE "Date" = ?''',
                  (row[1][:10],))

        # Write data to the DB
        check = c.fetchone()
        if check is None:
            c.execute('''
                INSERT INTO USGSCreekDaily ("Date", ''' + row[0] + ''')
                VALUES (?,?)''', (row[1][:10], row[2]))
        else:
            c.execute('''
                UPDATE USGSCreekDaily SET ''' + row[0] + ''' = ?
                WHERE "Date" = ?''', (row[2], row[1][:10]))
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
    # 0: Max water temp
    # 1: Min water temp
    # 2: Mean water temp
    # 3: Mean Discharge, cubic feet per second
    # 4: Max Specific conductance, water,
    #    unfiltered, microsiemens per centimeter
    # 5: Min Specific conductance, water,
    #    unfiltered, microsiemens per centimeter
    # 6: Mean Specific conductance, water,
    #    unfiltered, microsiemens per centimeter

    metrics = {2: 'WaterTempF',
               3: 'StreamFlowCubicFtSec'}

    # Enter any value for days back from current day - up to a max of 150.
    # Set to None to run with specific dates
    days = 7

    # r define specific dates. For whatever reason there is a gap in data
    # at the end of 2017 up to 3/15/18
    start = '2018-03-05'
    end = '2018-09-21'

    data = setup_request(startDate=start, endDate=end)
    rows = get_data(data)
    send_to_database(rows)
