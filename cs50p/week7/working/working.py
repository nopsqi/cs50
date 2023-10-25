import re
import sys


def main():
    print(convert(input("Hours: ")))
    # print(convert("9:00 AM to 5 PM"))
    # convert("9:00 AM - 5 PM")


def convert(s):
    if (
        re.match(
            r"(0?[0-9]|1[1-2])(?:\:([0-5][0-9]))? *(am|pm) to (0?[0-9]|1[1-2])(?:\:([0-5][0-9]))? *(am|pm)",
            s,
            re.IGNORECASE,
        )
        is None
    ):
        raise ValueError("Invallid input")

    time = re.findall(r"(0?[0-9]|1[1-2])(?:\:([0-5][0-9]))? *(am|pm)", s, re.IGNORECASE)
    for i, t in enumerate(time):
        hour = int(t[0])
        minute = int(t[1]) if t[1] else 0
        meridiem = t[2].lower()

        if hour not in [5, 9]:
            raise ValueError("Hour must be 5 or 9")

        match meridiem:
            case "am":
                hour = hour if hour != 12 else 0
            case "pm":
                hour = hour + 12 if hour != 12 else hour

        time[i] = f"{hour:02}:{minute:02}"

    return f"{time[0]} to {time[1]}"


if __name__ == "__main__":
    main()
