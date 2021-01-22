import pygame
from game import Game
import keys

UPDATE_SCREEN = pygame.USEREVENT + 1
if __name__ == '__main__':
    pygame.init()
    SIZE = 800, 600
    SCREEN = pygame.display.set_mode(SIZE)
    FPS = 16 # Миллисекунд между обновлениями
    pygame.display.flip()
    game = Game(SCREEN)
    pause = False
    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.type in keys.game_keys_list:
                    game.add_to_stack(event)
            elif event.type == UPDATE_SCREEN:
                pass
