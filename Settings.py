import pygame


class Settings:
    def __init__(self):
        self.width = 640
        self.height = 600
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
        self.user_text = ""
