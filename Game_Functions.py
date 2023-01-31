import pygame
import sys
from Card import Card


# Keyboard input holder -------------------------------------------------------


def events(settings, interface, user):
    """Keep track on the keyboard events."""
    for event in pygame.event.get():
        pygame.key.set_repeat(300, 100)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            interface.mouse_click(event, settings)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                interface.set_next_button_active(settings)
            elif event.key == pygame.K_RETURN:
                if interface.get_button_active():
                    interface.ret_press(settings)

            elif event.key == pygame.K_ESCAPE:
                interface.set_buttons_unactive()

            elif interface.get_text_button_active():
                if event.key == pygame.K_BACKSPACE:
                    settings.user_text = settings.user_text[:-1]

                elif not interface.get_delete_only():
                    settings.user_text += event.unicode

                interface.update_network_text(user, settings)

            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

# Screen effects --------------------------------------------------------------


def drawing(screen, settings, card_group):
    """Drawing cards effects in the background."""
    settings.count += 1
    if settings.count % 100 == 0:
        card = Card(settings)
        card_group.add(card)
        settings.count = 0
    card_group.update(screen, settings)


def update(settings, screen, interface, user):
    """Sync interface elements at screen."""
    interface.update_interface(screen, settings, user)

# Game logic ------------------------------------------------------------------


def collect_ansewrs():
    """Nothing yet."""
    pass
