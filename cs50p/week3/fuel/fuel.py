
while True:
    try:
        x, y = input("Fraction: ").split("/")
        z = int(x) / int(y)
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if z > 1:
            continue
        if z < 2:
            print("E")
        elif z > 0.99:
            print("F")
        else:
            print(f"{(z * 100):.0f}%")
        break