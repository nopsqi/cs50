from tictactoe import *
import math

def main():
    empty = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]
    # board = [[X, O, X],
    #          [O, EMPTY, O],
    #          [X, EMPTY, EMPTY]]
    # board = [[X, EMPTY, EMPTY],
    #          [EMPTY, EMPTY, EMPTY],
    #          [EMPTY, EMPTY, EMPTY]]
    # board = [[X,O,EMPTY],
    #          [X,X,O],
    #          [X,EMPTY,O]]
    # board = [[O,X,EMPTY],
    #          [O,O,X],
    #          [O,EMPTY,X]]
    # board = [[X,O,EMPTY],
    #          [O,O,X],
    #          [X,EMPTY,EMPTY]]
    board = [[X, O, X],
             [X, O, EMPTY],
             [O, X, EMPTY]]
    # board = [[O, X, X],
    #          [X, X, O],
    #          [O, X, O]]
    print(calculate(board))


if __name__ == "__main__":
    main()