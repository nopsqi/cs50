import csv
from cs50 import SQL


def main():
    db = SQL("sqlite:///roster.db")
    data = []
    with open("students.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            


if __name__ == "__main__":
    main()