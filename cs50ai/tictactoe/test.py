from tictactoe import *
from util import *


def main():
    # board = [[EMPTY, EMPTY, EMPTY],
    #          [EMPTY, EMPTY, EMPTY],
    #          [EMPTY, EMPTY, EMPTY]]
    board = [[EMPTY, X, EMPTY],
             [EMPTY, EMPTY, O],
             [EMPTY, EMPTY, EMPTY]]
    print(actions(board))


if __name__ == "__main__":
    main()