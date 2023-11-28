import pygame 
from config import *

def over_tela(window): 
    clock = pygame.time.Clock()

    # imagens para colocar 


    game = True 

    # ===== Loop principal =====
    while game: 
        clock.tick(FPS)     # frames por segundo 

        for event in pygame.event.gt(): 
            if event.type == pygame.QUIT:
                state = QUIT 
                game = False
            if event.type == pygame.KEYDOWN:
                state = GAME 
                game = False 

    window.blit()      # colocar imagem 
    pygame.display.update()

    return state