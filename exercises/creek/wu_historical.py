# convert times to 24 hr
# what does lambda do?
# convert dates back into 0 padded
# Where can I get more good Selenium training?
# Where can I learn more about the specific browser (Firefox) settings
# Add exceptions if the url isn't found or breaks somehow
# curious to see how much time each iteration takes
# how soon does data enter historical?
# add comments to follow the progress
# need exception when the historical table doesn't load to reload the table and try again a few times

from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import sqlite3
from datetime import date, timedelta

start_date = date(2018, 8, 20)  # Back loaded from 2010
end_date = date(2018, 8, 22)

diff = end_date - start_date

dates = []

for i in range(diff.days + 1):
    dates.append('{x.year}-{x.month}-{x.day}'.format(x=start_date + timedelta(i)))

conn = sqlite3.connect('canoeing.db')
c = conn.cursor()

# Setup the profile.
profile = webdriver.FirefoxProfile('C:/Users/RobMartin/AppData/Roaming/Mozilla/Firefox/Profiles/18xd5dcy.sel')
browser = webdriver.Firefox(profile, log_path='nul')

# Create or refresh table
c.execute('''
CREATE TABLE IF NOT EXISTS WeatherHistoricalHourly ("Date" DATE, "Time" DATE, Precip REAL, PRIMARY KEY("Date","Time"))''')

for date in dates:

    payload = {'req_city': 'Minneapolis', 'req_state': 'MN',
               'req_statename': 'Minnesota', 'eqdb.zip': 55409, 'reqdb.magic': 1,
               'reqdb.wmo': '99999'
               }

    url = 'https://www.wunderground.com/history/daily/KMSP/date/' + date

    r = requests.get(url, params=payload)

    surl = r.url

    browser.get(surl)

    soup = BeautifulSoup(browser.page_source, 'lxml')

    table_header = soup.find("city-history-observation")

    table_header_text = table_header.get_text()

    while "No Data Recorded" in table_header_text:
        browser.refresh()
        soup = BeautifulSoup(browser.page_source, 'lxml')
        table_header = soup.find("city-history-observation")
        table_header_text = table_header.get_text()

    table = soup.find(id="history-observation-table")

    headers = table.find_all('ngsaw-header')

    rows = table.tbody.find_all('tr')

    for row in rows:
        line = []
        line.append(date)
        items = row.find_all('ng-saw-cell-parser')

        for item in items:
                line.append(item.text.strip().replace('\n', ''))

        line = [line[i] for i in [0, 1, 9]]
        if "0.0 in" not in line[2]:
            c.execute('REPLACE INTO WeatherHistoricalHourly ("Date", "Time", Precip) VALUES (?,?,?)',line)
        conn.commit()

browser.close()
c.close()
