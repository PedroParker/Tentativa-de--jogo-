import pygame
import sys


def events(settings, interface):

    for event in pygame.event.get():
        pygame.key.set_repeat(300, 100)
        if event.type == pygame.QUIT:
            print(winner(1, interface))
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if interface.buttom1_rect.collidepoint(event.pos):
                interface.buttom1_color = settings.color_active
                interface.buttom1_active = True
                settings.user_text = interface.buttom1_text
            else:
                interface.buttom1_color = settings.color_passive
                interface.buttom1_active = False

            if interface.buttom2_rect.collidepoint(event.pos):
                interface.buttom2_color = settings.color_active
                interface.buttom2_active = True
                settings.user_text = interface.buttom2_text
            else:
                interface.buttom2_color = settings.color_passive
                interface.buttom2_active = False

        if event.type == pygame.KEYDOWN and (
            interface.buttom1_active or interface.buttom2_active
        ):
            if event.key == pygame.K_BACKSPACE:
                settings.user_text = settings.user_text[:-1]
            elif (
                len(settings.user_text) <= 10
                and event.key != pygame.K_ESCAPE
                and event.key != pygame.K_RETURN
            ):
                settings.user_text += event.unicode


def drawing(screen, interface):
    pygame.draw.rect(screen, interface.buttom1_color, interface.buttom1_rect)
    pygame.draw.rect(screen, interface.buttom2_color, interface.buttom2_rect)
    pygame.draw.rect(
        screen, interface.mensagem_text_color, interface.mensagem_text_rect
    )


def blit(base_font, settings, screen, interface):
    interface.update_text(settings)
    interface.blit(base_font, screen)


def welcome():
    return "You are welcome to the divination game"


def collect_ansewrs(players, interface):
    """Sync the players information and assert their number guess."""
    players_dictionary = {}
    total = 0
    for player in range(players):
        player_name = interface.buttom1_text
        player_ansewrs = int(interface.buttom2_text)
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
