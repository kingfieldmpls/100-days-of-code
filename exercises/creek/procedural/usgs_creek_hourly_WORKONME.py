# Should I aggregate this data at all?
# It comes in 15 minute chunks, it seems like hourly would be just fine.

import logging
from statistics import mean

import requests
import sqlite3


def temp_conversion(celsius):
    tempF = int(round(float(celsius) * 9/5 + 32))
    return tempF


def setup_request(days=7, startDate=None, endDate=None):
    # Define parameters for GET header
    logger.info("Setting up report ...\n")

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


def get_data(data):

    logger.info("Getting data ...")

    rows = []

    # Traverse and parse JSON output to prepare for writing to DB
    for index, metric in enumerate(metrics):
        print(f"Grabbing metric {index+1} of {len(metrics)}")
        if metric == 1:
            current_date = None
            nums = []
            for interval in range(len(data['value']['timeSeries'][metric]
                                      ['values'][0]['value'])):
                if current_date is None:
                    current_date = current_date = data['value']['timeSeries'][metric]['values'][0]['value'][interval]['dateTime']
                if data['value']['timeSeries'][metric]['values'][0]['value'][interval]['dateTime'][:10] == current_date[:10] and data['value']['timeSeries'][metric]['values'][0]['value'][interval]['dateTime'][11:13] == current_date[11:13]:
                    nums.append(float(data['value']['timeSeries'][metric]['values'][0]['value'][interval]['value']))
                else:
                    if current_date is not None:
                        rows.append([metrics[metric], current_date, sum(nums)])
                        nums = []
                    current_date = data['value']['timeSeries'][metric]['values'][0]['value'][interval]['dateTime']
                    nums.append(float(data['value']['timeSeries'][metric]['values'][0]['value'][interval]['value']))
        else:
            current_date = None
            nums = []
            for interval in range(len(data['value']['timeSeries'][metric]
                                      ['values'][0]['value'])):
                if current_date is None:
                    current_date = current_date = data['value']['timeSeries'][metric]['values'][0]['value'][interval]['dateTime']
                if data['value']['timeSeries'][metric]['values'][0]['value'][interval]['dateTime'][:10] == current_date[:10] and data['value']['timeSeries'][metric]['values'][0]['value'][interval]['dateTime'][11:13] == current_date[11:13]:
                    nums.append(float(data['value']['timeSeries'][metric]['values'][0]['value'][interval]['value']))
                else:
                    rows.append([metrics[metric], current_date, round(mean(nums), 2)])
                    nums = []
                    current_date = data['value']['timeSeries'][metric]['values'][0]['value'][interval]['dateTime']
                    nums.append(float(data['value']['timeSeries'][metric]['values'][0]['value'][interval]['value']))

    return rows


def send_to_database(rows):

    # Open or create Creek database
    conn = sqlite3.connect('canoeing.db')
    c = conn.cursor()

    logger.info('Writing rows to the database')

    # Create or refresh table
    c.execute('''
        CREATE TABLE IF NOT EXISTS USGSCreekHourly
        ("Date" DATE, "Time" DATE, WaterTempF REAL, PrecipInches REAL,
        StreamFlowCubicFtSec REAL, GageHeightFt Real,
        PRIMARY KEY("Date", "Time"))''')

    for row in rows:

        if row[0] == "WaterTempF":
            row[2] = temp_conversion(row[2])

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
        0: "WaterTempF",  # Average - checking for outliers
        1: "PrecipInches",  # Sum - Data starts in 2018, I think?
        2: "StreamFlowCubicFtSec",  # Average
        3: "GageHeightFt",  # Average
    }

    # Enter any value for days back from current day
    # up to a max of 150. Set to None to run with specific dates
    days = 2

    # Or define specific dates. For whatever reason there
    # is a gap in data at the end of 2017 up to 3/15/18
    # Data starts 2010-03-15
    start = '2018-09-01'
    end = '2018-09-10'

    # Use days or star and end
    data = setup_request(startDate=start, endDate=end)
    rows = get_data(data)
    send_to_database(rows)
