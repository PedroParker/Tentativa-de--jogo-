import random
import pygame


class Card(pygame.sprite.Sprite):
    def __init__(self, settings):
        super(Card, self).__init__()

        self.random_x = random.random()
        self.card_image = pygame.image.load(
            random.choice(["Resources/card.png", "Resources/card2.png"])
        )
        self.angle = random.random() * 360
        self.angle_speed = 2 * random.choice([-1, 1])
        self.card_rect = self.card_image.get_rect()
        self.card_rect.bottomleft = (self.random_x * settings.width, 0)
        self.linear_speed = 2

    def update(self, screen, settings):
        center = self.card_rect.center
        self.angle = (self.angle + self.angle_speed) % 360
        image = pygame.transform.rotate(self.card_image, self.angle)
        self.card_rect = image.get_rect()
        self.card_rect.center = (center[0], center[1] + self.linear_speed)

        if self.card_rect.topleft[1] >= settings.height:
            self.kill()
        screen.blit(image, self.card_rect)
