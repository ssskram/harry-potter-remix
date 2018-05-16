import csv
import os
import sys
import glob

master_f = "Ron"
master_l = "Weasley"

## refactor
# for each book
#   for each row in scv
#       

# main method
def parse (first, middle, last):
    os.chdir("/home/ssskram/other_repos/potter_remix/books/")
    for file in glob.glob("*.txt"):
        if first is not None:
            inplace_change( filename = file, old_string = first, new_string = master_f )
        if middle is not None:
            inplace_change( filename = file, old_string = middle, new_string = "" )
        if last is not None:
            inplace_change( filename = file, old_string = last, new_string = master_l )
    return

def inplace_change(filename, old_string, new_string):
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            return

    with open(filename, 'w') as f:
        s = s.replace(old_string, new_string)
        f.write(s)

# now get each character, and pass back to main
ch = open("characters.csv", "rb")
reader = csv.reader(ch)
for row in reader:
    parse( first = row[0], middle = row[1], last = row[2])

