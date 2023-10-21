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
            first = l
            break
    if first == "0":
        return False
    if first is not None and not s[s.index(first):].isdigit():
        return False

    return True


main()