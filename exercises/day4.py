from urllib import request, parse, error

f = request.urlopen('http://data.pr4e.org/romeo.txt')

counts = {}

for line in f:
	words = line.decode().split()
	for word in words:
		counts[word] = counts.get(word, 0) + 1

print(counts)