import pygame 
from pygame.locals import * 
from sys import exit 
from config import * 

pygame.init()
pygame.mixer.init()

def tela_init (window):
    clock = pygame.time.Clock()
    bg = pygame.image.load('pacmantela.png').convert()
    bg = pygame.transform.scale(bg, (largura, altura))
    bg_rect = bg.get_rect()
    # espaço para imagens 
    game = True
    
# ===== Loop principal =====
    while game: 
        clock.tick(FPS)      # Frames por segundo 

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT : 
                state = QUIT
                game = False
            if event.type == pygame.KEYDOWN: 
                state = GAME
                game = False 
         # colocar imagens 
        window.blit(bg, bg_rect)
        pygame.display.update()

    return state

    
    