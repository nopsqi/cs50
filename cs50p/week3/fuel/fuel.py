
while True:
    x, y = input("Fraction: ").split("/")
    if 
    try:
        z = float(x) / float(y)
    except Exception:
        pass
    else:
        if z == 1:
            print("F")
        elif z == 0:
            print("E")
        else:
            print(f"{(z * 100):.0f}%")
        break