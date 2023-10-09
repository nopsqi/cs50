import csv
from cs50 import SQL


def main():
    db = SQL("sqlite:///roster.db")
    data = []
    with open("students.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["id"] = int(row["id"])
            data.append(row)
    for d in data:
        db.execute("INSERT INTO students (student_name) VALUES (?)", d["student_name"])


if __name__ == "__main__":
    main()