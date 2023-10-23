def main():
    while True:
        try:
            percent = convert(input("Fraction: ").strip())
            status = gauge(percent)
        except (ValueError, ZeroDivisionError):
            continue

        print(status)
        break


def convert(fraction):
    x, y = fraction.split("/")
    return int(x) / int(y)


def gauge(percentage):
    if z > 1:
        continue
    if z < 0.02:
        print("E")
    elif z > 0.98:
        print("F")
    else:
        print(f"{(z * 100):.0f}%")
    break


if __name__ == "__main__":
    main()