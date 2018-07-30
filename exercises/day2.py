"""
10.2 Write a program to read through the mbox-short.txt and figure out
the distribution by hour of the day for each of the messages. You can
pull the hour out from the 'From ' line by finding the time and then
splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""

handle = open("mbox-short.txt")

mylist = []
mydict = {}

for line in handle:
 	if line.startswith('From '):
 		words = line.split(':')
 		mylist.append(words[0][-2:])

for hour in mylist:
	mydict[hour] = mydict.get(hour,0) + 1

for key, value in sorted(mydict.items()):
	print(key, value)	