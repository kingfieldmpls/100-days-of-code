import re

handle = open("rx.txt")

nums = []
count = 0

for line in handle:
	m = re.findall('[0-9]+', line)
	if len(m) > 0:
		nums.append(m)

for num in nums:
	for n in num:
		count += int(n)

print(count)

#and just for funzies, the list comprehension version. Seems like magic.
print(sum([int(n) for n in re.findall('[0-9]+', open("rx.txt").read())]))
