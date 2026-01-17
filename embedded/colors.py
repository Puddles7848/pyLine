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
