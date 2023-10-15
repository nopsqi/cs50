"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy
from util import Node, QueueFrontier, StackFrontier, letters_counter

X = "X"
O = "O"
EMPTY = None


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
    if not any(any(row) for row in board):
        return X
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
            res.append((ac, calculate(result(board, ac))))

    i = [r[1] for r in res]
    if pl == X:
        i = i.index(max(i))
    else:
        i = i.index(min(i))

    return res[i][0]


def ab_pruning(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    start = Node(state=board, parent=None, utility=None, level=0, action=None)
    frontier = StackFrontier()
    # frontier = QueueFrontier()
    frontier.add(start)
    num_explored = 0
    address_counter = letters_counter()
    addresses = {}

    while True:
        if frontier.empty():
            return None

        node = frontier.remove()
        num_explored += 1

        p = player(node.state)
        if p == X:
            value = -2
        else:
            value = 2

        padding = " " * node.level * 14
        if node.parent is not None:
            if addresses.get(id(node.parent)) is None:
                addresses[id(node.parent)] = next(address_counter)
            print(f"{padding}parent: {addresses.get(id(node.parent))}")
        if addresses.get(id(node)) is None:
            addresses[id(node)] = next(address_counter)
        print(f"{padding}node: {addresses.get(id(node))}")
        print(f"{padding}turn: {p}")
        print(f"{padding}action: {node.action}")
        if terminal(node.state):
            padding_t = (" " * (node.level - 1) * 14) + "t" + (" " * 13)
            print(f"{padding_t}winner: {winner(node.state)}")
        if node.level == 0 or terminal(node.state) or node.level == 2:
            print(f"{padding}utility: {calculate(node.state)}")
        for row in node.state:
            print(f"{padding}{row}")
        print()

        if terminal(node.state) or node.level > 0:
            continue

        for a, b in [(act, result(node.state, act)) for act in actions(node.state)]:
            child = Node(state=b, parent=node, utility=None, level=node.level+1, action=a)
            frontier.add(child)


def calculate(board):
    if terminal(board):
        return utility(board)

    values = [calculate(b) for b in [result(board, a) for a in actions(board)]]

    pl = player(board)
    if pl == X:
        return max(values)
    return min(values)


def to_tupe(board):
    return ((cell for cell in row) for row in board)