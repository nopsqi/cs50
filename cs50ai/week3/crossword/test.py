from crossword import *
from generate import *


def main():
    structure = "data/structure0.txt"
    words = "data/words0.txt"

    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    # for row in crossword.structure:
    #     print(row)
    # for key, value in crossword.overlaps.items():
    #     print(key, value)
    for var in crossword.variables:
        print(var.cells)
    print(crossword.neighbors(Variable(4, 1, 'across', 4)))
    print(crossword.words)


if __name__ == "__main__":
    main()