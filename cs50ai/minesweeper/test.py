from minesweeper import Minesweeper, MinesweeperAI
import itertools


def main():
    game = Minesweeper(height=3, width=3, mines=3)
    game.mines = {(0, 0), (1, 1), (2, 2)}
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