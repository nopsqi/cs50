coin = 50
print(f"Amount Due: {coin}")
while True:
    amount = int(input("Insert Coin: "))
    if amount >= coin:
        print(f"Change Owed: {coin}")
        break
    coin -= amount
    print(f"Amount Due: {coin}")