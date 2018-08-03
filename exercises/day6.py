# The program will prompt for a URL, read the JSON data from that URL
# using urllib and then parse and extract the comment counts from the
# JSON data, compute the sum of the numbers in the file and enter the sum below:

from urllib import request, parse, error
import json

total = 0

url = "http://py4e-data.dr-chuck.net/comments_44699.json"

with request.urlopen(url) as source:
	source = source.read()
	source = json.loads(source)
	for comment in source["comments"]:
		total += comment["count"]

print(total)