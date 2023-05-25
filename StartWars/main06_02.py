import pygame
import os,sys,time,random
from random import randint,uniform



'''
Criando os Meteoros Aula 06.02
'''
width, height = 1200, 650

def laser_update(laser_list,speed=300):
    for rec in laser_list:
        rec.y-=round(speed * dt)
        if rec.bottom < 0:
            laser_list.remove(rec)

def meteoro_update(meteoro_list,speed=500):
    for rec_tupla in meteoro_list:
        rec=rec_tupla[0]
        direcao = rec_tupla[1]
        
        rec.center += direcao*speed * dt
        if rec.top > height:
            meteoro_list.remove(rec_tupla)


def displayScore(display,font): 
    score_text = str(f'S T A R - GAME  {pygame.time.get_ticks()//1000}')
    texto = font.render(score_text, True,(255,255,225))
    recText = texto.get_rect(midleft=(30,15))
    display.blit(texto, recText)

#Calcula o tempo de disparo
def laser_timer(pode_disparar,duracao=300):
    if not pode_disparar:
        tempo_corrente = pygame.time.get_ticks()
        if tempo_corrente - tempo_disparo >= duracao:
            return True
    return False


pygame.init()
width, height = 1200, 650
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("N A S A")

#Carregando as imagens
nave = pygame.image.load(os.path.join("assets","img","ship.png")).convert_alpha()
nave = pygame.transform.scale(nave,(40,40))
lasersurf = pygame.image.load(os.path.join("assets","img","laser.png")).convert_alpha()
lasersurf =pygame.transform.scale(lasersurf,(4,40))
meteor_img = pygame.image.load(os.path.join("assets","img","meteor.png")).convert_alpha()
meteor_img = pygame.transform.scale(meteor_img,(60,60))
metoros_list = []

laser_list = []
#Capturando o Retangulo 
navRec = nave.get_rect(center=(500,500))
bg1 = pygame.image.load(os.path.join("assets","img","espaco.png")).convert()
bgR1 = bg1.get_rect(center=((width/2,(height/2))))
#Criando a Font do jogo
font = pygame.font.Font(os.path.join("assets","Font","Sigmar","Sigmar-Regular.ttf"),16)

pode_disparar = True #verifica se o jogador pode realizar outro dispato
tempo_disparo=0


# Criando os meteoros
meteoro_tempo = pygame.event.custom_type()
pygame.time.set_timer(meteoro_tempo, 500) # 0,5 segundos 




loop = True
relogio = pygame.time.Clock()
while loop:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            loop = False
      
        if event.type == pygame.MOUSEBUTTONDOWN and pode_disparar:
            laser_rec = lasersurf.get_rect(midbottom=navRec.midtop)
            laser_list.append(laser_rec)
            
            #calculo do tempo para um novo disparo
            pode_disparar = False
            tempo_disparo = pygame.time.get_ticks()
        
        if event.type == meteoro_tempo:
            x_pos = randint(-110, width+110)
            y_pos = randint(-100, -50)
            metoro_rec = meteor_img.get_rect(center=(x_pos,y_pos))
            # Criando uma direção para os metoros    
            direcao = pygame.math.Vector2(uniform(-0.5,0.5),1)
            metoros_list.append((metoro_rec,direcao))

    #Limitando os frames  (FPS)
    relogio.tick(120)
    #Limitando os frames  (FPS)
    dt = relogio.tick(120)/1000

    # entrada do mouse    
    navRec.center = pygame.mouse.get_pos()
    # Atualizando os Quadros
    display.fill('black')
    display.blit(bg1, bgR1)    

    #utilizando o retangulo para poscionar a nave
    display.blit(nave, navRec)
    
    #display.blit(texto, (10,10))
    displayScore(display=display,font=font)
    #Lista de Lasers
    laser_update(laser_list)  
    #tempo entre o laser
    pode_disparar = laser_timer(pode_disparar=pode_disparar,duracao=500)
    #Lista de Meteoros
    meteoro_update(meteoro_list=metoros_list)

    for rec in laser_list:
        display.blit(lasersurf,rec)  
    for rec in metoros_list:
        display.blit(meteor_img,rec[0]) 

    pygame.display.update()
    
pygame.quit()