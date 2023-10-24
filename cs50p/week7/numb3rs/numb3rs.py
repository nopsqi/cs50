import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # return re.search(r"(([0=1][0-5]{2}|[0-9]{1,2})\.){2}[0=1][0-5]{2}|[0-9]{1,2}", ip) is not None
    return re.search(r"([0=1][0-5]{2}|[0-9]{1,2})", ip) is not None


if __name__ == "__main__":
    main()