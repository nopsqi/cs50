# TODO

def main():
    height = get_int("Height: ")
    for h in range(height):
        brick = '#' * (h + 1)
        print(' ' * (height - (h + 1)) + brick + "  " + brick)


def get_int(prompt):
    height = 0
    while True:
        height = input("Height: ")
        try:
            height = int(height)
            if height in range(1, 9):
                return height
        except ValueError:
            print(f"{height} is not number")


if __name__ == "__main__":
    main()