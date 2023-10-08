# TODO

def main():
    height = get_int("Height: ")
    print(height)


def get_int(prompt):
    height = 0
    while True:
        if (height := int(input("Height: "))) in range(1, 9):
            return height



if __name__ == "__main__":
    main()