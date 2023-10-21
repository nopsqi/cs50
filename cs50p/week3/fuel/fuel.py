
while True:
    x, y = input("Fraction: ").split("/")
    try:
        z = float(x) / float(y)
    except Exception:
        pass
    else:
        if z == 1:
            print("F")
        else:
            print(f"{(z * 100):.0f}%")
        break