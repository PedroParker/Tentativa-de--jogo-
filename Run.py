import pygame
from Settings import Settings
import Game_Functions as game_f
from Interface import Interface


def main():
    pygame.init()
    card_group = pygame.sprite.Group()
    screen = pygame.display.set_mode((640, 540))
    settings = Settings(screen)
    interface = Interface(settings)
    pygame.display.set_caption("Divination Game")
    while True:
        game_f.events(settings, interface, screen)
        screen.fill(settings.backgroud_color)
        game_f.drawing(screen, interface, settings, card_group)
        game_f.blit(settings, screen, interface)
        pygame.display.flip()
        settings.clock.tick(60)


if __name__ == "__main__":
    main()
