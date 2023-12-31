def main():
    time = convert(input("What time is it? ").strip().lower())
    if 6.9 < time < 9.1:
        print("breakfast time")
    elif 11.9 < time < 14.1:
        print("lunch time")
    elif 17.9 < time < 20.1:
        print("dinner time")

def convert(time):
    hour, minute = time.split(":")
    hour = float(hour)
    minute = float(minute.split(" ")[0])

    match time.split(" ")[-1]:
        case "a.m.":
            if hour == 12:
                hour = 0
        case "p.m.":
            if hour != 12:
                hour += 12

    return hour + (minute / 60)


if __name__ == "__main__":
    main()