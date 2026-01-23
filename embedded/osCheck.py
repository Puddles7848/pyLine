import os

if os.name == "posix":
    import sys
    if sys.platform.startswith("linux"):
        basicOS = "linux"
        distroInfo = platform.freedesktop_os_release().get
        prettyOS = distroInfo("PRETTY_NAME") or distroInfo("NAME") or distroInfo.get("ID")
    elif sys.platform == "darwin":
        basicOS = "macos"
        prettyOS = "MacOS"+platform.mac_ver()[0]
    elif sys.platform.startswith("bsd"):
        basicOS = "bsd"
elif os.name == "nt":
    basicOS = "windows"
    import platform
    prettyOS = "Windows"+platform.release()
elif os.name == "java":
    basicOS = "Java"
    prettyOS = "Java Virtual Machine"
else:
    basicOS = "?"