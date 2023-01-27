import pygame


class Interface(pygame.sprite.Sprite):
    def __init__(self, settings):
        super().__init__()
        self.image = pygame.image.load("Resources/box.png")
        self.rect = self.image.get_rect()
        self.button1_active = False
        self.button1_color = settings.color_passive
        self.button1_rect = self.image.get_rect()
        self.button1_rect.topleft = (settings.button_x, settings.button_y)
        self.button1_text = ""

        self.button2_active = False
        self.button2_color = settings.color_passive
        self.button2_rect = self.image.get_rect()
        self.button2_rect.topleft = (
            settings.button_x,
            settings.button_y + settings.button_y_space,
        )
        self.button2_text = ""

        self.mensagem_text_rect = pygame.Rect(settings.width / 2, 40, 250, 32)
        self.mensagem_text = "Welcome to the divination game"
        self.mensagem_text_color = (255, 255, 255)

    def update_text(self, settings):
        if self.button1_active:
            self.button1_text = settings.user_text
        elif self.button2_active:
            self.button2_text = settings.user_text

    def blit(self, base_font, screen, settings):
        button1_text_surface = base_font.render(
            self.button1_text, True, settings.font_color
        )
        screen.blit(
            button1_text_surface,
            (self.button1_rect.x + 5, self.button1_rect.y),
        )
        button2_text_surface = base_font.render(
            self.button2_text, True, settings.font_color
        )
        screen.blit(
            button2_text_surface,
            (self.button2_rect.x + 5, self.button2_rect.y),
        )
        mensagem_text_surface = base_font.render(
            self.mensagem_text, True, settings.font_color
        )
        screen.blit(
            mensagem_text_surface,
            (self.mensagem_text_rect.x + 5, self.mensagem_text_rect.y + 5),
        )
