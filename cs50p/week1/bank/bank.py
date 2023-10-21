greet = input("Greeting: ")

if greet.startswith("Hello"):
    print("$0")
elif greet.startswith("H"):
    print("$20")
else:
    print("$100")