import pygame
import sys


class Interface:
    def __init__(self, settings, screen):
        self.button1_active = False
        self.button1_width_growth = True
        self.button1_color = settings.color_black
        self.button1_rect = pygame.Rect(
            settings.button_x,
            settings.button_y,
            settings.button_width,
            settings.button_height,
        )
        self.button1_rect.topleft = (settings.button_x, settings.button_y)
        self.button1_text = ""
        self.button1_empty = True

        self.button2_active = False
        self.button2_width_growth = True
        self.button2_color = settings.color_black
        self.button2_rect = pygame.Rect(
            settings.button_x,
            settings.button_y + settings.button_y_space,
            settings.button_width,
            settings.button_height,
        )
        self.button2_text = ""
        self.button2_empty = True

        self.mensagem_text = 'Press "Q" to quit'
        self.mensagem_text_color = (255, 255, 255)

        self.button_cursor_size = self.button1_rect.height
        self.button_cursor_draw = True

        self.submit_button_width = 125
        self.submit_button_height = 40
        self.submit_button_passive_color = settings.color_passive
        self.submit_button_active_color = settings.color_active
        self.submit_button_color = self.submit_button_passive_color
        self.submit_message = "Submit"
        self.submit_button_rect = pygame.Rect(
            settings.button_x + settings.button_width - self.submit_button_width,
            settings.button_y + settings.button_y_space * 2 + 10,
            self.submit_button_width,
            self.submit_button_height,
        )
        self.submit_button_active = False
        self.mouse_pass = False

    def update_text(self, settings):
        if self.button1_active:
            self.button1_text = settings.user_text
        elif self.button2_active:
            self.button2_text = settings.user_text

    def check_empty1(self, settings):
        if self.button1_empty:
            return ["Username", True, (183, 183, 183)]
        else:
            return [self.button1_text, True, settings.font_color]

    def check_empty2(self, settings):
        if self.button2_empty:
            return ["Guess", True, (183, 183, 183)]
        else:
            return [self.button2_text, True, settings.font_color]

    def blit(self, screen, settings):
        element = self.check_empty1(settings)
        button1_text_surface = settings.base_font.render(
            element[0], element[1], element[2]
        )
        width1 = button1_text_surface.get_width()
        if width1 > settings.button_width:
            pass
        elif width1 < settings.button_width:
            width1 = settings.button_width
        if width1 >= settings.width - 100:
            self.button1_width_growth = False
            self.button1_color = (200, 20, 20)
        else:
            self.button1_color = settings.color_black
            self.button1_width_growth = True
        self.button1 = pygame.draw.rect(
            screen,
            self.button1_color,
            (
                settings.button_x,
                settings.button_y,
                width1 + 20,
                settings.button_height,
            ),
            border_radius=10,
            width=3,
        )
        screen.blit(
            button1_text_surface,
            (self.button1_rect.x + 5, self.button1_rect.y),
        )
        element = self.check_empty2(settings)
        button2_text_surface = settings.base_font.render(
            element[0], element[1], element[2]
        )
        width2 = button2_text_surface.get_width()
        if width2 > settings.button_width:
            pass
        elif width2 < settings.button_width:
            width2 = settings.button_width
        if width2 >= settings.width - 100:
            self.button2_width_growth = False
            self.button2_color = (200, 20, 20)
        else:
            self.button2_color = settings.color_black
            self.button2_width_growth = True
        self.button2 = pygame.draw.rect(
            screen,
            self.button2_color,
            (
                settings.button_x,
                settings.button_y + settings.button_y_space,
                width2 + 20,
                settings.button_height,
            ),
            border_radius=10,
            width=3,
        )
        screen.blit(
            button2_text_surface,
            (self.button2_rect.x + 5, self.button2_rect.y),
        )
        mensagem_text_surface = settings.base_font.render(
            self.mensagem_text, True, settings.font_color
        )
        screen.blit(
            mensagem_text_surface,
            (settings.width / 2 - mensagem_text_surface.get_width() / 2, 45),
        )
        self.submit_button = pygame.draw.rect(
            screen,
            self.submit_button_color,
            (self.submit_button_rect),
            border_radius=10,
        )
        submit_message_surface = settings.base_font.render(
            self.submit_message, True, (255, 255, 255)
        )
        screen.blit(
            submit_message_surface,
            (self.submit_button_rect.x + 5, self.submit_button_rect.y),
        )

    def submit_button_animation(self, settings):
        if self.submit_button_rect.collidepoint(pygame.mouse.get_pos()):
            if not self.submit_button_active:
                self.active_button(settings, 3)
                self.mouse_pass = True
        elif self.button1_active or self.button2_active or self.mouse_pass:
            self.turn_off_button(3)
            self.mouse_pass = False

    def button_cursor(self, screen, settings):
        text = settings.base_font.render(settings.user_text, True, (0, 0, 0))
        if self.button1_active:
            pygame.draw.rect(
                screen,
                (0, 0, 0),
                (
                    self.button1_rect.x + text.get_width() + 5,
                    self.button1_rect.y + 5,
                    2,
                    self.button1_rect.height - 10,
                ),
            )
        elif self.button2_active:
            pygame.draw.rect(
                screen,
                (0, 0, 0),
                (
                    self.button2_rect.x + text.get_width() + 5,
                    self.button2_rect.y + 5,
                    2,
                    self.button2_rect.height - 10,
                ),
            )

    def change_button(self, settings):
        if self.button1_active:
            self.active_button(settings, 2)
            self.turn_off_button(1)
        elif self.button2_active:
            self.active_button(settings, 3)
            self.turn_off_button(2)
        else:
            self.active_button(settings, 1)
            self.turn_off_button(3)

    def turn_off_button(self, n):
        if n == 1:
            self.button1_active = False
            if self.button1_text == "":
                self.button1_empty = True
        if n == 2:
            self.button2_active = False
            if self.button2_text == "":
                self.button2_empty = True
        if n == 3:
            self.submit_button_active = False
            self.submit_button_color = self.submit_button_passive_color

    def reset_blink(self, settings):
        self.button_cursor_draw = True
        settings.count_blink = 0

    def active_button(self, settings, n):
        if n == 1:
            self.button1_empty = False
            self.button1_active = True
            settings.user_text = self.button1_text
        if n == 2:
            self.button2_empty = False
            self.button2_active = True
            settings.user_text = self.button2_text
        if n == 3:
            self.submit_button_active = True
            self.submit_button_color = self.submit_button_active_color
        self.reset_blink(settings)
        pygame.mixer.Sound.play(settings.button_sound)

    def mouse_click(self, event, settings):
        if self.button1_rect.collidepoint(event.pos):
            self.active_button(settings, 1)
        else:
            self.turn_off_button(1)
        if self.button2_rect.collidepoint(event.pos):
            self.active_button(settings, 2)
        else:
            self.turn_off_button(2)
        if self.submit_button_rect.collidepoint(event.pos):
            pygame.quit()
            sys.exit()
