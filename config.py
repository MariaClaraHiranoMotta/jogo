import pygame

pygame.init()

largura = 640 
altura = 480
FPS = 55
x = largura/ 2   # meio da tela 
y = altura - 60
speed = 8

QUIT = 0   # done
INIT = 1    # tela inicial 
GAME = 2   # playing 
OVER = 3    # explosão 
state = INIT

font = pygame.font.SysFont(None, 48)