from minesweeper import Minesweeper, MinesweeperAI
import itertools


def main():
    game = Minesweeper()
    game.mines = {(7, 4), (2, 1), (3, 7), (5, 7), (0, 6), (2, 3), (6, 3), (3, 5)}
    print(game.mines)
    position = None
    count = 0
    for p in itertools.product(range(8), repeat=2):
        if p in game.mines:
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