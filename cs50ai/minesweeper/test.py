from minesweeper import Minesweeper, MinesweeperAI
import itertools


def main():
    game = Minesweeper()
    mines = game.mines
    position = None
    for p in itertools.product(range(8), repeat=2):
        if p not in mines:
            position = p
            break
    ai = MinesweeperAI()
    ai.add_knowledge((3, 1), 3)


if __name__ == "__main__":
    main()