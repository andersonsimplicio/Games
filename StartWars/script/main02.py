import pygame
import os,sys,time

'''
Criando a movimentação do jogo com Mouse
'''

pygame.init()
width, height = 1200, 650
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("N A S A")

nave = pygame.image.load(os.path.join("assets","img","ship.png")).convert_alpha()
nave = pygame.transform.scale(nave,(40,40))
#Aula 10 de maio
navRec = nave.get_rect(center=(500,500))
print(navRec)


bg1 = pygame.image.load(os.path.join("assets","img","espaco.png")).convert()

bgR1 = bg1.get_rect(center=((width/2,(height/2))))

font = pygame.font.Font(os.path.join("assets","Font","Sigmar","Sigmar-Regular.ttf"),16)
texto = font.render('S T A R - GAME', True,(65,105,225))
recText = texto.get_rect(center=(100,10))
loop = True
relogio = pygame.time.Clock()

while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        '''
        if event.type == pygame.MOUSEMOTION:
             print(event.pos)
             navRec.center = event.pos
        '''
        if event.type == pygame.MOUSEBUTTONUP:
             print(f"Tiro {event.pos}")

    #Limitando os frames  (FPS)
    relogio.tick(120)
    # entrada do mouse
    #print(pygame.mouse.get_pressed())
    #print(pygame.mouse.get_pos())
    navRec.center = pygame.mouse.get_pos()
    # Atualizando os Quadros

    display.fill('black')
    display.blit(bg1, bgR1)    

    #utilizando o retangulo para poscionar a nave
    display.blit(nave, navRec)
   
    #display.blit(texto, (10,10))
    display.blit(texto, recText)
    
    pygame.display.update()
    
pygame.quit()