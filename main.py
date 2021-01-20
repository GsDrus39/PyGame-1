import pygame
from game import Game

if __name__ == '__main__':
    pygame.init()
    SIZE = 800, 600
    SCREEN = pygame.display.set_mode(SIZE)
    pygame.display.flip()
    game = Game(SCREEN)
    pause = False
    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
