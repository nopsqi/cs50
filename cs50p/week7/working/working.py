import re
import sys


def main():
    # print(convert(input("Hours: ")))
    convert("9:00 AM to 5 PM")


def convert(s):
    time = re.findall(r"(0?[0-9]|1[1-2])(?:\:([0-5][0-9]))? *(am|pm)", s, re.IGNORECASE)
    for i, t in enumerate(time):
        if t[0] not in [5, 9]:
            raise ValueError
        hour = int(t[0])
        munute = int(t[0]) if t[0] else 0
        
        match t[2].lower():
            case am:
                hour = t[0] if t[0] !=


if __name__ == "__main__":
    main()