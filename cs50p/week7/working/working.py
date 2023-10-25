import re
import sys


def main():
    # print(convert(input("Hours: ")))
    convert("9:00 AM to 5 PM")


def convert(s):
    time = re.findall(r"(0?[0-9]|1[1-2])", s)
    print(time)


if __name__ == "__main__":
    main()