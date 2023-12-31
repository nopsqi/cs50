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
    houses = []
    for d in data:
        house = {k: v for k, v in d.items() if k not in ["student_name", "id"]}
        if house not in houses:
            houses.append(house)
    # for house in sorted(houses, key=lambda house: house["house"]):
    #     db.execute("INSERT INTO houses (house, head) VALUES (?, ?)", house["house"], house["head"])
    for d in data:
        # db.execute("INSERT INTO students (student_name) VALUES (?)", d["student_name"])
        house_id = db.execute("SELECT id FROM houses WHERE house = ?", d["house"])[0]["id"]
        db.execute("INSERT INTO assignment (student_id, house_id) VALUES (?, ?)", d["id"], house_id)


if __name__ == "__main__":
    main()