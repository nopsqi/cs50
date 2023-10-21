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
    if len(date.split("/")) == 3:
