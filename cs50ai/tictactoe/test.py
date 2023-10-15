from tictactoe import *
import string
from itertools import product

def main():
    empty = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    # board = [[X, O, X],
    #          [O, EMPTY, O],
    #          [X, EMPTY, EMPTY]]
    board = [[X, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    # board = [[X,O,EMPTY],
    #          [X,X,O],
    #          [X,EMPTY,O]]
    # board = [[O,X,EMPTY],
    #          [O,O,X],
    #          [O,EMPTY,X]]
    # board = [[X,O,EMPTY],
    #          [O,O,X],
    #          [X,EMPTY,EMPTY]]
    # board = [[X, O, X],
    #          [X, O, EMPTY],
    #          [EMPTY, EMPTY, EMPTY]]
    # board = [[O, X, X],
    #          [X, X, O],
    #          [O, X, O]]
    # ab_pruning(board)
    letters = generate_combiations()
    print(next(letters))


def generate_combinations():
    letters = string.ascii_uppercase  # 'A' to 'Z'

    for r in range(1, 4):  # Generate up to 3-letter combinations (adjust as needed)
        for combination in product(letters, repeat=r):
            yield ''.join(combination)

# Example usage:
for combination in generate_combinations():
    print(combination)


if __name__ == "__main__":
    main()