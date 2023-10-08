# TODO
import sys
import re
import math


def main():
    text = input("Input text: ")
    # text = "Congratulations! Today is your day. You're off to Great Places! You're off and away!"
    print(check_text(text))
    sys.exit(0)


def check_text(text):
    grade = coleman(text)
    if grade > 16:
        return "Grade 16+"
    if grade < 1:
        return "Before Grade 1"
    return f"Grade {grade}"


def coleman(text):
    sentences = re.split(r"[.!?]", text)
    sentences = sum(1 for s in sentences if s != "")
    # sentences = sum(1 for _ in sentences)
    words = text.split(" ")
    words = sum(1 for w in words if w != "")
    # words = sum(1 for _ in words)
    letters = sum(1 for c in text if c.isalpha())

    l = letters / words * 100
    s = sentences / words * 100
    index = 0.0588 * l - 0.296 * s - 15.8
    return round(index)


if __name__ == "__main__":
    main()