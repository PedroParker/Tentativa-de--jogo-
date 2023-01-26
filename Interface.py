import pygame


class Interface(pygame.sprite.Sprite):
    def __init__(self, settings):
        super().__init__()
        # self.image = pygame.image.load("ImageDirectory.png")
        self.buttom1_active = False
        self.buttom1_color = settings.color_passive
        self.buttom1_rect = pygame.Rect(200, 200, 140, 32)
        self.buttom1_text = ""

        self.buttom2_active = False
        self.buttom2_color = settings.color_passive
        self.buttom2_rect = pygame.Rect(200, 500, 140, 32)
        self.buttom2_text = ""

        self.mensagem_text_rect = pygame.Rect(200, 50, 140, 32)
        self.mensagem_text = "Welcome"
        self.mensagem_text_color = (0, 0, 0)

    def update_text(self, settings):
        if self.buttom1_active:
            self.buttom1_text = settings.user_text
        elif self.buttom2_active:
            self.buttom2_text = settings.user_text

    def blit(self, base_font, screen):
        buttom1_text_surface = base_font.render(
            self.buttom1_text, True, (255, 255, 255)
        )
        screen.blit(
            buttom1_text_surface,
            (self.buttom1_rect.x + 5, self.buttom1_rect.y + 5),
        )
        buttom2_text_surface = base_font.render(
            self.buttom2_text, True, (255, 255, 255)
        )
        screen.blit(
            buttom2_text_surface,
            (self.buttom2_rect.x + 5, self.buttom2_rect.y + 5),
        )
        mensagem_text_surface = base_font.render(
            self.mensagem_text, True, (255, 255, 255)
        )
        screen.blit(
            mensagem_text_surface,
            (self.mensagem_text_rect.x + 5, self.mensagem_text_rect.y + 5),
        )
