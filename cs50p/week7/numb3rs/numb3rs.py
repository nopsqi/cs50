import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    return re.search(r"", ip) is not None


if __name__ == "__main__":
    main()