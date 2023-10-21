amount = 50
while True:
    print(f"Amount Due: {amount}")
    coin = int(input("Insert Coin: "))
    if coin not in [5, 10, 25]:
        continue
    amount -= coin
    if amount < 1:
        print(f"Change Owed: {abs(amount)}")
        break