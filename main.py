import os

def choice():
    return int(input('>>'))

try:
    os.mkdir("saves")
except FileExistsError:
    print()

import mainScreen