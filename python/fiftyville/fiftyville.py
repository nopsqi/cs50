from cs50 import SQL


def main():
    db = SQL("sqlite:///fiftyville.db")
    tables = db.execute("SELECT name FROM sqlite_master;")
    for table in tables:
        db.execute("SELECT * FROM ? LIMIT 5", table["name"])
        break


if __name__ == "__main__":
    main()