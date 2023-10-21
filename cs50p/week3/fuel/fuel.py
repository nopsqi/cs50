
while True:
    try:
        x, y = input("Fraction: ").split("/")
        z = int(x) / int(y)
    except Exception:
        pass
    else:
        if z < 2:
            print("F")
        elif z == 0:
            print("E")
        else:
            print(f"{(z * 100):.0f}%")
        break