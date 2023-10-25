import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    return re.search(r"^a(.+)z$", s).groups(1)


if __name__ == "__main__":
    main()