from Button import Button
import pygame


class VisualizeButton(Button):
    def __init__(self, rect, color, settings):
        super().__init__(rect, color, settings)
        self.text = ""

    # Methods -----------------------------------------------------------------

    def draw(self, screen, settings):
        pygame.draw.rect(
            screen,
            self.color,
            self.rect,
            border_radius=10,
            width=3
        )

        screen.blit(self.get_text_surface(), (self.rect.x + 5, self.rect.y + 5))

    # Setters -----------------------------------------------------------------

    def set_text(self, user):
        self.text = user.update_data()
        self.set_text_surface()
        self.set_width()

    def set_text_surface(self):
        self.text_surface = self.settings.base_font.render(
            self.text, True, self.settings.get_color("black")
        )

    def set_width(self):
        if self.get_text_surface().get_width() + 19 <= self.settings.button_width:
            self.rect.width = self.settings.button_width

        elif self.get_text_surface().get_width() + 19 < self.settings.width - 60:
            self.rect.width = self.get_text_surface().get_width() + 40
            self.color = self.settings.get_color("black")
        else:
            self.color = self.settings.get_color("red")
