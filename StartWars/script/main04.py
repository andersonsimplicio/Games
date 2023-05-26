import pygame
import os,sys,time


'''
Criando os Disparos com laser e a lista de lasers
'''

def laser_update(laser_list,speed=300):
    for rec in laser_list:
        rec.y-=speed * dt
        if rec.bottom < 0:
            laser_list.remove(rec)


pygame.init()
width, height = 1200, 650
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("N A S A")

#Carregando as imagens
nave = pygame.image.load(os.path.join("assets","img","ship.png")).convert_alpha()
nave = pygame.transform.scale(nave,(40,40))
lasersurf = pygame.image.load(os.path.join("assets","img","laser.png")).convert_alpha()
lasersurf =pygame.transform.scale(lasersurf,(4,40))
laser_list = []
#Capturando o Retangulo 
navRec = nave.get_rect(center=(500,500))

print(navRec)

bg1 = pygame.image.load(os.path.join("assets","img","espaco.png")).convert()

bgR1 = bg1.get_rect(center=((width/2,(height/2))))



font = pygame.font.Font(os.path.join("assets","Font","Sigmar","Sigmar-Regular.ttf"),16)
texto = font.render('S T A R - GAME', True,(255,255,225))
recText = texto.get_rect(center=(100,10))
loop = True
relogio = pygame.time.Clock()

while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
      
        if event.type == pygame.MOUSEBUTTONDOWN:
            laser_rec = lasersurf.get_rect(midbottom=navRec.midtop)
            laser_list.append(laser_rec)
            print(laser_list)

    #Limitando os frames  (FPS)
    relogio.tick(60)
    #Limitando os frames  (FPS)
    dt = relogio.tick(60)/1000

    # entrada do mouse
    
    navRec.center = pygame.mouse.get_pos()
    # Atualizando os Quadros
    display.fill('black')
    display.blit(bg1, bgR1)    

    #utilizando o retangulo para poscionar a nave
    display.blit(nave, navRec)
    
    #display.blit(texto, (10,10))
    display.blit(texto, recText)
    #Lista de Lasers
    laser_update(laser_list)  
    for rec in laser_list:
        display.blit(lasersurf,rec)   
    pygame.display.update()
    
pygame.quit()