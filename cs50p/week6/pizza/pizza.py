import csv
import sys
from tabulate import tabulate


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
        reader = csv.reader(file)
        header = next(reader)
        print(tabulate(reader, headers=header, tablefmt="grid"))


if __name__ == "__main__":
    main()
