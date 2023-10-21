amount = 50
while True:
    print(f"Amount Due: {amount}")
    coin = int(input("Insert Coin: "))
    if coin not in [5, 10, 25]:
        continue
    amount -= coin
    if amount == 0:
        print(f"Change Owed: {amount}")
        break
    if amount < 0:
        print(f"Change Owed: {amount + coin}")
        break