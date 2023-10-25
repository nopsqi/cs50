import re
import sys


def main():
    # print(convert(input("Hours: ")))
    convert("9:00 AM to 5 PM")


def convert(s):
    time = re.findall(r"(0?[0-9]|1[1-2])(?:\:([0-5][0-9]))? *(am|pm) to (0?[0-9]|1[1-2])(?:\:([0-5][0-9]))? *(am|pm)", s, re.IGNORECASE)
    print(time)
    return
    for i, t in enumerate(time):

        hour = int(t[0])
        minute = int(t[1]) if t[1] else 0
        meridiem = t[2].lower()

        match meridiem:
            case 'am':
                hour = hour if hour != 12 else 0
            case 'pm':
                hour = hour + 12 if hour != 12 else hour

        time[i] = f"{hour:02}:{minute:02}"
    print(time)


if __name__ == "__main__":
    main()