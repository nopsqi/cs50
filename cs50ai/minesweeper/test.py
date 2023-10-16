import itertools
import string
import os
from minesweeper import Minesweeper, MinesweeperAI


def main():
    size = 3
    game = Minesweeper(height=size, width=size, mines=3)
    ai = MinesweeperAI()
    encoder = {letter: move for letter, move in zip(string.ascii_lowercase, itertools.product(range(size), repeat=2))}
    positions = []
    game.print()
    while True:
        position = encoder.get(input("Move: "))
        if position is None:
            continue
        positions.append(position)
        count = game.nearby_mines(position)
        game.print_board(positions, count)
        print(position, count)
        ai.add_knowledge(position, count)


if __name__ == "__main__":
    main()