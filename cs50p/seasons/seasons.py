import sys
from datetime import date
import inflect


def main():
    print(convert(input("Date of Birth")))
    # print(convert("2000-07-12"))


def convert(birth):
    p = inflect.engine()
    try:
        year, month, day = birth.split("-")
    except ValueError:
        sys.exit("Invalid date")

    return (p.number_to_words(round((date.today() - date(int(year), int(month), int(day))).total_seconds() / 60), andword="") + " minutes").capitalize()


if __name__ == "__main__":
    main()
