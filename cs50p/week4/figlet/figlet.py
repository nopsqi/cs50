from pyfiglet import Figlet
import sys

if len(sys.argv) < 2:
    sys.exit("usage: python figlet.py [-f, --f font]")
if len(sys.argv) == 

figlet = Figlet()

print(figlet.getFonts())