def main():
    print("$", value(input("Greeting: ").strip()), sep="")


def value(greeting):
    if greeting.startswith("Hello"):
        return 0
    if greeting.startswith("H"):
        return 20
    return 100


if __name__ == "__main__":
    main()