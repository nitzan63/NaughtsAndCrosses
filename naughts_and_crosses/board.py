from naughts_and_crosses.cell import Cell


class Board:
    """
    Board class represents a game board, it holds the board state with 3X3 Cells array
    """
    def __init__(self):
        self._cells = [[Cell() for _ in range(3)] for _ in range(3)]

    def reset(self):
        for row in self._cells:
            for cell in row:
                cell.value = None

    def make_move(self, row, col, player):
        """
        checks if the clicked cell is empty - and places the players symbol.
        returns False if the cell is taken
        """
        if self._cells[row][col].is_empty():
            self._cells[row][col].value = player.symbol
            return True
        return False

    def get_cell_value(self, row, col):
        return self._cells[row][col].value

    @property
    def cells(self):
        return self._cells
