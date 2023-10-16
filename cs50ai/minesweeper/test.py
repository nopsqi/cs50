from minesweeper import MinesweeperAI


def main():
    ai = MinesweeperAI()
    ai.add_knowledge((3, 1), 3)


if __name__ == "__main__":
    main()