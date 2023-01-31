from Button import Button
from Rect import Rect
import pygame


class TextButton(Button):
    count = 0

    def __init__(self, rect, color, settings):
        super().__init__(rect, color, settings)
        self.delete_only = False

        self.id = self.add_instance()
        self.input_list = ["Username", "Guess"]
        self.empty_text = self.input_list[self.id - 1]

        self.text_rect = Rect((
            self.rect.x,
            self.rect.y + 5,
            2,
            self.rect.height - 10,
        ), settings.get_color("black"), settings)

# Methods ---------------------------------------------------------------------

    def add_instance(self):
        type(self).count += 1
        return type(self).count

    def draw(self, screen, settings):
        pygame.draw.rect(
            screen,
            self.color,
            self.rect,
            border_radius=10,
            width=3
        )

        self.set_text(settings)
        screen.blit(self.get_text_surface(), (self.rect.x + 5, self.rect.y + 5))
        self.text_rect.draw_when_active(screen, settings)

    def click(self, settings):
        self.set_active(settings)

    def verify_emtpy(self):
        if not self.get_active() and len(self.get_text()) == 0:
            return self.input_list[self.id - 1], (183, 183, 183)
        else:
            return self.text, self.settings.get_color("black")

    # Setters -----------------------------------------------------------------

    def set_width(self):
        if self.get_text_surface().get_width() + 19 <= self.settings.button_width:
            self.rect.width = self.settings.button_width
            return False

        elif self.get_text_surface().get_width() + 19 < self.settings.width - 60:
            self.rect.width = self.get_text_surface().get_width() + 40
            self.color = self.settings.get_color("black")
            return False

        else:
            self.color = self.settings.get_color("red")
            return True

    def set_text(self, settings):
        if self.get_active():
            self.text = settings.user_text
            self.set_text_surface()
            self.delete_only = self.set_width()
            self.text_rect.set_x_pos(self.rect.x + 5 + self.text_surface.get_width())
        else:
            self.set_text_surface()

    def set_active(self, settings):
        if not self.get_active():
            settings.user_text = self.get_text()
            pygame.mixer.Sound.play(self.settings.button_sound)
            self.text_rect.set_active(settings)
        super().set_active(settings)

    def set_unactive(self):
        if self.get_active():
            self.text_rect.set_unactive()
        super().set_unactive()

    def set_text_surface(self):
        text, color = self.verify_emtpy()
        self.text_surface = self.settings.base_font.render(
            text, True, color
        )

    # Getters -----------------------------------------------------------------

    def get_delete_only(self):
        return self.delete_only
