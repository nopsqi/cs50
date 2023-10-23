import os
import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if is_valid(sys.argv[1]):
        extension = os.split.text(sys.argv[1])[-1].lower()
    else:
        
    for arg in sys.argv:


def is_valid(filename):
    if os.split.text(filename)[-1].lower() in [".jpg", ".jpeg", ".png"]:
        return True
    return False


if __name__ == "__main__":
    main()