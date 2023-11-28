import pygame 
from sprites import  *
from config import *
from init_tela import * 
from over_tela import * 

pygame.init()
pygame.mixer.init()  #  inicialização do módulo de áudio do pygame;

# ----- Gera tela principal

window = pygame.display.set_mode((largura, altura)) # janela com 600 pixels de largura e 300 pixels de altura
pygame.display.set_caption('Pac burguer') # titulo do jogo 
font = pygame.font.SysFont(None, 48)
background = pygame.image.load('fundo_tela.jpg').convert()   # tela de fundo 
background_rect = background.get_rect()

# Carrega os sons do jogo
pygame.mixer.music.load('joker-boy-109889.mp3')
pygame.mixer.music.set_volume(0.4)
good_sound = pygame.mixer.Sound('arcade-videogame-sound-160948.mp3')
explosion_sound = pygame.mixer.Sound('hq-explosion-6288.mp3')

all_sprites = pygame.sprite.Group()

player = jogador()
all_sprites.add(player)

clock = pygame.time.Clock()    

ref = pygame.time.get_ticks()
game = True 

 
pygame.mixer.music.play(loops=-1)  # começa a tocar o som de fundo em loop;

while game :      # loop principal 
    clock.tick(FPS)   # Quanto mais frames, mais rápido o objeto vai se mexer 
    window.fill((0,0,0))       # preenche a tela com  a cor preta para não mostrar a trajetória do objeto

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            game = False

        if event.type == pygame.KEYDOWN :          # keydown é qualquer tecla selecionada 
            if event.key == pygame.K_LEFT :           # teclas são as setas b
                player.speedx -= speed 
            
            if event.key == pygame.K_RIGHT : 
                player.speedx += speed 

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT :           # teclas são as setas 
                player.speedx = 0
            
            if event.key == pygame.K_RIGHT : 
                player.speedx = 0

    now = pygame.time.get_ticks()

    if now - ref >= 1000:     # criar bombas e hamburguer novos a cada 1 segundo 
        objeto_obstaculo = obstaculo()
        objeto_comida = comida(objeto_obstaculo.rect.x)
        all_sprites.add(objeto_obstaculo, objeto_comida)
        ref = now
    
    all_sprites.update()
    window.blit(background, background_rect)
    all_sprites.draw(window)



    pygame.display.update()  # a cada iteração do loop principal do jogo a tela é atualizada 
