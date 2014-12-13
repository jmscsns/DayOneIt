# Grabs jpgs in a folder and creates a Day One entry with image using the filename as the text.
#
# Requires DayOne CLI be installed.
#
# This will delete all *.jpg files in the specified directory, use with care.
# NB Does not, for some reason, include the last file in the generated entry

import glob
import os

# Set directory
dir = '/Users/James/GitHub/InstaDayOne/testfiles/'

# Create list of jpgs
dlist = glob.glob(dir + '*.jpg')
for i in dlist:
    # Run DayOne CLI
    print '/usr/local/bin/dayone -p="' + i + '" new < ' + '"' + dir + 'inst.txt"'
    os.system('echo "' + i[len(dir):-4:].replace("_", " ") + ' \n\n#instagram" | /usr/local/bin/dayone -p="' + i + '" new')
    # Remove created file
    os.remove(i)



