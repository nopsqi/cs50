# TODO
import sys
import re


def main():
    # text = input("Input text: ")
    text = "Congratulations! Today is your day. You're off to Great Places! You're off and away!"
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
    sentences = re.split(r'[.!?]', text)
    sentences.pop()
    print(sentences)
    return 3


if __name__ == "__main__":
    main()