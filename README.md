## Working
1. The Game will be played by two players (PvP).
2. The Game Board should be of variable dimensions.
3. The target is top connect N discs in a row(Vertically,horizontally or diagonally)
   - N is a variable (e.g - connect4, connect5 etc)
4. There should be a score tracking system.
   1. After a player reaches the target score he wins the game.

## Design
1. We will need Grid class that maintains the state of the 2D Grid/Board
   1. The board cell can be empty, yellow(occ by p1) or red (occ by p2)
   2. The Grid will also be responsible for checking the win condition.

2. We Can have a Player class that represents the player peice color.
   1. Encapsulating information is a good practice.

3. The Game class will be composed of Grid and Players
   1. The Game class will be responsible for the game loop and keeping track of the score.

    