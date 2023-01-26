import pygame
from pygame.locals import *
from sys import exit

pygame.init()  # Inicia todas as funções do pygame

largura = 640
altura = 480

pygame.display.set_mode((largura, altura))  # Cria a nossa janela
pygame.display.set_caption("Jogo")  # Renomeia o titulo que fica na parte de cima da tela

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()  # Responsavel para fechar a janela
            exit()

    pygame.display.update()  # Responsavel por ficar atualizando a janela
