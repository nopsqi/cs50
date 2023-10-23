import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if sys.argv[1].split(".")[-1] != "py":
        sys.exit("Not a Python file")

    try:
        file = open(sys.argv[1])
    except: 


if __name__ == "__main__":
    main()