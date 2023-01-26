import pygame
from Settings import Settings
import Game_Functions as game_f
from Interface import Interface

settings = Settings()
interface = Interface(settings)
pygame.init()
screen = pygame.display.set_mode((settings.width, settings.height))
base_font = pygame.font.Font(None, 32)
pygame.display.set_caption("Jogo")
while True:
    game_f.events(settings, interface)
    screen.fill((255, 255, 255))
    game_f.drawing(screen, interface)
    game_f.blit(base_font, settings, screen, interface)
    pygame.display.flip()
    settings.clock.tick(60)
