import re
import sys


def main():
    # print(convert(input("Hours: ")))
    print(convert("9:00 AM to 5:00 PM"))


def convert(s):
    regex = r"(0?[0-9]|1[1-2])(?:\:([0-5][0-9]))? *(am|pm)"
    if (
        re.match(
            r"^" +  regex + r" to " + regex + r"$",
            s,
            re.IGNORECASE,
        )
        is None
    ):
        raise ValueError

    time = re.findall(regex, s, re.IGNORECASE)

    for i, t in enumerate(time):
        hour = int(t[0])
        minute = int(t[1]) if t[1] else 0
        meridiem = t[2]

        match meridiem:
            case "AM":
                hour = hour if hour != 12 else 0
            case "PM":
                hour = hour + 12 if hour != 12 else hour

        time[i] = f"{hour:02}:{minute:02}"

    return time[0] + " to " + time[1]



if __name__ == "__main__":
    main()
