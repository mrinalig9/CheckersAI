import pygame
from CheckerGame import CheckerBoard, Piece
from CheckerAI import CheckerAI
from constants import HEIGHT, WIDTH

if __name__ == "__main__":
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    gameActive = True
    clock = pygame.time.Clock()

    ai = CheckerAI()
    CB = CheckerBoard()
    CB.initializeBoard()
    print(CB)
    CB2 = CheckerBoard()
    CB2.initializeBoard()
    
    boardDict = dict()
    boardDict[CB] = ai.evaluateBoard(CB)

    print(boardDict)
    print(CB.__hash__())
    print(CB2.__hash__())

    if (CB2 in boardDict):
        print("Checker board 1 is equal to Checkers board 2")
    else:
        print("Checker boards are not equal")

    # Treat as pointer to a piece
    selectedPiece:Piece = None

    while gameActive:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameActive = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(f"Previous selected piece: ${selectedPiece}")
                selectedPiece = CB.selectPiece()

        # Monitoring Performance
        # clock.tick()
        # print(clock.get_fps())

        CB.drawBoard(window)
        CB.drawPieces(window)
        pygame.display.update()

    pygame.quit()

