import pygame 
from pygame.locals import * 
from sys import exit 
from janela import * 

pygame.init()
pygame.mixer

INIT = 0
GAME = 1
OVER = 2

def tela_ini (window):
    clock = pygame.time.Clock()

    # espaço para imagens 
    game = True
    
# ===== Loop principal =====
    while game: 
        clock.tip(FPS)      # Frames por segundo 

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT : 
                state = QUIT
                game = False
            elif event.type == pygame.KEYDOWN: 
                state = GAME
                game = False 
        
        window.blit()  # colocar imagens 
        pygame.display.update()

    return state

    
    