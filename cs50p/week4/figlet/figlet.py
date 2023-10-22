import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    font = random.choice(figlet.getFonts())
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    font = sys.argv[2]
else:
    sys.exit("usage: python figlet.py [-f, --f font]")


figlet.setFont(font=font)
print(figlet.renderText(input("Input: ")))