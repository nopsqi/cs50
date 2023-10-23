import csv
import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if sys.argv[1].split(".")[-1].lower() != "csv":
        sys.exit("Not a CSV file")

    try:
        file = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")

    with open(sys.argv[1]) as file:
        reader = csv.reader(sys.argv[1])
        header = next(reader)
        print(header)


if __name__ == "__main__":
    main()
