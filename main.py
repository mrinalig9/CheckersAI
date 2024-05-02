import pygame
from CheckerGame import CheckerBoard, Piece
from constants import HEIGHT, WIDTH

if __name__ == "__main__":
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    gameActive = True
    clock = pygame.time.Clock()

    CB = CheckerBoard()
    CB.initializeBoard()
    print(CB)

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

