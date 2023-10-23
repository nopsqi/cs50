import os
import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    extension = 
    for arg in sys.argv:
        if os.split.text(arg)[-1].lower() not in [".jpg", ".jpeg", ".png"]:
            sys.exit("Invalid input")