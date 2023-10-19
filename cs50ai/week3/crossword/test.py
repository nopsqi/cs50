from crossword import *
from generate import *


def main():
    structure = "data/structure0.txt"
    words = "data/words0.txt"

    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    print(crossword)


if __name__ == "__main__":
    main()