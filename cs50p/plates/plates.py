def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s.isalnum():
        return False
    if not s[:2].isalpha():
        return False
    if not (1 < len(s) < 7):
        return False
    first = None
    for l in s:
        if l.isdigit():
            first = int(l)
            break
    if first == 0:
        return False
    if first is not None:
        for l in s[s.index(first):]:
            if l.isalpha():
                return False

    return True


main()