import pygame
from Settings import Settings
import Game_Functions as game_f
from Interface import Interface
from Network import Network
from User import User


def main():

    # pygame Initializing -----------------------------------------------------

    pygame.init()

    screen = pygame.display.set_mode((640, 540))
    pygame.display.set_caption("Divination Game")

    # Initializing instances --------------------------------------------------

    card_group = pygame.sprite.Group()
    settings = Settings(screen)
    interface = Interface(settings)
    # network = Network()
    # user = User(network)

    # Game stuff --------------------------------------------------------------

    while True:

        screen.fill(settings.color_white)

        # Game logic ----------------------------------------------------------

        game_f.events(settings, interface)  # Keyboard events
        game_f.drawing(screen, settings, card_group)  # background animation
        game_f.blit(settings, screen, interface)  # Sync elements with window

        # Final compliment ----------------------------------------------------

        pygame.display.flip()
        settings.clock.tick(60)


if __name__ == "__main__":
    main()
