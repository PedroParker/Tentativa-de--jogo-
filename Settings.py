import pygame


class Settings:
    def __init__(self):
        self.width = 640
        self.height = 600
        self.active = False
        self.color_active = pygame.Color("lightskyblue3")
        self.color_passive = pygame.Color("chartreuse4")
        self.color = self.color_passive
        self.clock = pygame.time.Clock()
        self.user_text = ""
