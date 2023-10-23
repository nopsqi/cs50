import sys
import csv


def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    try:
        source = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit(f"Cound not read {sys.argv[1]}")

    destination = open(sys.argv[2], "a")

    reader = csv.DictReader(source)
    writer = csv.DictWriter(destination, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for row in reader:
        last, first = row["name"].split(",")
        writer.writerow({"first": first, "last": last, "house": row["house"]})


    source.close()
    destination.close()


if __name__ == "__main__":
    main()