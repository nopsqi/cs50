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
    except FileNotFoundError:
        sys.exit("File does not exist")

    count = 0
    for line in file:
        line = line.strip()
        if line[0] != '#' and line != '\n':
            count += 1
    print(count)


if __name__ == "__main__":
    main()