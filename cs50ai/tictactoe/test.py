from tictactoe import *
from util import *


def main():
    empty = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    board = [[X, O, O],
             [X, X, O],
             [O, X, X]]
    print(winner(board))


if __name__ == "__main__":
    main()