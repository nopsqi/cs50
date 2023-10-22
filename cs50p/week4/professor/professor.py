import random


def main():
    actuals = []
    answers = []
    level = get_level()
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        actuals.append(x + y)
        while True:
            try:
                answers.append(int(input(f"{x} + {y}")))
            except ValueError:
                print("EEE")
                continue
            break


def get_level():
    while True:
        try:
            return int(input("Level: "))
        except ValueError:
            pass


def generate_integer(level):
    return random.randint(level ** 10, (level ** 10) * 9)


if __name__ == "__main__":
    main()