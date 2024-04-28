import pygame
from constants import _P1PIECE, _P2PIECE, _P1KING, _P2KING, _BOARD_COLOR, _PIECE_COLOR, _SQUARE_SIZE

# Each piece in the checkers board
class Piece:    
    def __init__(self, row, col, pieceNum):
        self.x = 0
        self.y = 0
        self.radius = (_SQUARE_SIZE // 2)

        self.king = False
        if (pieceNum == _P1KING or pieceNum == _P2KING):
            self.king = True

        # determines which row and column the piece is located at
        self.row = row
        self.col = col
        self.pieceNum = pieceNum

        # calculates x and y position from row and column
        self.calculatePositon()

    def calculatePosition(self):
        self.x = self.col * _SQUARE_SIZE + _SQUARE_SIZE // 2
        self.y = self.row * _SQUARE_SIZE + _SQUARE_SIZE // 2
        
    def draw(self, window):
        pygame.draw.circle(window, _PIECE_COLOR[self.pieceNum], (self.x, self.y), self.radius)



# Game board class
class CheckerBoard:
    
    def __init__(self):
        
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

        #background color
        window.fill((255,255,255))

        #draw each square
        for row_index, row in enumerate (self.board):
            for col_index, col in enumerate(row):
                #divide window into 8 equal spaces 
                x = col_index * _SQUARE_SIZE
                y = row_index * _SQUARE_SIZE
                if (row_index + col_index) % 2 == 0:
                    color = _BOARD_COLOR[0]
                else:
                    color = _BOARD_COLOR[1]
        
                #draw each square in the checkersboard
                pygame.draw.rect(window, color, (x,y, _SQUARE_SIZE, _SQUARE_SIZE))
    

    def drawPiece(self, window, pieces:list[Piece]) -> None:
        for piece in piece:
            piece.draw(window)

    # for printing out the board on the console
    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.board)


