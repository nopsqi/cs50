import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # return re.search(r"[0-2][0-5]{2}", ip) is not None
    return (
        re.search(
            r"(^2[0-4][0-9]\.|^1[0-9]{2}\.|^[1-9]?[0-9]\.)(2[0-5]{2}\.|1[0-9]{2}\.|[1-9]?[0-9]\.){2}(2[0-5]{2}$|1[0-9]{2}$|[1-9]?[0-9])$",
            ip,
        )
        is not None
    )


if __name__ == "__main__":
    main()
