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
            if tried > 2:
                print(f"{x} + {y} = {actuals[i]}")
                break
            answer = input(f"{x} + {y} = ")
            try:
                answers[i] = int(answer)
            except IndexError:
                answers.append(int(answer))
            except ValueError:
                print("EEE")
                tried += 1
                continue
            if answers[i] != actuals[i]:
                print("EEE")
                tried +=1
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
    start = 10 ** level
    end = start * 9
    start = 0 if start == 1 else start
    return random.randint(start, end)


if __name__ == "__main__":
    main()