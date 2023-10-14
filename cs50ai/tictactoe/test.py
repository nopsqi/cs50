from tictactoe import *
from util import *


def main():
    empty = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    board = [[X, O, X],
             [O, X, O],
             [X, EMPTY, EMPTY]]
    board = [[X, O, X],
             [X, X, O],
             [O, X, EMPTY]]
    print(terminal(board))


if __name__ == "__main__":
    main()