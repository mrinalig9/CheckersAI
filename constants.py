WIDTH = 800
HEIGHT = 800

_P1PIECE = -1
_P2PIECE = 1
_P1KING = -2
_P2KING = 2
_BOARD_COLOR = [(255, 0, 0), (0, 0, 0)]
_ROWS = _COLS = 8
# color of piece 1 2 3 4 in that order
#_PIECE_COLOR = [(255, 255, 255), (0, 255, 0), (255, 100, 255), (100, 255, 0)] 
_PIECE_COLOR = dict([(-1, (220, 220, 220)), (1, (220, 0, 50)), (-2, (255, 100, 255)), (2, (100, 255, 0))])

_SQUARE_SIZE = WIDTH // _COLS
_PIECE_RADIUS = _SQUARE_SIZE // 2
_PIECE_PADDING = 10