import itertools
import string
from minesweeper import Minesweeper, MinesweeperAI


def main():
    size = 3
    game = Minesweeper(height=size, width=size, mines=3)
    encoder = {letter: move for letter, move in zip(string.ascii_lowercase, itertools.product(range(size), repeat=2))}
    while True:
        game.print()
        position = encoder.get(input("Move: "))
        if position is None:
            continue
        count = game.nearby_mines(position)
        print(position, count)
        # ai = MinesweeperAI()
        # ai.add_knowledge((3, 1), 3)


if __name__ == "__main__":
    main()