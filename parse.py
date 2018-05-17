import csv
import os
import glob

Ron = "Ron"
Weasley = "Weasley"

# main swapping function
def swap(character):

    # collect casings of first name
    fc = []
    fc.append(character[0])
    fc.append(character[0].upper())

    # ..of middle name
    mc = []
    mc.append(character[1])
    mc.append(character[1].upper())

    # ..of last name
    lc = []
    lc.append(character[2])
    lc.append(character[2].upper())

    # for each book
    for file in glob.glob("*.txt"):

        # swap first names
        for c in fc:
            if c != '':
                with open(file) as fin:
                    new = fin.read().replace(c, Ron)
                with open(file, "w") as fout:
                    fout.write(new)
                fin.close()
                fout.close()

        # swap middle names
        for c in mc:
            if c != '':
                with open(file) as fin:
                    new = fin.read().replace(c, '')
                with open(file, "w") as fout:
                    fout.write(new)
                fin.close()
                fout.close()

        # swap last names
        for c in lc:
            if c != '':
                with open(file) as fin:
                    new = fin.read().replace(c, Weasley)
                with open(file, "w") as fout:
                    fout.write(new)
                fin.close()
                fout.close()

# get characters
ch = open("characters.csv")
reader = csv.reader(ch)
characters = []
for row in reader:
    characters.append(row)
ch.close()

# navigate to books
os.chdir("/home/ssskram/other_repos/potter_remix/books/")

# for each character, pass back to main
for character in characters:
    swap(character)