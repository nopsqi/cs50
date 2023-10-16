from minesweeper import Minesweeper, MinesweeperAI


def main():
    game = Minesweeper()
    print(game.mines)
    ai = MinesweeperAI()
    ai.add_knowledge((3, 1), 3)


if __name__ == "__main__":
    main()