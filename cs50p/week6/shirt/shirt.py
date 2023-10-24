import os
import sys
from PIL import Image, ImageOps


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

    if os.path.splitext(sys.argv[2])[-1] != os.path.splitext(sys.argv[1])[-1]:
        sys.exit("Input and output have different extensions")

    before = ImageOps.fit(before, size=shirt.size)
    before.paste(shirt)
    before.save()


if __name__ == "__main__":
    main()