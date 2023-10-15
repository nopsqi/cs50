import string
from itertools import product

class Node():
    def __init__(self, state, parent, utility, level, action):
        self.state = state
        self.parent = parent
        self.utility = utility
        self.level = level
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node


def letters_counter():
    letters = string.ascii_uppercase  # 'A' to 'Z'

    for r in range(2, 4):  # Generate up to 3-letter combinations (adjust as needed)
        for combination in product(letters, repeat=r):
            yield ''.join(combination)


def print_node(node):
    address_counter = letters_counter()
    addresses = {}
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