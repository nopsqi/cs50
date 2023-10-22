import random


def main():
    actuals = []
    answers = []
    level = get_level()
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        actuals.append(x + y)
        tried = 0
        while True:
            try:
                answers.append(int(input(f"{x} + {y} = ")))
            except ValueError:
                if tried > 2:
                    break
                print("EEE")
                tried += 1
                continue
            break
    print(f"Score: {sum(actual == answer for actual, answer in zip(actuals, answers))}")


def get_level():
    while True:
        level = input("Level: ")
        try:
            level = int(level)
        except ValueError:
            continue
        if 0 < level < 4:
            return level


def generate_integer(level):
    level = level - 1
    return random.randint(10 ** level, (10 ** level) * 9)


if __name__ == "__main__":
    main()