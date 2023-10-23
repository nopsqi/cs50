def main():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            z = int(x) / int(y)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if z > 1:
                continue
            if z < 0.02:
                print("E")
            elif z > 0.98:
                print("F")
            else:
                print(f"{(z * 100):.0f}%")
            break


def convert(fraction):
    


if __name__ == "__main__":
    main()