# Translates CSV WU output back into the database
# open file
# add precip is it's the same date and hour
# if not, write it to the matrix
# write output to a new text file
# OOOOk. It looks like Precip is actually accumlated, so you would have to take the difference. FFS.


import csv
import sqlite3
from datetime import datetime

conn = sqlite3.connect('canoeing.db')
c = conn.cursor()

# Create or refresh table
c.execute('''
    CREATE TABLE IF NOT EXISTS WUHistoricalHourlyNew
    ("Date" DATE, "Time" DATE, PrecipInches REAL,
    PRIMARY KEY("Date","Time"))''')

with open('wudata.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    day = None
    time = None
    precip = 0
    row_total = []

    # Skip header
    next(csv_reader, None)

    for row in csv_reader:
        if day is None:
            day = row[0]
            time = row[1]
            precip = float(row[2])
            continue
        if row[0] == day and row[1] == time:
            precip += float(row[2])
        else:
            t1 = datetime.strptime(time, "%H")
            t2 = datetime.strftime(t1, "%H:%M:%S")
            d1 = datetime.strptime(day, "%m/%d/%Y")
            d2 = datetime.strftime(d1, "%Y-%m-%d")
            row_total.append([d2, t2, round(precip, 1)])
            day = row[0]
            time = row[1]
            precip = float(row[2])

for line in row_total:
    c.execute('''
        INSERT INTO WUHistoricalHourlyNew
        ("Date", "Time", "PrecipInches")
        VALUES (?,?,?)''', line)

conn.commit()
c.close()
