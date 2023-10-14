from tictactoe import *
from util import *


def main():
    empty = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    board = [[X, O, X],
             [X, X, O],
             [O, X, O]]
    print(utility(board))


if __name__ == "__main__":
    main()