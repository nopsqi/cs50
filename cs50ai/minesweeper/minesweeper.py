import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print_board(self, moves):
        letter = (l for l in 'abcdefghijklmnopqrstuvwxyz')
        l = 'a'
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                l = next(letter)
                if self.board[i][j]:
                    print("|X", end="")
                elif (i, j) in moves:
                    print(f"|{moves[(i, j)]}", end="")
                else:
                    print(f"|{l}", end="")
            print("|")
        print("--" * self.width + "-")

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count
        self.__mines = set()
        self.__safes = set()

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __sub__(self, other):
        return Sentence(self.cells - other.cells)

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def __repr__(self):
        return self.__str__()

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        return self.__mines

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        return self.__safes

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        if cell in self.cells:
            self.count -= 1
            self.__mines.add(cell)
            self.cells.discard(cell)

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        if cell in self.cells:
            self.__safes.add(cell)
            self.cells.discard(cell)

class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def nearby_cells(self, cell):
        cells = set()
        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    cells.add((i, j))
        return cells

    def cleanup(self):
        temp = self.knowledge.copy()
        self.knowledge = []
        [self.knowledge.append(item) for item in temp if item not in self.knowledge]

    def learn(self):
        self.cleanup()
        for a, b in itertools.combinations(self.knowledge, 2):
            if a.count == 0 and len(a.cells) != 0:
                safes = set()
                for cell in a.cells:
                    safes.add(cell)
                for cell in safes:
                    self.mark_safe(cell)
            if len(a.cells) == a.count and a.count != 0:
                mines = set()
                for cell in a.cells:
                    mines.add(cell)
                for cell in mines:
                    self.mark_mine(cell)

            temp = set()
            for cell in a.known_safes():
                temp.add(cell)
            for cell in temp:
                self.mark_safe(cell)

            for cell in a.known_mines():
                temp.add(cell)
            for cell in temp:
                self.mark_mine(cell)

            sentence = None
            if a.cells > b.cells:
                sentence = Sentence(a.cells - b.cells, a.count - b.count)
            if b.cells > a.cells:
                sentence = Sentence(b.cells - a.cells, b.count - a.count)
            if sentence is not None:
                self.knowledge.append(sentence)
                self.learn()
            continue

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        self.moves_made.add(cell)
        n_cells = self.nearby_cells(cell) - self.moves_made
        sentence = Sentence(n_cells, count)
        if sentence not in self.knowledge:
            self.knowledge.append(sentence)

        self.mark_safe(cell)
        self.learn()
        self.cleanup()
        for sentence in self.knowledge:
            print(sentence)
            print("mines: ", sentence.known_mines())
            print("safes: ", sentence.known_safes())

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        raise NotImplementedError

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        raise NotImplementedError
