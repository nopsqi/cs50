amount = 50
while True:
    if amount < 1:
        print("Change Owed: 0")
        break
    print(f"Amount Due: {amount}")
    amount -= int(input("Insert Coin: "))