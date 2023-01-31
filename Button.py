import pygame
from Rect import Rect


class Button(Rect):
    def __init__(self, rect, color, settings):
        super().__init__(rect, color, settings)
        self.text = ""
        self.text_color = color
        self.settings = settings
        self.text_surface = settings.base_font.render(self.text, True, self.text_color)

    # Methods -----------------------------------------------------------------

    def draw(self, screen, settings):
        pygame.draw.rect(
            screen,
            self.get_color(),
            self.get_rect(),
            border_radius=10,
        )
        screen.blit(self.get_text_surface(), (self.rect.x + 5, self.rect.y + 5))

    def click(self, settings):
        pass

    # Getters ------------------------------------------------------------------

    def get_text(self):
        return self.text

    def get_text_surface(self):
        return self.text_surface


