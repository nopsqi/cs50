import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if not (link := re.match(r"^<iframe.*src=\".*you[^\"]+/([^\"/]+)\".*></iframe>$", s)):
        return link
    return f"https://youtu.be/{link.group(1)}"


if __name__ == "__main__":
    main()