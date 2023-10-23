import os
import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    extension =
    for arg in sys.argv:
        if not is_valid(arg):
            sys.exit("Invalid input")


def is_valid(filename):
    if os.split.text(filename)[-1].lower() in [".jpg", ".jpeg", ".png"]:
        return True
    return False


if __name__ == "__main__":
    main()