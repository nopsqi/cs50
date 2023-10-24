import os
import sys
from PIL import Image


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    shirt = Image.open("shirt.png")

    if not is_valid(sys.argv[1]):
        sys.exit("Invalid input")
    try:
        before = Image.open()
    except FileNotFoundError:
        sys.exit()


def is_valid(filename):
    if os.path.splitext(filename)[-1].lower() in [".jpg", ".jpeg", ".png"]:
        return True
    return False


if __name__ == "__main__":
    main()