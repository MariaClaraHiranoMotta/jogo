import pygame
from pygame.sprite import _Group 
from janela import *

class jogador(pygame.sprite.Sprite): 
    def __init__(self) :
         # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self) 

        self.image = pygame.image.load('pacman.png').convert_alpha()  # carrega imagem 
        self.image = pygame.transform.scale(self.image, (50, 50))     # tamamnho da imagem 
        self.rect = self.image.get_rect()      # monta perímetro para imagem 
        self.rect.y = altura - 30
        self.rect.x = largura/2
        self.speedx = 0
    
    def update(self):
        self.rect.x += self.speedx

        if self.rect.x <= 0 :       # se o retangulo tentar passar da tela ele irá parar 
            sel.speedx = 0

        if serf.rect.x 

        # Mantem dentro da tela
        if self.rect.right > largura:
            self.rect.right = largura
        if self.rect.left < 0:
            self.rect.left = 0




class obstaculo(pygame.sprite.Sprite): 
    def __init__(self) : 
         # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('bomb.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.y = 
        self.rect.x = 0
        self.speedy = 0

    def update(self):
         # Atualizando a posição da bomba
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        


class comida(pygame.sprite.Sprite): 
    def __init__(self): 
         # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('hamburger.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.,rect = self.image.get_rect()
        self.rect.y = 
        self.rect.x = 
        self.speedx = 0
        self.speedy = 0

    def update(self): 
         # Atualizando a posição do hamburger
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
       