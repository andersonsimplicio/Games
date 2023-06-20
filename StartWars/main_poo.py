import pygame, sys,os
from classes import Nave

#Configuração basica
width,height = 1200,720
display_surface = pygame.display.set_mode((width,height))   
pygame.display.set_caption("Tiros em Aerolitos")
FPS = pygame.time.Clock() 

#Criando a Sprite Group
group_sprite = pygame.sprite.Group() 
#Criando a Nave
nave = Nave(group_sprite)

bg1 = pygame.image.load(os.path.join("assets","img","espaco.png")).convert()


while True:
    #Tratando Evento de loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Calculo do delta time
    dt = FPS.tick(60) / 1000.0
    #incluido imagem de Fundo
    display_surface.blit(bg1,(0,0))
    
    group_sprite.draw(display_surface)

    pygame.display.update()