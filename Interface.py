import pygame
import sys


class Interface:
    def __init__(self, settings):
        self.box_image = pygame.image.load("Resources/box.png")
        self.button1_active = False
        self.button1_color = settings.color_passive
        self.button1_rect = self.box_image.get_rect()
        self.button1_rect.topleft = (settings.button_x, settings.button_y)
        self.button1_text = ""
        self.button1_empty = True

        self.button2_active = False
        self.button2_color = settings.color_passive
        self.button2_rect = self.box_image.get_rect()
        self.button2_rect.topleft = (
            settings.button_x,
            settings.button_y + settings.button_y_space,
        )
        self.button2_text = ""
        self.button2_empty = True

        self.mensagem_text = 'Press "Q" to quit'
        self.mensagem_text_color = (255, 255, 255)

        self.button_cursor_size = 3, self.box_image.get_rect().height
        self.button_cursor_draw = True

        self.submit_button_width = 125
        self.submit_button_height = 40
        self.submit_button_passive_color = (40, 180, 40)
        self.submit_button_active_color = (20, 200, 20)
        self.submit_button_color = self.submit_button_passive_color
        self.submit_message = "Submit"
        self.submit_button_rect = pygame.Rect(
            settings.button_x + settings.button_width - self.submit_button_width,
            settings.button_y + settings.button_y_space * 2 + 10,
            self.submit_button_width,
            self.submit_button_height,
        )

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
        screen.blit(
            button1_text_surface,
            (self.button1_rect.x + 5, self.button1_rect.y),
        )
        element = self.check_empty2(settings)
        button2_text_surface = settings.base_font.render(
            element[0], element[1], element[2]
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

    def submit_button_animation(self):
        if self.submit_button_rect.collidepoint(pygame.mouse.get_pos()):
            self.submit_button_color = self.submit_button_active_color
        else:
            self.submit_button_color = self.submit_button_passive_color

    def button_cursor(self, screen, settings):
        text = settings.base_font.render(settings.user_text, True, (0, 0, 0))
        if self.button1_active:
            pygame.draw.rect(
                screen,
                (0, 0, 0),
                (
                    self.button1_rect.x + text.get_width() + 5,
                    self.button1_rect.y + 3,
                    3,
                    self.button1_rect.height - 6,
                ),
            )
        elif self.button2_active:
            pygame.draw.rect(
                screen,
                (0, 0, 0),
                (
                    self.button2_rect.x + text.get_width() + 5,
                    self.button2_rect.y + 3,
                    3,
                    self.button2_rect.height - 6,
                ),
            )

    def change_button(self, settings):
        if self.button1_active:
            self.active_button(settings, 2)
            self.turn_off_button(1)
        else:
            self.active_button(settings, 1)
            self.turn_off_button(2)

    def turn_off_button(self, n):
        if n == 1:
            self.button1_active = False
            if self.button1_text == "":
                self.button1_empty = True
        if n == 2:
            self.button2_active = False
            if self.button2_text == "":
                self.button2_empty = True

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
        self.reset_blink(settings)
        pygame.mixer.Sound.play(settings.button_sound)

    def mouse_action(self, event, settings):
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
