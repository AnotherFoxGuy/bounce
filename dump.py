import glob
import os
from os.path import isfile, join

files = glob.glob("src/*/**", recursive=True)

for f in files:
    if isfile(join(os.curdir, f)):
        print(f)