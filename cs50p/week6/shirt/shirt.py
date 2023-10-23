import os
import sys
from PIL import Image


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    shirt = Image.open(")

    if not is_valid(sys.argv[1]):
        sys.exit("Invalid File")
    extension = os.path.splitext(sys.argv[1])[-1].lower()
    images = []

    for arg in sys.argv[1:]:
        if not is_valid(arg):
            sys.exit("Invalid File")
        if os.path.splitext(arg)[-1].lower() != extension:
            sys.exit("Input and output have diferent extensions")

        try:
            images.append(Image.open(arg))
        except FileNotFoundError:
            sys.exit(f"File {arg} doesn't exist")


def is_valid(filename):
    if os.path.splitext(filename)[-1].lower() in [".jpg", ".jpeg", ".png"]:
        return True
    return False


if __name__ == "__main__":
    main()