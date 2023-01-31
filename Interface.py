from ClickButton import ClickButton
from Text import Text
from TextButton import TextButton
from VisualizeButton import VisualizeButton


class Interface:
    def __init__(self, settings):
        self.buttons = [
            ClickButton(
                (
                    settings.button_x + settings.button_width - 125,
                    settings.button_y + settings.button_y_space * 2 + 10,
                    125,
                    40,
                ),
                settings.get_color("passive"),
                settings,
                "Submit",
            ),
            TextButton(
                (
                    settings.button_x,
                    settings.button_y,
                    settings.button_width,
                    settings.button_height,
                ),
                settings.get_color("black"),
                settings,
            ),
            TextButton(
                (
                    settings.button_x,
                    settings.button_y + settings.button_y_space,
                    settings.button_width,
                    settings.button_height,
                ),
                settings.get_color("black"),
                settings,
            ),
        ]
        self.visualize_button = VisualizeButton(
            (
                settings.button_x,
                settings.button_y + 4 * settings.button_y_space,
                settings.button_width,
                settings.button_height,
            ),
            settings.get_color("black"),
            settings,
        )

        self.text = Text('Press "q" to quit', (50, 45), settings)

    # Methods ---------------------------------------------------------------------

    def update_interface(self, screen, settings, user):
        for button in self.buttons:
            button.draw(screen, settings)
            if isinstance(button, ClickButton):
                button.set_active_by_mouse(settings)

        self.update_visualize_buttons(screen, user, settings)

    def mouse_click(self, event, settings):
        for button in self.buttons:
            if button.get_rect().collidepoint(event.pos):
                button.click(settings)
            else:
                button.set_unactive()

    def ret_press(self, settings):
        for button in self.buttons:
            if button.get_active():
                button.click(settings)

    def update_visualize_buttons(self, screen, user, settings):
        self.text.draw(screen)
        self.visualize_button.set_text(user)
        self.visualize_button.draw(screen, settings)

    def update_network_text(self, user, settings):
        if self.buttons[1].get_active():
            user.set_text(settings.user_text)

    # Setters -----------------------------------------------------------------

    def set_next_button_active(self, settings):
        for idx, button in enumerate(self.buttons):
            if button.get_active():
                button.set_unactive()
                self.buttons[(idx + 1) % len(self.buttons)].set_active(settings)
                return
        self.buttons[1].set_active(settings)

    def set_buttons_unactive(self):
        for button in self.buttons:
            button.set_unactive()

    # getters -----------------------------------------------------------------

    def get_text_button_active(self):
        for button in self.buttons:
            if button.get_active() and isinstance(button, TextButton):
                return True

    def get_button_active(self):
        for button in self.buttons:
            if button.get_active():
                return True

    def get_delete_only(self):
        for button in self.buttons:
            if isinstance(button, TextButton) and button.get_active():
                return button.get_delete_only()
        return True
