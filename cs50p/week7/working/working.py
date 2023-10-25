import re
import sys


def main():
    # print(convert(input("Hours: ")))
    print(convert("9:00 AM to 5 PM"))
    # convert("9:00 AM - 5 PM")


def convert(s):
    regex = r"(0?(?:5|9))(?:\:00)? *(am|pm)"
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
        time[i] = f"{int(t[0]) if t[1] == 'AM' else int(t[0]) + 12:02}:00"

    return f"{time[0]} to {time[1]}"


if __name__ == "__main__":
    main()
