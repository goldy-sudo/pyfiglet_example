import pyfiglet
RED = '\033[91m'
END = '\033[0m'


ascii_art = pyfiglet.figlet_format("goldy")
print(RED,ascii_art,END)
