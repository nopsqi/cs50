
while True:
    x, _, y = input("Fraction: ").split("/")
    try:
        print(x / y)
    except Exception: