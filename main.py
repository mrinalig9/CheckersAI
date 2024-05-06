import pygame
from CheckerGame import CheckerBoard, Piece
from CheckerAI import CheckerAI
from constants import HEIGHT, WIDTH
from Transition import BoardTransition

if __name__ == "__main__":
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    gameActive = True
    clock = pygame.time.Clock()

    ai = CheckerAI()
    CB = CheckerBoard()
    # CB.initializeBoard()
    boardLayout = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [-1, 0, 0, 0, 1, 0, 0, 0],
        [0, -1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, -1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, -2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    CB.makeCustomBoard(boardLayout)

    print(CB)

    bt = BoardTransition()
    pieceToTest = CB.board[4][3]
    newBoards = bt.getAllBoards(CB)

    print(newBoards)

    # Treat as pointer to a piece
    selectedPiece:Piece = None

    while gameActive:
        time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameActive = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(f"Previous selected piece: ${selectedPiece}")
                selectedPiece = CB.selectPiece()

        # Monitoring Performance
        # clock.tick()
        # print(clock.get_fps())

        if (time < 1000) or len(newBoards) == 0:
            CB.drawBoard(window)
            CB.drawPieces(window)
        else:
            index = int((time / 4000) % len(newBoards))
            newBoards[index].drawBoard(window)
            newBoards[index].drawPieces(window)

        pygame.display.update()

    pygame.quit()

