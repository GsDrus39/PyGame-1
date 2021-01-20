import pygame
from os import path


def load_image(name):
    if not path.isfile(name):
        print(f"Файл с изображением '{name}' не найден")
        raise ValueError(f'Нет файла по пути {name}')
    image = pygame.image.load(name)
    image.convert_alpha()
    return image


class Entity(pygame.sprite.Sprite):
    def __init__(self, *group, image='entities/error.png', hp=100, speed=10):
        super().__init__(*group)
        self.hp = hp
        self.speed = speed
        self.image = load_image(image)
        self.rect = self.image.get_rect()


class Player(Entity):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image('entities/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 250

    def update(self, *keys):
        x, y = pygame.mouse.get_pos()




class Enemy(Entity):
    pass


class BackGround(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.group = group

    def setup(self, img):
        self.image = load_image(img)
        self.rect = self.image.get_rect()

