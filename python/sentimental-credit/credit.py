# TODO
def main():
    card_number = get_string("Number: ")
    print(card_number)

def check_card(card_number):
    
    for i, n in enumerate(card_number):
        if

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