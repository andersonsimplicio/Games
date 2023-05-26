import pygame
import os,sys,time


'''
Criando a Hora Delta
'''
def update_laser(laser_list,speed=300):
    for laserRec in laser_list: 
        laserRec.y-= round(speed*dt) # type: ignore
        if laserRec.midbottom[1] < 0:
            laser_list.remove(laserRec)

def displayScore(display,font): 
    score_text = str(f'S T A R - GAME  {pygame.time.get_ticks()//1000}')
    texto = font.render(score_text, True,(255,255,225))
    recText = texto.get_rect(midleft=(30,15))
    display.blit(texto, recText)

pygame.init()
width, height = 1200, 650
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("N A S A")

#Carregando as imagens
nave = pygame.image.load(os.path.join("assets","img","ship.png")).convert_alpha()
nave = pygame.transform.scale(nave,(40,40))
lasersurf = pygame.image.load(os.path.join("assets","img","laser.png")).convert_alpha()
lasersurf =pygame.transform.scale(lasersurf,(4,40))
#Capturando o Retangulo 
navRec = nave.get_rect(center=(500,500))
#laserRec = lasersurf.get_rect(midbottom=navRec.midtop)
laser_list = []
#Carregado imagem de Fundo
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
           laserRec = lasersurf.get_rect(midbottom=navRec.midtop)
           laser_list.append(laserRec) 
        
    #Limitando os frames  (FPS)
    #dt = relogio.tick(120)/1000
    # entrada do mouse
    dt = relogio.tick(30)/1000
    navRec.center = pygame.mouse.get_pos()
    # Atualizando os Quadros

    display.fill('black')
    display.blit(bg1, bgR1)    

    #utilizando o retangulo para poscionar a nave
    display.blit(nave, navRec)
    #Desenhado o laser da nave
    update_laser(laser_list)
    for laserRec in laser_list: 
        display.blit(lasersurf,laserRec)
        
    #print(round(10*dt))
    print(laser_list)
    
    displayScore(display,font)
    #display.blit(texto, (10,10))
    #display.blit(texto, recText)
    
    pygame.display.update()
    
pygame.quit()