"""
9.4 Write a program to read through the mbox-short.txt and figure out who has
the sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""


handle = open("mbox-short.txt")

mydict = {}
bigname = None
bigcount = 0

for line in handle:
 	if line.startswith('From '):
 		words = line.split()
 		mydict[words[1]] = mydict.get(words[1],0) + 1

for k,v in mydict.items():
	if v > bigcount:
		bigname = k
		bigcount = v

print(bigname, bigcount)


