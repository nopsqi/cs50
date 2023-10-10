from cs50 import SQL


def main():
    db = SQL("sqlite:///fiftyville.db")
    tables = db.execute("SELECT tbl_name FROM sqlite_master;")
    for table in tables:
        print(table)
        rows = db.execute("SELECT * FROM ? LIMIT 5;", table["tbl_name"])
        for row in rows:
            print(row)
        print()


if __name__ == "__main__":
    main()