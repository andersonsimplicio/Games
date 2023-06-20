import pygame,os

class Score:
    def __init__(self,font) -> None:
        self.__font = font
    
    def display(self,display):
        score_text = str(f'Start-WAR Score: {pygame.time.get_ticks()//1000}')
        texto = self.__font.render(score_text, True,(255,255,225))
        recText = texto.get_rect(midleft=(40,50))
        display.blit(texto, recText)
        pygame.draw.rect(display,(255,255,255),recText.inflate(35,35),width=2,border_radius=5)
