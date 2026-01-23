# Import
import os
import subprocess
from pathlib import Path

os.system("clear") # idek.

# Find pyLine root.
rootDir = Path(__file__).parent
os.chdir(rootDir)
with open("rootDir", "w") as rootDirFile:
    rootDirFile.write(str(rootDir))

# Open /embedded/mkPath.py
#with open("embedded/mkPath.py") as mkPath:
#    exec(mkPath.read())

# Open colors.py
with open("embedded/colors.py") as colors:
    exec(colors.read())

# subprocess.run("python", mkPath(/scripts/pySH.py))