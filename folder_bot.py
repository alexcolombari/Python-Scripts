# ------------------------------------------------------------
#   Author: Alex Colombari (http://github.com/alexcolombari)
#   Date: 2019-10-12
#   Create random folders in directory
# ------------------------------------------------------------

import os
import random
import string

def randomName(stringLength = 5):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def createFolders():
    folderNumber = 3
    try:
        for i in range(folderNumber):
            folderName = randomName()
            os.mkdir(folderName)
            print("Directory " + folderName + " created!")
    except OSError:
        print("Directory " +  folderName + " already exists")

createFolders()
