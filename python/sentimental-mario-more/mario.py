# TODO

def main():
    height = get_int("Height: ")
    print(height)


def get_int(prompt):
    height = 0
    while True:
        try:
            height = int(input("Height: "))
        except ValueError:
            print(f"{height} is not number")



if __name__ == "__main__":
    main()