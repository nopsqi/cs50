# TODO
import sys


def main():
    # card_number = get_string("Number: ")
    card_number = str(4062901840)
    if (check_card(card_number) == 0):
        print("INVALID")
        sys.exit(1)
    print("VALID")


def check_card(card_number):
    luhn = 0;
    for i, n in enumerate(card_number[::-1]):
        n = int(n)
        if i % 2 == 1:
            luhn += n * 2
        else:
            luhn += n
    return luhn


def get_string(prompt):
    while True:
        card_number = input(prompt)
        try:
            int(card_number)
            return card_number
        except ValueError:
            continue


if __name__ == "__main__":
    main()