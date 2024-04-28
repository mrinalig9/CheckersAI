import pygame
from CheckerGame import CheckerBoard
from constants import HEIGHT, WIDTH

if __name__ == "__main__":
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    gameActive = True
    clock = pygame.time.Clock()

    CB = CheckerBoard()
    print(CB)

    while gameActive:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameActive = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        CB.drawBaord(window)
        pygame.display.update()

    pygame.quit()

