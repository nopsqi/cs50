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



if __name__ == "__main__":
    main()
