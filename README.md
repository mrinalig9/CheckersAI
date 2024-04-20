# CheckersAI
An AI to play Checkers. Uses Q-Learning as its foundation. Minimax algorithm with alpha-beta pruning is used to evaluate each move on the checkers board.

## Game Description
Checkers is a two-person board game in which each player tries to get rid of all the other player’s playing pieces in order to win. There are 24 playing pieces in all, 12 for each player, and each player’s chess color pieces are different from their opponents. Usually one player’s pieces are black while the other player’s is white. The playing field is a square board with 64 squares that are an even number of dark and light colored; the same colors are not next to each other. 

## Game Rules
- At the start of the game black player goes first.
- Each player takes turn to make a move
- There are two types of moves, a regular move and a capture move:
  - On regular move a piece moves forward one square diagonally to an adjacent empty square.
  - On capture move a piece can jump over and capture an opponents piece if the square across is an empty square. The player can capture multiple times in one turn.
- If a piece can be captured then it must be captured, it is not an option. If multiple pieces can capture on the same turn then the player can chose which piece to capture with (this also applies to consecutive captures).
- If a piece reaches the back row of the opponent it promotes to a King.
- All the previous rules apply to the king but it can also move backwards diagonally.

## Win condition
- A player can win the game by capturing all of their opponents pieces.
- If any one player reaches a board state in which they have no legal moves on their turn, then the player with the most amount of pieces wins. If they have the same amount of pieces then its a draw.
