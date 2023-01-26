import pygame


class Interface(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.image = pygame.image.load("ImageDirectory.png")
        self.rect = pygame.Rect(200, 200, 140, 32)
