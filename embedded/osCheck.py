import os

if os.name == "posix":
    basicOS = "POSIX"
elif os.name == "nt":
    basicOS = "Windows"
elif os.name == "java":
    basicOS = "Java"
elif os.name not in {"POSIX","Windows","Java"}:
    basicOS = "?"
else:
    basicOS = "?"