import pygame
import os,sys,time,random
from random import randint,uniform


'''
Criando os Meteoros Aula 07 Colisão simples
'''
width, height = 1200, 650

#Calcula o tempo de disparo
def laser_timer(pode_disparar,duracao=500):
    if not pode_disparar:
        tempo_corrente = pygame.time.get_ticks()
        if tempo_corrente - tempo_disparo > duracao: 
            pode_disparar =True
    return pode_disparar


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
 
pygame.init()
width, height = 1200, 650
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("N A S A")

#Carregando as imagens
nave = pygame.image.load(os.path.join("assets","img","ship.png")).convert_alpha()
nave = pygame.transform.scale(nave,(40,40))

campo = pygame.image.load(os.path.join("assets","img","campo.png")).convert_alpha()
campo.set_alpha(100)
campo = pygame.transform.scale(campo,(90,80))

campo2 = pygame.image.load(os.path.join("assets","img","campo2.png")).convert_alpha()
campo2.set_alpha(100)
campo2 = pygame.transform.scale(campo2,(90,80))

campo3 = pygame.image.load(os.path.join("assets","img","campo3.png")).convert_alpha()
campo3.set_alpha(100)
campo3 = pygame.transform.scale(campo2,(110,100))


image_sprite = [campo,campo2,campo3]


lasersurf = pygame.image.load(os.path.join("assets","img","laser.png")).convert_alpha()
lasersurf =pygame.transform.scale(lasersurf,(4,40))
meteor_img = pygame.image.load(os.path.join("assets","img","meteor.png")).convert_alpha()
meteor_img = pygame.transform.scale(meteor_img,(60,60))
metoros_list = []

laser_list = []
#Capturando o Retangulo 
navRec = nave.get_rect(center=(500,500))
campoRec = campo.get_rect(center=navRec.center)

bg1 = pygame.image.load(os.path.join("assets","img","espaco.png")).convert()
bgR1 = bg1.get_rect(center=((width/2,(height/2))))
#Criando a Font do jogo
font = pygame.font.Font(os.path.join("assets","Font","Sigmar","Sigmar-Regular.ttf"),16)

pode_disparar = True #verifica se o jogador pode realizar outro dispato
tempo_disparo=pygame.time.get_ticks()


# Criando os meteoros
meteoro_tempo = pygame.event.custom_type()
pygame.time.set_timer(meteoro_tempo, 500) # 0,5 segundos 

#Criando som
try:
    laser_som = pygame.mixer.Sound(os.path.join("assets","sound","laser.ogg"))
    explosao_som = pygame.mixer.Sound(os.path.join("assets","sound","explosao.wav"))
    musica = pygame.mixer.Sound(os.path.join("assets","sound","ledzepelin.mp3"))
    musica.play(loops=-1)
except:
    print("Modulo de Som nao carregado")
    laser_som=None
    explosao_som=None
    musica=None

loop = True
relogio = pygame.time.Clock()
campo_ativo = True
life_campo = 100
list_campo = 0
while loop:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            loop = False
      
        if event.type == pygame.MOUSEBUTTONDOWN and pode_disparar:
            print(tempo_disparo)
            laser_rec = lasersurf.get_rect(midbottom=navRec.midtop)
            laser_list.append(laser_rec)
            
            #calculo do tempo para um novo disparo
            pode_disparar = False
            tempo_disparo = pygame.time.get_ticks()
            #Executa som do laser
            if laser_som is not None:
                laser_som.play()

           
        if event.type == meteoro_tempo:
            x_pos = randint(-110, width+110)
            y_pos = randint(-100, -50)
            metoro_rec = meteor_img.get_rect(center=(x_pos,y_pos))
            # Criando uma direção para os metoros    
            direcao = pygame.math.Vector2(uniform(-0.5,0.5),1)
            metoros_list.append((metoro_rec,direcao))

    #Limitando os frames  (FPS)
    relogio.tick(60)
    #Limitando os frames  (FPS)
    dt = relogio.tick(60)/1000

    # entrada do mouse    
    navRec.center = pygame.mouse.get_pos()
    #campoRec.center = pygame.mouse.get_pos()
    # Atualizando os Quadros
    display.fill('black')
    display.blit(bg1, bgR1)    

    #utilizando o retangulo para poscionar a nave
    display.blit(nave, navRec)
    
    if list_campo >= len(image_sprite):
        list_campo = 0

    image = image_sprite[list_campo]
    campoRec = image.get_rect(center=navRec.center)
    
    display.blit(image,campoRec)
    
    list_campo+=1
    #display.blit(texto, (10,10))
    displayScore(display=display,font=font)
    #Lista de Lasers e tempo entre o laser
    laser_update(laser_list)  
    pode_disparar = laser_timer(pode_disparar,duracao=500)
   
    #Lista de Meteoros
    meteoro_update(meteoro_list=metoros_list)

    #Criando colisão meteoro e a nave
    for meteoro_tupla in metoros_list:
        rec_meteoro = meteoro_tupla[0]
        if navRec.colliderect(rec_meteoro):
            if not campo_ativo:
                pygame.quit()
                sys.exit()
            else:
                life_campo-=50
                for campo in image_sprite:
                    campo.set_alpha(life_campo)

                metoros_list.remove(meteoro_tupla)
                if explosao_som is not None:
                    explosao_som.play()
                if life_campo <= 0:
                    campo_ativo =False

    for laser_ret in laser_list:
        for meteoro_tupla in metoros_list:
            if laser_ret.colliderect(meteoro_tupla[0]):
                metoros_list.remove(meteoro_tupla)
                laser_list.remove(laser_ret)
                if explosao_som is not None:
                    explosao_som.play()


    for rec in laser_list:
        display.blit(lasersurf,rec)  

    for rec in metoros_list:
        display.blit(meteor_img,rec[0]) 

    pygame.display.update()
    
pygame.quit()