import pygame


class Settings:
    def __init__(self, screen):
        self.width = screen.get_rect().width
        self.height = screen.get_rect().height
        self.backgroud_color = (255, 255, 255)
        self.color_active = pygame.Color("lightskyblue3")
        self.color_passive = pygame.Color("chartreuse4")
        self.button_x = 200
        self.button_y = 200
        self.button_y_space = 50
        self.button_width = 200
        self.button_height = 40
        self.clock = pygame.time.Clock()
        self.font_color = (0, 0, 0)
        self.font = "Resources/CascadiaCodeItalic.ttf"
        self.base_font = pygame.font.Font(self.font, 32)
        self.user_text = ""
        self.count = 99
        self.count_blink = 0
        self.music = pygame.mixer.music.load("Resources/awesomeness.wav")
        self.button_sound = pygame.mixer.Sound("Resources/sfx_sounds_button6.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
        self.button_sound.set_volume(0.2)
