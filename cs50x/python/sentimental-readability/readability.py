# TODO
import sys
import re
import math


def main():
    text = input("Input text: ")
    # text = "Congratulations! Today is your day. You're off to Great Places! You're off and away!"
    # text = 'Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversation?"'
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
    if len(sentences[-1]) < 2:
        sentences.pop()
    sentences = len(sentences)
    words = text.split(" ")
    words = len(words)
    letters = sum(1 for c in text if c.isalpha())

    l = letters / words * 100
    s = sentences / words * 100
    index = 0.0588 * l - 0.296 * s - 15.8
    return round(index)


if __name__ == "__main__":
    main()