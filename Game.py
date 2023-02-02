from Player import Player
from Grid import GridPosition, Grid


# Game class is used to play the game. It will keep track of players, grid and the score.
class Game:
    def __init__(self, grid, connectN, targetScore):
        self._grid = grid
        self._connectN = connectN
        self._targetScore = targetScore
        # define players
        self._players = [Player("Player 1", GridPosition.YELLOW), Player("Player 2", GridPosition.RED)]
        self._score = {}
        for player in self._players:
            self._score[player.getName()] = 0

    def printGrid(self):
        def getVal(item):
            if item == GridPosition.YELLOW:
                return "Y"
            elif item == GridPosition.RED:
                return "R"
            else:
                return "0"

        grid = self._grid.getGrid()
        print("--------------")
        for i in grid:
            print("\t".join(map(getVal, i)))
        print("--------------")

    def playMove(self, player):
        self.printGrid()
        print(f"{player.getName()}'s Turn : ")
        colCnt = self._grid.getColumnCount()
        insertColumn = int(input(f"Enter column b/w 0 and {colCnt - 1} to insert the piece\t"))
        insertRow = self._grid.placePiece(insertColumn, player.getPieceColor())

        return insertRow, insertColumn

    def playRound(self):
        while True:
            for player in self._players:
                row, col = self.playMove(player)
                # check if player wom by adding a piece
                pieceColor = player.getPieceColor()

                if self._grid.checkNConnected(self._connectN, row, col, pieceColor):
                    self._score[player.getName()] += 1
                    return player

    def play(self):
        maxScore = 0
        winner = None
        while maxScore < self._targetScore:
            winner = self.playRound()
            print(f"{winner.getName()} won the round.")
            maxScore = max(self._score[winner.getName()], maxScore)

            # reset the grid
            self._grid.initGrid()

        for x, y in self._score.items():
            if y == maxScore:
                print(f"{x} is the winner of the Game")


# create a grid
grid = Grid(4, 4)
# create a game with that grid
game = Game(grid, 4, 2)
# start the game
game.play()
