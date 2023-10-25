import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    return len(re.match(r"um", s, re.IGNORECASE).groups())


if __name__ == "__main__":
    main()