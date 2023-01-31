from Button import Button
import pygame
import sys


class ClickButton(Button):
    def __init__(self, rect, color, settings, text):
        super().__init__(rect, color, settings)
        self.text = text
        self.text_color = settings.get_color("white")
        self.text_surface = settings.base_font.render(self.text, True, self.text_color)
        self.cycle = True

# Methods ---------------------------------------------------------------------

    def click(self, settings):
        pygame.quit()
        sys.exit()

    # Setters -----------------------------------------------------------------

    def set_active(self, settings):
        super().set_active(settings)
        self.color = self.settings.get_color("active")
        self.cycle = True

    def set_active_by_mouse(self, settings):
        if self.get_rect().collidepoint(pygame.mouse.get_pos()):
            self.set_active(settings)
            self.cycle = False
        elif not self.cycle:
            self.set_unactive()

    def set_unactive(self):
        super().set_unactive()
        self.color = self.settings.get_color("passive")

