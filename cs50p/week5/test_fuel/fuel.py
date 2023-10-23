def main():
    while True:
        try:
            status = gauge(convert(input("Fraction: ").strip()))
        except (ValueError, ZeroDivisionError):
            continue

        print(status)
        break


def convert(fraction):
    x, y = fraction.split("/")
    return (int(x) / int(y)) * 100


def gauge(percentage):
    if percentage > 98:
        return "F"
    if percentage < 2:
        return "E"
    return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()