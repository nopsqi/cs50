"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None
BOARD_DICTIONARY = {}


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    sum_x = sum(sum(1 for r in row if r == X) for row in board)
    sum_o = sum(sum(1 for r in row if r == O) for row in board)
    if sum_x > sum_o:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return set((i, j) for i, row in enumerate(board) for j, cell in enumerate(row) if cell is None)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] is not None:
        raise Exception("Ilegal move.")
    r = deepcopy(board)
    p = player(board)
    r[action[0]][action[1]] = p

    return r


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    r = [[1 if cell == X else -1 if cell == O else 0 for cell in row] for row in board]
    states = {}
    states["row"] = [0] * 3
    states["column"] = [0] * 3
    states["diagonal"] = [0] * 2
    i_prev = -1
    j_prev = 3
    for i, row in enumerate(r):
        for j, cell in enumerate(row):
            states["row"][i] += cell
            states["column"][j] += cell
            if i == j:
                states["diagonal"][0] += cell
            if i == i_prev + 1 and j == j_prev - 1:
                states["diagonal"][1] += cell
                j_prev = j
                i_prev = i
    states = sum(states.values(), [])
    if 3 in states:
        return X
    if -3 in states:
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    filled = all(all(row) for row in board)
    if filled:
        return filled
    if winner(board):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)

    if w == X:
        return 1
    if w == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    pl = player(board)
    res = []
    for ac in actions(board):
        if ac is not None:
            # res.append((ac, calculate(result(board, ac))))
            res.append((ac, prune(result(board, ac), -math.inf, math.inf)))

    i = [r[1] for r in res]
    if pl == X:
        i = i.index(max(i))
    else:
        i = i.index(min(i))

    return res[i][0]


def calculate(board):
    if terminal(board):
        return utility(board)

    values = []
    for b in [result(board, a) for a in actions(board)]:
        if not BOARD_DICTIONARY.get(to_tuple(b)):
            BOARD_DICTIONARY[to_tuple(b)] = calculate(b)
        values.append(BOARD_DICTIONARY[to_tuple(b)])

    pl = player(board)
    if pl == X:
        return max(values)
    return min(values)


def prune(board, alpha, beta):
    if terminal(board):
        return utility(board)

    pl = player(board)

    if pl == X:
        eval_util = -math.inf
    else:
        eval_util = math.inf

    for b in :
        util = prune(b, alpha, beta)
        if pl == X:
            eval_util = max(eval_util, util)
            alpha = max(alpha, util)
        else:
            eval_util = min(eval_util, util)
            beta = min(beta, util)
        if beta <= alpha:
            break
    return eval_util


def to_tuple(board):
    return tuple(tuple(cell for cell in row) for row in board)