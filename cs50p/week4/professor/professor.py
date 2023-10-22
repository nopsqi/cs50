import random


def main():
    actual = []
    answers = []
    level = get_level()
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        try:
            answers.append(int(input(f"{x} + {y}")))
        except ValueError:
            print("EEE")
            continue
        


def get_level():
    ...


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()