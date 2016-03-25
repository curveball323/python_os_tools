#This script creates folders for every single file within a directory.
#Directions: Place the script in the same directory with the files run the script
#Created by: Bryce Johnson 24Mar2016

import os
import shutil

cwdirectory = os.getcwd()
files = os.listdir(cwdirectory)

for x in files:
    path = os.path.join(cwdirectory, str(x))
    fpath = os.path.splitext(path)
    os.mkdir(fpath[0])
    shutil.move(path, fpath[0])
