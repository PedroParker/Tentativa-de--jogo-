import pygame
from Settings import Settings
import Game_Functions as game_f
from Interface import Interface

settings = Settings()
interface = Interface(settings)
pygame.init()
screen = pygame.display.set_mode((settings.width, settings.height))
base_font = pygame.font.Font(settings.font, 32)
pygame.display.set_caption("Divination Game")
while True:
    game_f.events(settings, interface)
    screen.fill(settings.backgroud_color)
    game_f.drawing(screen, interface, settings)
    game_f.blit(base_font, settings, screen, interface)
    pygame.display.flip()
    settings.clock.tick(60)
