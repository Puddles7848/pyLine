from pathlib import Path

with open("rootDir") as rootDirFile:
    rootDir = rootDirFile.read()

def ckPath(input):
    return Path(input).is_relative_to(rootDir)