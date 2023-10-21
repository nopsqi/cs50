def main():
    convert(input("What time is it? ").strip().lower())
    if 6 < hour < 9:
                print("breakfast time")
            elif 11 < hour < 14:
                print("lunch time")
            elif 17 < hour < 20:
                print("dinner time")

def convert(time):
    hour, minute = time.split(":")
    hour = int(hour)
    minute = float(minute.split(" ")[0])
    match time.split(" ")[-1]:
        case "a.m.":
            if 6 < hour < 9:
                print("breakfast time")
        case "p.m.":
            if hour == 12 and hour == 1:
                print("lunch time")
            elif 5 < hour < 8:
                print("dinner time")
        case _:



if __name__ == "__main__":
    main()