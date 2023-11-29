import pygame
from config import *
from tela_jogo import *
from over_tela import *
from init_tela import *
from sprites import *

pygame.init()
pygame.mixer.init()  #  inicialização do módulo de áudio do pygame;

window = pygame.display.set_mode((largura, altura)) # janela com 600 pixels de largura e 300 pixels de altura
pygame.display.set_caption('Pac burguer') # titulo do jogo 

pygame.mixer.music.load('joker-boy-109889.mp3')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops=-1)  # começa a tocar o som de fundo em loop;

state = INIT
while state != QUIT:
    if state == INIT:
        state = tela_init(window)
    if state == GAME:
        state = tela_jogo(window)
    if state == OVER:
        state = over_tela(window)

pygame.quit()