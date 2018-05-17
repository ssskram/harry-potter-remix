import csv
import os
import sys
import glob

master_f = "Ron"
master_l = "Weasley"

# get characters
ch = open("characters1.csv")
reader = csv.reader(ch)

# test
def test(line, row):
    print(line)
    print(row[0])

# swap function
def swapIt(line):
    for row in reader:   
        test(line, row)

# do it
os.chdir("/home/ssskram/other_repos/potter_remix/books/")
for file in glob.glob("*.txt"):
    with open(file, 'rb') as f:
        for line in f:
            print(line)
            swapIt(line)

    # with open("out.txt", "wt") as fout:
    # if row[0] is not None:
    #     old = row[0]
    #     print(old)
    #     # fout.write(line.replace(row[0], master_f))
    # if row[1] is not None:
    #     old = row[1]
    #     print(old)
    #     # fout.write(line.replace(row[1], ''))
    # if row[2] is not None:
    #     old = row[2]
    #     print(old)
    #     # fout.write(line.replace(row[1], master_l))