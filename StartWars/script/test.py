import pygame
import os,sys,time
pygame.init()
width, height = 800, 650
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("TESTE -WHILE")
loop = True
while loop:
    start_time = int(round(time.time() * 1000))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                loop = False
    end_time = int(round(time.time() * 1000))
    loop_time = end_time - start_time
    print(f"Loop time: {loop_time}ms")
pygame.quit()