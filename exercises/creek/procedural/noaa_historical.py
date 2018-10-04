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
# To Do Here:
# - Write various unit tests
# - Write methods for command line arguments
# - There's probasbly one more layer of abstraction in the main function

import json
import logging
import os

import requests
import sqlite3

<<<<<<< HEAD
metrics = {'PRCP': 'PrecipInches',
           'TMAX': 'TempF',
           'SNOW': 'SnowfallInches',
           'SNWD': 'SnowAccumInches'}

logging.basicConfig(filename='creek.log', level=logging.INFO,
                    format='%(asctime)-.19s : %(module)s :'
                           '%(levelname)s : %(message)s')
logger = logging.getLogger(__file__)
logger.addHandler(logging.StreamHandler())

count =1
offset =1
limit = 1

=======
>>>>>>> 8385fc367122e629345e204e651cdf1bed54bbe8

def setup_request(fromDate, toDate, offset=1, limit=250):
    """ Makes API call to NOAA enpoint and returns JSON data.

    Pulls in API key defined as an environment variable and metrics
    defined in the main body of the script. Makes Requests call to
    NOAA endpoint. Data set, station ID and units hard coded into
    the payload. Limted to a one year range.

    Args:
        fromDate (str): Required. Accepts valid ISO formated date
                        (YYYY-MM-DD) or# date time (YYYY-MM-DDThh:mm:ss)
        toDate (str): Required. Formatted like 'YYYY-MM-DD'.
        offset (int): Defaults to 1.
        limit (int): Defaults to 250.

    Returns:
        JSON: NOAA data from Requests object.
    """

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
    logger.info('Getting report ... ')
    try:
        r = requests.get(url, headers=headers, params=payload)
        r.raise_for_status()
    except Exception:
        logger.exception('API Call Failed')

<<<<<<< HEAD
    print(r.text)
    print(type(r.text))

=======
>>>>>>> 8385fc367122e629345e204e651cdf1bed54bbe8
    data = json.loads(r.text)

    return data


def get_data(data):
    """ Parses NOAA JSON data for SQL insertion.

    Due to the nature of the endpoint, grabs date, datatype and value
    from the JSON results and writes to individual lines.

    Args:
        data (JSON string): Required. Output from Requests object.

    Returns:
        list of lists: One line for each day of each metric.
    """

    if count < limit + offset:
        logger.info(f'Grabbing {offset} through {count} of {count} records')
    else:
        logger.info(f'Grabbing {offset} through {offset + limit - 1}'
                    ' of {count} records')

    rows = []

    for result in data['results']:
        line = []
        line.append(result['date'])
        line.append(result['datatype'])
        line.append(result['value'])
        rows.append(line)

    return rows


def send_to_database(rows):
    """ Writes NOAA data to SQL database.

    Checks if the table exists and creates if not. Checks if the current
    date is already in the db. If not, creates a new row. If yes, updates
    into the existing row. Commits after each row for restartability.

    Args:
        rows (list of lists): Required. Passed from parsing of Requests output.
    """

    # Open Canoeing database
    conn = sqlite3.connect('canoeing.db')
    c = conn.cursor()

    # Create or refresh table
    c.execute('''
    CREATE TABLE IF NOT EXISTS NOAAWeatherHistorical
    ("Date" DATE PRIMARY KEY, PrecipInches REAL,
    TempF REAL, SnowfallInches REAL, SnowAccumInches REAL)''')

    logger.info('Writing rows to the database')

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


# Run main program here
if __name__ == "__main__":
<<<<<<< HEAD
=======
    # Setup logging to file and stdout
    logging.basicConfig(filename='creek.log', level=logging.INFO,
                        format='%(asctime)-.19s : %(module)s :'
                               '%(levelname)s : %(message)s')
    logger = logging.getLogger(__file__)
    logger.addHandler(logging.StreamHandler())

>>>>>>> 8385fc367122e629345e204e651cdf1bed54bbe8
    # Add metrics:
    # PRCP = Precipitation mm or inches as per user preference,
    #        inches to hundredths
    # SNOW = Snowfall mm or inches as per user preference inches to tenths
    # SNWD = Snow depth mm or inches as per user preference inches
    # TMAX = Maximum  temperature  (Fahrenheit  or  Celsius  as  per
    #        user  preference,  Fahrenheit  to  tenths
<<<<<<< HEAD

    startdate = '2018-09-20'
    enddate = '2018-09-21'
=======
    metrics = {'PRCP': 'PrecipInches',
               'TMAX': 'TempF',
               'SNOW': 'SnowfallInches',
               'SNWD': 'SnowAccumInches'}
    startdate = '2018-08-01'
    enddate = '2018-08-31'
>>>>>>> 8385fc367122e629345e204e651cdf1bed54bbe8

    data = setup_request(startdate, enddate)

    count = data['metadata']['resultset']['count']
    offset = data['metadata']['resultset']['offset']
    limit = data['metadata']['resultset']['limit']

    if count <= limit:
        rows = get_data(data)
        send_to_database(rows)

    else:
        rows = get_data(data)
        send_to_database(rows)
        offset += limit
        while offset <= count:
            data = setup_request(startdate, enddate, offset)
            rows = get_data(data)
            send_to_database(rows)
            offset += limit

    logger.info(f'Finished writing to database.\nCompleted {count} records')
