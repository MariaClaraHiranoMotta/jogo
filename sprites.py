import pygame
from config import *
import random

class jogador(pygame.sprite.Sprite): 
    def __init__(self) :
         # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self) 

        self.image = pygame.image.load('pacman.png').convert_alpha()  # carrega imagem 
        self.image = pygame.transform.scale(self.image, (50, 50))     # tamamnho da imagem 
        self.rect = self.image.get_rect()      # monta perímetro para imagem 
        self.rect.bottom = altura
        self.rect.x = largura/2
        self.speedx = 0
    
    def update(self):
        self.rect.x += self.speedx

        if self.rect.x <= 0 :       # se o retangulo tentar passar da tela ele irá parar 
            self.speedx = 0

        # Mantem dentro da tela
        if self.rect.right > largura:
            self.speedx = 0
        if self.rect.left < 0:
            self.speedx = 0




class obstaculo(pygame.sprite.Sprite): 
    def __init__(self) : 
         # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('bomb.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.y = -50
        self.rect.x = random.randint(50,largura - 50)
        self.speedy = 5

    def update(self):
         # Atualizando a posição da bomba
        self.rect.y += self.speedy
        


class comida(pygame.sprite.Sprite): 
    def __init__(self, posicao_obstaculo): 
         # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('hamburger.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.y = -50
        self.rect.x = random.randint(50,largura - 50)
        while self.rect.x in range(posicao_obstaculo-10, posicao_obstaculo+10): # garante que a bomba e o hamburguer não estejam no mesmo espaço
            self.rect.x = random.randint(50,largura - 50)
        self.speedy = 4

    def update(self): 
         # Atualizando a posição do hamburger
        self.rect.y += self.speedy
        
       