def main():
    ...


def convert(time):
    hour = time.split(":")[0]
    match time.split(" ")[-1]:
        case "a.m.":
            if 6 < hour < 9:
                return "breakfast time"
            if 


if __name__ == "__main__":
    main()