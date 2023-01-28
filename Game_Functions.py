import pygame
import sys
from Card import Card


def events(settings, interface, screen):

    for event in pygame.event.get():
        pygame.key.set_repeat(300, 100)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            interface.mouse_click(event, settings)

        elif event.type == pygame.KEYDOWN and (
            interface.button1_active or interface.button2_active
        ):
            if event.key == pygame.K_BACKSPACE:
                settings.user_text = settings.user_text[:-1]
                interface.reset_blink(settings)
            elif event.key == pygame.K_TAB or event.key == pygame.K_RETURN:
                interface.change_button(settings)
            elif event.key == pygame.K_ESCAPE:
                interface.turn_off_button(1)
                interface.turn_off_button(2)
            elif event.key != pygame.K_RETURN:
                if interface.button1_width_growth and interface.button1_active:
                    settings.user_text += event.unicode
                    interface.reset_blink(settings)
                elif interface.button2_width_growth and interface.button2_active:
                    settings.user_text += event.unicode
                    interface.reset_blink(settings)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_TAB or event.key == pygame.K_RETURN:
                interface.change_button(settings)


def drawing(screen, interface, settings, card_group):
    settings.count += 1
    settings.count_blink += 1
    if settings.count % 100 == 0:
        card = Card(settings)
        card_group.add(card)
        settings.count = 0
    card_group.update(screen, settings)
    if settings.count_blink % 70 == 0:
        interface.button_cursor_draw = not interface.button_cursor_draw
        settings.count_blink = 0
    if interface.button_cursor_draw:
        interface.button_cursor(screen, settings)
    interface.submit_button_animation(settings)


def blit(settings, screen, interface):
    interface.update_text(settings)
    interface.blit(screen, settings)


def welcome():
    return "You are welcome to the divination game"


def collect_ansewrs(players, interface):
    """Sync the players information and assert their number guess."""
    players_dictionary = {}
    total = 0
    for player in range(players):
        player_name = interface.button1_text
        player_ansewrs = int(interface.button2_text)
        players_dictionary[player_name] = player_ansewrs
        total += player_ansewrs
    total = total / players * 0.8
    ansewr_list = [players_dictionary, total]
    return ansewr_list


def winner(players, interface):
    """Compile all the running functions for now and return the winner."""
    welcome()
    ansewr_list = collect_ansewrs(players, interface)
    total = ansewr_list[1]
    error = 100
    winner_player = ""
    for player in ansewr_list[0]:
        if abs(ansewr_list[0][player] - total) <= error:
            error = abs(ansewr_list[0][player] - total)
            winner_player = player
    return winner_player
