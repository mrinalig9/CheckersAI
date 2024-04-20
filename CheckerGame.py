#import pygame

# Game board class
class CheckerBoard:
    def __init__(self):
        _BPIECE = 1
        _WPIECE = 2
        _BKING = 3
        _WKING = 4
        # 2D Board Matrix
        # 0 = empty square
        # 1 = Black piece
        # 2 = White piece
        # 3 = Black king
        # 4 = White king
        self.board = [
            [0, _BPIECE, 0, _BPIECE, 0, _BPIECE, 0, _BPIECE],
            [_BPIECE, 0, _BPIECE, 0, _BPIECE, 0, _BPIECE, 0],
            [0, _BPIECE, 0, _BPIECE, 0, _BPIECE, 0, _BPIECE],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [_WPIECE, 0, _WPIECE, 0, _WPIECE, 0, _WPIECE, 0],
            [0, _WPIECE, 0, _WPIECE, 0, _WPIECE, 0, _WPIECE],
            [_WPIECE, 0, _WPIECE, 0, _WPIECE, 0, _WPIECE, 0]
            ]
        # indicated player's turn (black starts)
        self.turn = _BPIECE

    # draws the board with pieces onto the screen using pygame
    def drawBaord(self) -> None:
        # GUI team works on this
        pass

    # for printing out the board on the console
    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.board)
