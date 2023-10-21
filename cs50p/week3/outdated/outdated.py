months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    year = month = day = None
    date = input("Date: ").strip()
    mdy = date.split("/")
    if len(mdy) == 3:
        month, day, year = mdy
    mdy = date.split(",")
    if len(mdy) == 2:
        month, day = mdy[0].split(" ")
        year = mdy[1].strip()
        try:
            month = month.index(month.capitalize())
        except ValueError:
            continue
    if None in [year, month, day]:
        continue
    try:
        year = int(year)
        month = int(month)
        day = int(day)
    except ValueError:
        continue

    if month > 12 or day > 30:
        continue

    print(f"{year}-{month:02}-{day:02}")
    break
