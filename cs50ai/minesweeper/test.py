import itertools
import string
from minesweeper import Minesweeper, MinesweeperAI


def main():
    size = 3
    game = Minesweeper(height=size, width=size, mines=3)
    ai = MinesweeperAI()
    encoder = {letter: move for letter, move in zip(string.ascii_lowercase, itertools.product(range(size), repeat=2))}
    status = None
    while True:
        game.print()
        if status is not None:
            print(status)
        position = encoder.get(input("Move: "))
        if position is None:
            status = None
            continue
        count = game.nearby_mines(position)
        status = f"{position} {count}"
        ai.add_knowledge(position, count)


if __name__ == "__main__":
    main()