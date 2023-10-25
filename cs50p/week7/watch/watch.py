import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        link = re.search(r"^<iframe.*src=\"([^\"]+)\".*></iframe>$", s).groups(1)[0]
    except IndexError:
        return None

    


if __name__ == "__main__":
    main()