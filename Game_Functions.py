import pygame
import sys
from Card import Card


def events(settings, interface):

    for event in pygame.event.get():
        pygame.key.set_repeat(300, 100)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if interface.button1_rect.collidepoint(event.pos):
                interface.button1_empty = False
                interface.button1_active = True
                settings.user_text = interface.button1_text
            else:
                interface.button1_active = False
                if interface.button1_text == "":
                    interface.button1_empty = True

            if interface.button2_rect.collidepoint(event.pos):
                interface.button2_empty = False
                interface.button2_active = True
                settings.user_text = interface.button2_text
            else:
                interface.button2_active = False
                if interface.button2_text == "":
                    interface.button2_empty = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN and (
            interface.button1_active or interface.button2_active
        ):
            if event.key == pygame.K_BACKSPACE:
                settings.user_text = settings.user_text[:-1]
            elif (
                len(settings.user_text) <= 9
                and event.key != pygame.K_ESCAPE
                and event.key != pygame.K_RETURN
            ):
                settings.user_text += event.unicode


def drawing(screen, interface, settings, card_group):
    pygame.draw.rect(
        screen, interface.mensagem_text_color, interface.mensagem_text_rect
    )
    settings.count += 1
    if settings.count % 100 == 0:
        card = Card(settings)
        card_group.add(card)
        settings.count = 0
    card_group.update(screen, settings)
    screen.blit(interface.box_image, (settings.button_x, settings.button_y))
    screen.blit(
        interface.box_image,
        (settings.button_x, settings.button_y + settings.button_y_space),
    )


def blit(base_font, settings, screen, interface):
    interface.update_text(settings)
    interface.blit(base_font, screen, settings)


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
