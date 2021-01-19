import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, hp=100):

        self.hp = hp


class Player(Entity):
    def __init__(self):
        pass


class Enemy(Entity):
    def __init__(self):
        pass

