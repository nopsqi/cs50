import os
import sys
from PIL import Image


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    shirt = Image.open("shirt.png")

    try:
        before = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Invalid input")

    extension = os.path.splitext(sys.argv[1])[-1]

    if os.path.splitext(sys.argv[2])[-1] != extension:
        sys.exit("Input and output have different extensions")

    try:
        after = Image.open(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Invalid input")

    print(dir(before))


if __name__ == "__main__":
    main()