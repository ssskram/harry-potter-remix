import csv
import os
import sys
import glob

master_f = "Ron"
master_l = "Weasley"

# get characters
ch = open("characters1.csv")
reader = csv.reader(ch)
characters = []
for row in reader:
    characters.append(row)
ch.close()

# do it
os.chdir("/home/ssskram/other_repos/potter_remix/books/")
for file in glob.glob("*.txt"):
    with open(file) as f:
        for line in f:
            for i in characters:   
                with open("out.txt", "wt") as fout:
                    if i[0] != "":
                        old = i[0]
                        fout.write(line.replace(old, master_f))
                    if i[1] != "":
                        old = i[1]
                        fout.write(line.replace(old, ''))
                    if i[2] != "":
                        old = i[2]
                        fout.write(line.replace(old, master_l))
