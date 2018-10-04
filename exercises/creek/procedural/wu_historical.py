# convert times to 24 hr
# what does lambda do?
# convert dates back into 0 padded
# Where can I get more good Selenium training?
# Where can I learn more about the specific browser (Firefox) settings
# Add exceptions if the url isn't found or breaks somehow
# curious to see how much time each iteration takes
# TODO - Make data aggregate to the hour match the current db "New" version


import logging
import urllib.parse
from datetime import date, datetime, timedelta

import sqlite3
from bs4 import BeautifulSoup
from selenium import webdriver


def parseDate(url):
    parsedDate = (datetime.strptime(url
                  .rsplit('?', 1)[0]
                  .rsplit('/', 1)[1], '%Y-%m-%d')
                  .strftime('%Y-%m-%d'))

    return parsedDate


def constructTime(startDate, endDate):

    diff = endDate - startDate

    dates = []

    for i in range(diff.days + 1):
        dates.append('{x.year}-{x.month}-{x.day}'
                     .format(x=start_date + timedelta(i)))
    return dates


def setupSelenium():

    # Setup the profile.
    profile = webdriver.FirefoxProfile('C:/Users/RobMartin/AppData/Roaming/'
                                       'Mozilla/Firefox/Profiles/18xd5dcy.sel')
    # bury the logfile
    browser = webdriver.Firefox(profile, log_path='nul')

    return browser


def getRequests(dates):

    logger.info("Building date parameters")

    SeleniumURLs = []

    for day in dates:

        params = urllib.parse.urlencode({'req_city': 'Minneapolis',
                                         'req_state': 'MN',
                                         'req_statename': 'Minnesota',
                                         'eqdb.zip': 55409,
                                         'reqdb.magic': 1,
                                         'reqdb.wmo': '99999'
                                         })

        url = 'https://www.wunderground.com/history/daily/KMSP/date/' + day

        SeleniumURLs.append(url + '?' + params)

    return SeleniumURLs


def getData(URL, browser):

    logger.info("Grabbing table for one day")

    browser.get(URL)

    # Grab page source with BS4
    soup = BeautifulSoup(browser.page_source, 'lxml')

    # Check to make sure table loaded
    table_header = soup.find("city-history-observation")

    table_header_text = table_header.get_text()

    # If the table doesn't load, keep reloading the page
    while "No Data Recorded" in table_header_text:
        logger.info("Reloading table")
        browser.refresh()
        soup = BeautifulSoup(browser.page_source, 'lxml')
        table_header = soup.find("city-history-observation")
        table_header_text = table_header.get_text()

    table = soup.find(id="history-observation-table")

    rows = table.tbody.find_all('tr')

    return rows


def transformData(rows, urldate):

    logger.info("Transforming data")

    lines = []

    for row in rows:
        line = []

        items = row.find_all('ng-saw-cell-parser')

        for item in items:
                line.append(item.text.strip().replace('\n', ''))

        line = [line[i] for i in [0, 8]]
        if "0.0 in" not in line[1]:
            line.insert(0, urldate)
            line[1] = (datetime
                       .strptime(line[1], '%I:%M %p')
                       .strftime('%H:%M:%S'))
            line[2] = line[2].rsplit(" ", 1)[0]
            lines.append(line)

    return lines


def sendToDatabase(lines):

    # Open or create Creek database
    conn = sqlite3.connect('canoeing.db')
    c = conn.cursor()

    logger.info('Writing rows to the database')

    # Create or refresh table
    c.execute('''
        CREATE TABLE IF NOT EXISTS WUHistoricalHourly
        ("Date" DATE, "Time" DATE, PrecipInches REAL,
        PRIMARY KEY("Date","Time"))''')

    for line in lines:

        # Check if update or new row
        c.execute('''
            SELECT "Date" from WUHistoricalHourly
            WHERE "Date" = ? AND "Time" = ?''',
                  (line[0], line[1]))

        # Write data to the DB
        check = c.fetchone()
        if check is None:
            c.execute('''
                INSERT INTO WUHistoricalHourly
                ("Date", "Time", "PrecipInches")
                VALUES (?,?,?)''', line)
        else:
            c.execute('''
                UPDATE WUHistoricalHourly SET "PrecipInches" = ?
                WHERE "Date" = ? and "Time" = ?''',
                      (line[2], line[0], line[1]))
        conn.commit()

    c.close()


if __name__ == "__main__":

    # Setup logging to file and stdout
    logging.basicConfig(filename='creek.log', level=logging.INFO,
                        format='%(asctime)-.19s : %(module)s :'
                               '%(levelname)s : %(message)s')
    logger = logging.getLogger(__file__)
    logger.addHandler(logging.StreamHandler())

    start_date = date(2011, 3, 2)
    end_date = date(2014, 8, 3)  # 2018-7-31

    browser = setupSelenium()
    dates = constructTime(start_date, end_date)
    SeleniumURLs = getRequests(dates)

    for url in SeleniumURLs:
        rows = getData(url, browser)

        urldate = parseDate(url)

        lines = transformData(rows, urldate)

        sendToDatabase(lines)

    browser.close()
