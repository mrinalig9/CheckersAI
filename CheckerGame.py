#import pygame

# Game board class
class CheckerBoard:
    def __init__(self):
        _P1PIECE = 1
        _P2PIECE = 2
        _P1KING = 3
        _P2KING = 4
        # 2D Board Matrix
        # 0 = empty square
        # 1 = Player 1's piece
        # 2 = Player 2's piece
        # 3 = Player 1's king
        # 4 = Player 2's king
        self.board = [
            [0, _P1PIECE, 0, _P1PIECE, 0, _P1PIECE, 0, _P1PIECE],
            [_P1PIECE, 0, _P1PIECE, 0, _P1PIECE, 0, _P1PIECE, 0],
            [0, _P1PIECE, 0, _P1PIECE, 0, _P1PIECE, 0, _P1PIECE],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [_P2PIECE, 0, _P2PIECE, 0, _P2PIECE, 0, _P2PIECE, 0],
            [0, _P2PIECE, 0, _P2PIECE, 0, _P2PIECE, 0, _P2PIECE],
            [_P2PIECE, 0, _P2PIECE, 0, _P2PIECE, 0, _P2PIECE, 0]
            ]
        # indicated player's turn
        self.turn = _P1PIECE

        self.player1NumPieces = self.player2NumPieces = 12
        self.player1NumKings = self.player2NumKings = 0

    # draws the board with pieces onto the window using pygame
    def drawBaord(self, window) -> None:
        # GUI team works on this
        pass

    # for printing out the board on the console
    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.board)
