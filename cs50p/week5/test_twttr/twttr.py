def main():
    text = input("Input: ")
    print("Output:", end=" ")


def shorten(word):
    for w in word:
        if w.lower() in ['a', 'i', 'u', 'e', 'o']:
            continue
        print(w, end="")
    print()


if __name__ == "__main__":
    main()