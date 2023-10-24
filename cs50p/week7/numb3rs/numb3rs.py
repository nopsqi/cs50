import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    return re.search(r"[0-2]", ip) is not None


if __name__ == "__main__":
    main()