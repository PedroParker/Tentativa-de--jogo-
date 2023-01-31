import pygame


class Rect:
    def __init__(self, rect, color, settings):
        self.rect = pygame.Rect(rect)
        self.color = color
        self.settings = settings
        self.active = False

    # Methods -----------------------------------------------------------------

    def draw(self, screen, settings):
        pygame.draw.rect(
            screen,
            self.get_color(),
            self.get_rect(),
        )

    def draw_when_active(self, screen, settings):
        if self.get_active():
            self.draw(screen, settings)

    # Setters -----------------------------------------------------------------

    def set_active(self, settings):
        if not self.get_active():
            self.active = True

    def set_unactive(self):
        if self.get_active():
            self.active = False

    def set_x_pos(self, x):
        self.rect.x = x

    # Getters -----------------------------------------------------------------

    def get_rect(self):
        return self.rect

    def get_color(self):
        return self.color

    def get_active(self):
        return self.active
