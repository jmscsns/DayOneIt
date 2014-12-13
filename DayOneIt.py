# Grabs files from a folder and creates DayOne entries
#
# It currently only deals with .jpgs (which it assumes are from Instagram) and .txt files
#
# Requires DayOne CLI be installed.
#
# This will delete processed files in the specified directory, use with care.
# NB Does not, for some reason, include the last file in the generated entry

import glob
import os

# Set directory
dir = '/Users/James/GitHub/DayOneIt/testfiles/'

# Create list of jpgs
ilist = glob.glob(dir + '*.jpg')
for i in ilist:
    # Run DayOne CLI
    os.system('echo "' + i[len(dir):-4:].replace("_", " ") + ' \n\n#instagram" | /usr/local/bin/dayone -p="' + i + '" new')
    # Remove created file
    os.remove(i)

#Create list of txts
tlist = glob.glob(dir + '*.txt')
for t in tlist:
    # Run DayOne CLI
    os.system('/usr/local/bin/dayone new < "' + t + '"')
    os.remove(t)




