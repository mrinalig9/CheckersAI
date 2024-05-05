from collections.abc import Iterable
import pygame
from constants import _P1PIECE, _P2PIECE, _P1KING, _P2KING, _BOARD_COLOR, _PIECE_COLOR, _SQUARE_SIZE
from constants import _PIECE_RADIUS, _ROWS, _COLS,_PIECE_PADDING

# Each piece in the checkers board
class Piece:    
    def __init__(self, row, col, pieceNum):
        self.x = 0
        self.y = 0

        self.king = False
        if (pieceNum == _P1KING or pieceNum == _P2KING):
            self.king = True

        # determines which row and column the piece is located at
        self.row = row
        self.col = col
        self.pieceNum = pieceNum

        # calculates x and y position from row and column
        self.calculatePosition()

    def calculatePosition(self):
        self.x = (self.col * _SQUARE_SIZE) + (_SQUARE_SIZE // 2)
        self.y = (self.row * _SQUARE_SIZE) + (_SQUARE_SIZE // 2)
        
    def draw(self, window):
        pygame.draw.circle(window, _PIECE_COLOR[self.pieceNum], (self.x, self.y), _PIECE_RADIUS - _PIECE_PADDING)

    def __str__(self) -> str:
        return str(self.pieceNum)


# Game board class
class CheckerBoard:
    
    def __init__(self):
        
        # 2D Board Matrix
        # 0 = empty square
        # -1 = Player 1's piece
        # 1  = Player 2's piece
        # -2 = Player 1's king
        # 2  = Player 2's king
        self.board = []
        # indicated player's turn
        self.turn = _P2PIECE

        self.player1NumPieces = self.player2NumPieces = 12
        self.player1NumKings = self.player2NumKings = 0

    # Sets up pieces for a new game
    def initializeBoard(self):
        for i in range(_ROWS):
            self.board.append([])
            for j in range(_COLS):
                if (((i+j) % 2) != 0):
                    if (i < 3):
                        self.board[i].append(Piece(i, j, _P1PIECE))
                    elif (i > 4):
                        self.board[i].append(Piece(i, j, _P2PIECE))
                    else:
                        self.board[i].append(0)
                else:
                    self.board[i].append(0)

    # draws the board with pieces onto the window using pygame
    def drawBoard(self, window) -> None:
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
    

    def drawPieces(self, window) -> None:
        for row in self.board:
            for piece in row:
                if (type(piece) is Piece):
                    piece.draw(window)

    def selectPiece(self) -> Piece:
        # get mouse position
        mousePosX, mousePosY = pygame.mouse.get_pos()
        #print(f"Mouse position x: ${mousePosX}, y: ${mousePosY}")
        # calculate board square location clicked on
        pieceRow = mousePosY // _SQUARE_SIZE
        pieceCol = mousePosX // _SQUARE_SIZE
        #print(f"Row: ${pieceRow} Col: ${pieceCol}")
        
        selectedSquare = self.board[pieceRow][pieceCol]
        if (type(selectedSquare) is Piece and (selectedSquare.pieceNum * self.turn) > 0):
            #print("selected player piece")
            return selectedSquare
        return None

    
    def placePiece(self, piece) -> None:
        #get mouse position
        mousePosX, mousePosY = pygame.mouse.get_pos()
        print(f"Mouse position x: ${mousePosX}, y: ${mousePosY}")
        # calculate board square location clicked on
        pieceRow = mousePosY // _SQUARE_SIZE
        pieceCol = mousePosX // _SQUARE_SIZE
        print(f"Row: ${pieceRow} Col: ${pieceCol}")
        
        #make sure its a valid move

         #ensure the checker piece moves diagonally
        if abs(pieceRow - piece.row) == 1 and abs(pieceCol - piece.col) == 1:
            print('valid move')
            print(piece.row)
            print(piece.col)
            piece.row = pieceRow
            piece.col = pieceCol
            piece.calculatePosition()
            self.board[pieceRow][pieceCol] ,self.board[piece.row][piece.col]= piece,self.board[pieceRow][pieceCol]
            print(piece.row)
            print(piece.col)
        
        #switch players turn
            if self.turn == _P2PIECE:
                self.turn = _P1PIECE
            else:
                self.turn = _P2PIECE

    # for printing out the board on the console
    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.board)


