#The program will prompt for a URL, read the XML data from that URL
#using urllib and then parse and extract the comment counts from
#the XML data, compute the sum of the numbers in the file. 

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

total = 0
ct = 0

#open up url and read contents into a string
with urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_44698.xml') as f:
	fp = f.read().decode()

tree = ET.fromstring(fp)

counts = tree.findall('.//count')

for i, count in enumerate(counts):
	total += int(counts[i].text)

print(total)

