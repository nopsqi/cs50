def main():
    text = input("Input: ")


def shorten(word):
    short = []
    for w in word:
        if w.lower() in ['a', 'i', 'u', 'e', 'o']:
            continue
        short.append(w)
    return "".join(short)

if __name__ == "__main__":
    main()