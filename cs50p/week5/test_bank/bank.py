def main():
    greeting = input("Greeting: ").strip()


def value(greeting):
    if greeting.startswith("Hello"):
        print("$0")
    elif greeting.startswith("H"):
        print("$20")
    else:
        print("$100")


if __name__ == "__main__":
    main()