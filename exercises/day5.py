from urllib import request, parse, error
from bs4 import BeautifulSoup
import ssl

count = 7

url = "http://py4e-data.dr-chuck.net/known_by_Tay.html"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while count > 0:
	links = []
	html = request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')

	# Retrieve all of the anchor tags
	tags = soup('a')

	for tag in tags:
	    links.append(tag.get('href', None))

	url = links[17]
	count -= 1

print(links[17])
