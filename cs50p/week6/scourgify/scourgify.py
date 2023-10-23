import sys


def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    try:
        source = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit(f"Cound not read {sys.argv[1]}")

    destination = open(sys.argv[2], "w")
    

    source.close()
    destination.cose()


if __name__ == "__main__":
    main()