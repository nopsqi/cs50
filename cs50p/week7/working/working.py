import re
import sys


def main():
    print(convert(input("Hours: ")))


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

    if time[0][1] == time[1][1]:
        raise ValueError

    for i, t in enumerate(time):
        time[i] = f"{int(t[0]) if t[1] == 'AM' else int(t[0]) + 12:02}:00"

    return f"{time[0]} to {time[1]}"


if __name__ == "__main__":
    main()
