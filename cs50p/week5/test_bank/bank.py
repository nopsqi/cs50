def main():
    print("$", value(input("Greeting: ").strip()), sep="")


def value(greeting):
    if greeting.lower().startswith("hello"):
        return 0
    if greeting.lower().startswith("h"):
        return 20
    return 100


if __name__ == "__main__":
    main()