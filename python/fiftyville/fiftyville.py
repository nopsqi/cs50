from cs50 import SQL


def main():
    db = SQL("sqlite:///fiftyville.db")
    tables = db.execute("SELECT name FROM sqlite_master;")
    for table in tables:
        print(table)
        db.execute("SELECT * FROM ? LIMIT 5;", table["name"])
        break
    db.execute("SELECT * FROM crime_scene_reports LIMIT 5;")


if __name__ == "__main__":
    main()