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
    date = input("Date: ")
    mdy = date.split("/")
    if len(mdy) == 3:
        month, day, year = mdy
        if int(month) > len(months):
            continue
    mdy = date.split(",")
    if len(mdy) == 2:
        month, day = mdy[0].split(" ")
        year = mdy[1].strip()
        try:
            month = str(month.index(month))
        except ValueError:
            continue
    if None in [year, month, day]:
        continue
    print(f"{year}-{month:02}-{day:.02}")
