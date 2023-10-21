
while True:
    try:
        x, y = input("Fraction: ").split("/")
        z = int(x) / int(y)
    except Exception:
        pass
    else:
        if z < 2:
            print("E")
        elif z > 0.99:
            print("F")
        else:
            print(f"{(z * 100):.0f}%")
        break