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
        except ValueError:
            print(f"{height} is not number")
        else:
            print(f"height is {height}")



if __name__ == "__main__":
    main()