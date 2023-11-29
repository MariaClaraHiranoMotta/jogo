import pygame 
from config import *

def over_tela(window): 
    clock = pygame.time.Clock()

    # imagens para colocar 
    img = pygame.transform.scale(pygame.image.load('pactriste.jpeg').convert(),(largura, altura))  # imagem game over
    img_rect = img.get_rect()

    running =  True 

    # ===== Loop principal =====
    while running: 
        clock.tick(FPS)     # frames por segundo 

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                state = QUIT 
                running = False
            if event.type == pygame.KEYDOWN:
                state = GAME 
                running = False 

        window.blit(img, img_rect)      # colocar imagem 
        pygame.display.update()

    return state