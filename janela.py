import pygame 
from pygame.locals import * 
from sys import exit 
from sprites import * 

pygame.init()
pygame.mixer.init()  #  inicialização do módulo de áudio do pygame;

# ----- Gera tela principal

largura = 640 
altura = 480

window = pygame.display.set_mode((largura, altura)) # janela com 600 pixels de largura e 300 pixels de altura
pygame.display.set_caption('Pac burguer') # titulo do jogo 

FPS = 60 


x = largura/ 2   # meio da tela 
y = altura - 60

pygame.display.set_caption(' Pygame ')   # título do jogo 

clock = pygame.time.Clock()    # analisar troca para speed

speed = 20 
game = True 

while game :      # loop principal 
    clock.tick(FPS)   # Quanto mais frames, mais rápido o objeto vai se mexer 
    tela.fill((0,0,0))       # preenche a tela com  a cor preta para não mostrar a trajetória do objeto
    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit( )
            exit ()


        if event.type == KEYDOWN :          # keydown é qualquer tecla selecionada 
            if event.key == K_LEFT :           # teclas são as setas b
                x -= speed 
            
            if event.key == K_RIGHT : 
                x += speed 


    if pygame.key.get_pressed ()[K_LEFT]:     # quando essas teclas forem selecionadas o objeto vai se movimentar normalmente sem travar 
        x -= 20 

    if pygame.key.get_pressed ()[K_RIGHT]:
        x += 20 



    pygame.draw.rect(tela , (255,0,0), (x, y, 40, 10))   # desenha retangulo 

   


    pygame.display.update()  # a cada iteração do loop principal do jogo a tela é atualizada 
