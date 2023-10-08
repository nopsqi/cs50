# TODO
import sys


def main():
    card_number = get_string("Number: ")
    # card_number = str(4003600000000014)
    if (not check_card(card_number)):
        print("INVALID")
        sys.exit(1)
    print(check_provider(card_number))
    sys.exit(0)


def check_provider(card_number):
    card_length = len(card_number)
    if card_length == 16 and int(card_number[:2]) in range(51,56):
        return "MASTERCARD"
    if card_length == 15 and int(card_number[:2]) in [34, 37]:
        return "AMEX"
    if card_length in [13, 16] and int(card_number[0]) == 4:
        return "VISA"
    return "INVALID"


def check_card(card_number):
    luhn = 0;
    for i, n in enumerate(card_number[::-1]):
        n = int(n)
        if i % 2 == 1:
            luhn += sum(int(sub_n) for sub_n in str(n * 2))
        else:
            luhn += n
    return luhn % 10 == 0


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