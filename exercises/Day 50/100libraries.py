# get a list of all the files
# open all .py files in a directory one at a time
# check for import lines
# grab after import until end of line
# clean
# write to a list
# remove dups
# https://stackabuse.com/python-list-files-in-a-directory/
# https://realpython.com/python-pathlib/
# https://docs.python.org/3/library/pathlib.html
# Doesn't really properly handle the from 'x import y' idiom

import re

from pathlib import Path

starting_dir = r'C:\Users\RobMartin\Desktop\100-days-of-code'
pattern = '*.py'
regex = r'import [^\s]*'
import_list = []

p = Path(starting_dir)

file_list = list(p.glob('**/*.py'))


for file in file_list:
    with file.open() as f:
        for line in f:
            a = re.search(regex, line)
            if a is not None:
                a = a.group(0)
                if a not in import_list:
                    import_list.append(a)

import_list.sort()

for line in import_list:
    print(line)

print(len(import_list))
