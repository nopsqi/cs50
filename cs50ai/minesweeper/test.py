from minesweeper import Minesweeper, MinesweeperAI
import itertools


def main():
    game = Minesweeper()
    mines = game.mines
    position = None
    count = 0
    for p in itertools.product(range(8), repeat=2):
        if p in mines:
            continue
        position = p
        count = game.nearby_mines(position)
        break
    count = game.nearby_mines(position)
    game.print()
    print(count)
    # ai = MinesweeperAI()
    # ai.add_knowledge((3, 1), 3)


if __name__ == "__main__":
    main()