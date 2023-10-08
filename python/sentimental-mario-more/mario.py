# TODO

def main():
    height = get_int("Height: ")
    print(height)


def get_int(prompt):
    height = 0
    while True:
        height = input("Height: ")
        try:
            height = int(height)
            if height in range(1, 9):
                break
        except ValueError:
            print(f"{height} is not number")



if __name__ == "__main__":
    main()