amount = 50
while True:
    if amount < 1:
        print("Amount Due: 0")
        break
    print(f"Amount Due: {amount}")
    amount -= int(input("Insert Coin: "))