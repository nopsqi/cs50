coin = 50
print(f"Amount Due: {coin}")
while True:
    amount = int(input("Insert Coin: "))
    coin -= amount
    if amount >= coin:
        print(f"Change Owed: {max(0, coin)}")
        break
    print(f"Amount Due: {coin}")