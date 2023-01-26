import pygame
import sys


def events(settings, interface):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if interface.rect.collidepoint(event.pos):
                settings.active = True
            else:
                settings.active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                settings.user_text = settings.user_text[:-1]
            else:
                settings.user_text += event.unicode
    if settings.active:
        settings.color = settings.color_active
    else:
        settings.color = settings.color_passive


def drawing(settings, screen, interface):
    pygame.draw.rect(screen, settings.color, interface.rect)


def blit(base_font, settings, screen, interface):
    text_suface = base_font.render(settings.user_text, True, (255, 255, 255))
    screen.blit(text_suface, (interface.rect.x + 5, interface.rect.y + 5))


def welcome():
    return "You are welcome to the divination game"


def collect_ansewrs(players):
    """Perform the players information and assert their number guess."""
    """Get it?."""
    players_dictionary = {}
    total = 0
    for player in range(players):
        player_name = input("Coloque seu nome: ")
        player_ansewrs = int(input("Esconlha um número entre 1 e 100: "))
        players_dictionary[player_name] = player_ansewrs
        total += player_ansewrs
    total = total / players * 0.8
    ansewr_list = [players_dictionary, total]
    return ansewr_list


def winner(ansewr_list):
    """Compile all the running functions for now and return the winner."""
    welcome()
    total = ansewr_list[1]
    error = 100
    winner_player = ""
    for player in ansewr_list[0]:
        if abs(ansewr_list[0][player] - total) <= error:
            error = abs(ansewr_list[0][player] - total)
            winner_player = player
    return winner_player
