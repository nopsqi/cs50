import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    return re.search(r"^<iframe.*src=\"([^\"]+)\".*></iframe>$", s).groups(1)[0]


if __name__ == "__main__":
    main()