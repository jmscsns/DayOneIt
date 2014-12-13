# Grabs all the files in a directory, consolidates them, chucks them in Day One.
# One day.
#
# Assumes files are *.txt and requires DayOne CLI be installed.
#
# This will delete all *.txt files in the specified directory, use with care.
# NB Does not, for some reason, include the last file in the generated entry

import glob
import os

# Set directory
dir = '/Users/James/GitHub/DayOneLogging/testfiles/'

# Create dummy text file
# This is a very inelegant way of getting around the failure to append the last file in the for loop

dummy = open(dir + 'zzzzz.txt', 'a')
dummy.write('There must be a better way than this')

# Create text chunks and append to final.txt
dlist = glob.glob(dir + '*.txt')
for i in dlist:
    h = '#### ' + i[len(dir):-4:].replace("_", " ").title()
    r = open(dir + 'final.txt', 'a')
    t = open(i, 'r')
    r.write(str(h) + '\n')
    r.write(t.read() + '\n\n')
    print i
    os.remove(i)

# Add some tags
open(dir + 'final.txt', 'a').write('\n\n#automated #log')

# Run DayOne CLI
os.system('/usr/local/bin/dayone -d="yesterday 23:59" new <"' + dir + 'final.txt"')

# Remove created file
os.remove(dir + 'final.txt')
