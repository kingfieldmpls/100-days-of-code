from urllib import request
from bs4 import BeautifulSoup
import ssl
import re

total = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_44696.html"
html = request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

spans = soup("span")

for span in spans:
	nums = re.findall('[0-9]+', str(span))
	for num in nums:
		if int(num) > 0:
			total += int(num)

print(total)