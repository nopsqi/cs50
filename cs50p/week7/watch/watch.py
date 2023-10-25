import re
import sys


def main():
    print(parse(input("HTML: ")))
    # parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>')
    # parse('<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
    # parse('<iframe src="https://www.cs50.com/embed/xvFZjo5PgG0"></iframe>')


def parse(s):
    if not (link := re.match(r"^<iframe.*src=\".*you[^\"]+/([^\"/]+)\".*></iframe>$", s)):
        return link
    return f"https;//youtu.be/{link.group(1)}"


if __name__ == "__main__":
    main()