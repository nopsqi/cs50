import re
import sys


def main():
    # print(convert(input("Hours: ")))
    convert("9:00 AM to 5 PM")


def convert(s):
    time = re.match(r"(^1?[0-9])", s)


if __name__ == "__main__":
    main()