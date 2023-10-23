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
    if z > 100:
        return None
    if z < 2:
        return "E"
    if z > 98:
        return "F"
    return f"{percentage}%"


if __name__ == "__main__":
    main()