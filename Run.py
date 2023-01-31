import pygame
from Settings import Settings
import Game_Functions as game_f
from Interface import Interface
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
    user = User()

    # Game stuff --------------------------------------------------------------

    while settings.get_run():

        screen.fill(settings.get_color("white"))

        # Game logic ----------------------------------------------------------

        game_f.events(settings, interface, user)  # Keyboard events
        game_f.drawing(screen, settings, card_group)  # background animation
        game_f.update(settings, screen, interface, user)  # Sync elements with window

        # Final compliment ----------------------------------------------------

        pygame.display.flip()
        settings.clock.tick(60)


if __name__ == "__main__":
    main()
