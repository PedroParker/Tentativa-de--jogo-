import pygame


class Settings:
    def __init__(self, screen):

        # Screen dimension ----------------------------------------------------

        self.width = screen.get_rect().width
        self.height = screen.get_rect().height

        # Avalible colors -----------------------------------------------------

        self.color_active = pygame.Color("lightskyblue3")
        self.color_passive = pygame.Color("chartreuse4")
        self.color_white = (255, 255, 255)
        self.color_black = (0, 0, 0)
        self.color_red = (200, 40, 40)

        # Buttons general properties ------------------------------------------

        self.button_x = 40
        self.button_y = 200
        self.button_y_space = 50
        self.button_width = 200
        self.button_height = 40

        # Pygame general resorces ---------------------------------------------

        self.clock = pygame.time.Clock()
        self.font_color = self.color_black
        self.font = "Resources/CascadiaCodeItalic.ttf"
        self.base_font = pygame.font.Font(self.font, 25)
        self.button_sound = pygame.mixer.Sound("Resources/sfx_sounds_button6.wav")

        # Config existing properties

        pygame.mixer.music.load("Resources/awesomeness.wav")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)
        self.button_sound.set_volume(0.2)

        # Extra game logic stuff ----------------------------------------------

        self.user_text = ""
        self.count = 99
