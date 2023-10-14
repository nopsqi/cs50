from tictactoe import *
from util import *


def main():
    empty = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    board = [[EMPTY, X, EMPTY],
             [EMPTY, X, O],
             [EMPTY, EMPTY, EMPTY]]
    print(winner(board))


if __name__ == "__main__":
    main()