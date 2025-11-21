######################
### IMPORTANT INIT ###
######################
import subprocess # Call other scripts
import sys # Operating System
import os # Filesystem
import wget
from pathlib import Path # Filesystem^2
###############
### Colours ###
###############
RESET = "\033[0m"

COLORS = {
    "black": 30, "red": 31, "green": 32, "yellow": 33,
    "blue": 34, "magenta": 35, "cyan": 36, "white": 37,
    "bright_black": 90, "bright_red": 91, "bright_green": 92, "bright_yellow": 93,
    "bright_blue": 94, "bright_magenta": 95, "bright_cyan": 96, "bright_white": 97
}

# Generate functions: red("text"), bright_red("text"), etc.
def make_color_func(code):
    def f(text: str):
        return f"\033[{code}m{text}{RESET}"
    return f

for name, code in COLORS.items():
    globals()[name] = make_color_func(code)

# Usage:
# print(blue("Hello, world!"))

################
### OS Check ###
################
if sys.platform.startswith("linux"):
    prettyOS = "Linux"
elif sys.platform == "darwin":
    prettyOS = "MacOS"
elif sys.platform.startswith("win"):
    prettyOS = "Windows"
elif sys.platform.startswith("bsd"):
    prettyOS = "BSD"
elif sys.platform == "os2" or "os2emx":
    prettyOS = "OS/2"
elif sys.platform == "riscos":
    prettyOS = "RiscOS"
elif sys.platform == "atheos":
    prettyOS = "AtheOS"
elif sys.platform.startswith("aix"):
    prettyOS = "AIX"
else:
    prettyOS = "?"

os.system("clear")

print(bright_white("Host OS:"),blue(prettyOS))
if prettyOS != "Linux":
    print(yellow("[WARN]"),bright_white("Your OS is not supported! But it might still work."))
if prettyOS == "?":
    print(red("[FATAL] Your OS isn't Linux, MacOS, Windows, FreeBSD, OpenBSD, OS/2, RiscOS, AtheOS, or AIX... that shouldn't be possible!"))
    sys.exit("A fatal error occured.")

#############
### Files ###
#############
rootDir = Path(__file__).parent
print("Snakeline runs at:",rootDir)
