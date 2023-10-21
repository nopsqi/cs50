def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[:2].isalpha():
        return False
    if not (1 < len(s) < 7):
        return False
    if s[-1].isalpha():
        for l in s[:-1]:
            if l.isdigit():
                return False
    if not s.isalnum():
        return False


main()