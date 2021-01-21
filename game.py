import pygame
import test
import keys
from sprites import *


def check_obstacle(x1, y1, x2, y2):  # TODO сделать метод определения наличия препятствия между двумя точками (Glepp to Pasha)
    return False


class Game:
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    """Класс игры"""  # TODO Начать писать хоть какую-то документацию, пока не слишком стало поздно

    def __init__(self, screen):
        self.all_sprites = pygame.sprite.Group()
        self.all_objects = pygame.sprite.Group()
        self.all_without_player = pygame.sprite.Group()  # уверен, есть более красивый способ сделать всё это
        self.fps = 60
        self.running = True
        self.screen = screen
        self.background = BackGround(self.all_sprites)
        self.load_level()
        self.player = Player(self.all_sprites)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def load_level(self):
        self.background.setup('levels/test/back.png')
        self.all_sprites.draw(self.screen)

    def update(self):
        pass
