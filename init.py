# Import
import os
import sys
import subprocess
from pathlib import Path

if os.name == "nt":
    print("Your OS is not supported.")
    sys.exit("Your OS is not POSIX compliant.")

os.system("clear") # idek.

# Find root.
rootDir = Path(__file__).parent
print("[INFO] pyLine's root directory is:",rootDir)

# Define pyLine's paths.
def mkPath(path):
    if os.path.isabs(path) == True:
        return os.path.join(rootDir,path.lstrip("/"))
    elif os.path.isabs(path) != True:
        return os.path.join(os.getcwd(),path.lstrip("/"))

# Open colors.py
with open(mkPath("/scripts/colors.py")) as colors:
    exec(colors.read())

subprocess.run("python", mkPath(/scripts/pySH.py))