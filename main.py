import pygame
from CheckerGame import CheckerBoard

WIDTH = 800
HEIGHT = 800

if __name__ == "__main__":
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    gameActive = True
    clock = pygame.time.Clock()

    CB = CheckerBoard()
    print(CB)

    while gameActive:
        CB.drawBaord(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameActive = False
            break

    pygame.quit()

