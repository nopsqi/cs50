# TODO
def main():
    card_number = get_string("Number: ")
    print(card_number)

def get_string(prompt):
    card_number = input(prompt)
    while True:
        try:
            int(card_number)
            return card_number
        except ValueError:
            print("invalid")



if __name__ == "__main__":
    main()