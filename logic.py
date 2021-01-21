"""Поведение ботов и стрельба (наверное)"""
from game import check_obstacle


class AI:
    def __init__(self, enemy, hero):
        self.enemy = enemy
        self.hero = hero

    def attack(self):
        res = check_obstacle(self.enemy.x, self.enemy.y, self.hero.x, self.hero.y)
        if not res:
            self.go_to_hero()
        print('piu-piu')  # TODO сделать поиск укрытия и наведение на ГГ

    def go_to_hero(self):
        pass  # TODO сделать движение в комнату героя
