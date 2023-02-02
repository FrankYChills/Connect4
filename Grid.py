# We will use Enum to store a grid cell value.
import enum


class GridPosition(enum.Enum):
    EMPTY = 0
    YELLOW = 1
    RED = 2


# Grid maintains the state of the board and also check for a win condition


class Grid:
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self._grid = None
        self.initGrid()

    def initGrid(self):
        self._grid = [[GridPosition.EMPTY for _ in range(self._columns)] for _ in range(self._rows)]

    def getGrid(self):
        return self._grid

    def getColumnCount(self):
        return self._columns

    # places a piece on a column as deep as available
    def placePiece(self, column, piece):
        if column < 0 or column >= self._columns:
            raise ValueError("Invalid column")
        if piece == GridPosition.EMPTY:
            raise ValueError("Invalid Piece")
        for row in range(self._rows - 1, -1, -1):
            if self._grid[row][column] == GridPosition.EMPTY:
                self._grid[row][column] = piece
                return row
            if row == 0:
                for c in self._grid[0]:
                    if c == GridPosition.EMPTY:
                        print("returning columnfull")
                        return "ColumnFull"

                print("returning gridfull")
                return "GridFull"

    def checkNConnected(self, connectN, row, col, piece):
        count = 0

        # check horizontal
        # check horizontally(all columns in a single row) if continuous same peices sum to connectN
        for c in range(self._columns):
            if self._grid[row][c] == piece:
                count += 1
            else:
                # if theres any gap reset to 0
                count = 0
            if sum == connectN:
                return True

        # check vertical and reset count to 0
        count = 0
        # check vertically(all rows in a single col) if continuous same peices sum to connectN
        for r in range(self._rows):
            if self._grid[r][col] == piece:
                count += 1
            else:
                # if theres any gap reset to 0
                count = 0
            if count == connectN:
                return True

        # check diagonally
        count = 0
        # check diagonally (top right corner to bottom left in line of the placed peice
        for r in range(self._rows):
            c = row + col - r
            if c >= 0 and c < self._columns and self._grid[r][c] == piece:
                count += 1
            else:
                # if theres any gap reset to 0
                count = 0
            if count == connectN:
                return True

        # check anti-diagonally
        count = 0
        # check anti-diagonally (top left corner to the bottom right in line of the placed piece)
        for r in range(self._rows):
            c = col - row + r
            if c >= 0 and c < self._columns and self._grid[r][c] == piece:
                count += 1
            else:
                # if theres any gap reset
                count = 0
            if count == connectN:
                return True

        # if no condition matches return false
        return False
