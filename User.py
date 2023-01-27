import pygame


class User(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.points = 10

        def update_points():
            self.points -= 1
