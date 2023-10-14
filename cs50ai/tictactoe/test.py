from tictactoe import *
from util import *


def main():
    empty = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    board = [[X, O, X],
             [X, X, O],
             [O, EMPTY, EMPTY]]
    print(minimax(board))


if __name__ == "__main__":
    main()