import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    link = re.match(r"^<iframe.*src=\"([^\"]+)\".*></iframe>$", s)
    print(link.groups)


if __name__ == "__main__":
    main()