from crossword import *
from generate import *


def main():
    structure = "data/structure0.txt"
    words = "data/words0.txt"

    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    # print(crossword.neighbors(Variable(4, 1, 'across', 4)))
    # print(crossword.words)
    # creator.enforce_node_consistency()
    # creator.revise(Variable(0, 1, "across", 3), Variable(0, 1, "down", 5))
    # print(creator.ac3())


if __name__ == "__main__":
    main()