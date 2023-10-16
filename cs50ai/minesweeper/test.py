from minesweeper import Minesweeper, MinesweeperAI
import itertools


def main():
    game = Minesweeper()
    print(list(itertools.product(range(8), 2)))
    ai = MinesweeperAI()
    ai.add_knowledge((3, 1), 3)


if __name__ == "__main__":
    main()