import pygame


class Game:
    def __init__(self):
        self.fps = 60
        self.time = 1
        self.running = True
        pygame.init()
        self.size = width, height = 500, 500
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.flip()
        while self.running:
            pass

    def load_level(self):
        import levels.test



    def pause(self):
        pass

    def unpause(self):
        pass