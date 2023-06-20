from random import randint,uniform
import pygame,os

class Meteoro(pygame.sprite.Sprite):
    def __init__(self,pos,dt, groups) -> None:
        super().__init__(groups)
        self.__meteor_img = pygame.image.load(os.path.join("assets","img","meteor.png")).convert_alpha()
        self.__meteor_img = pygame.transform.scale(self.__meteor_img,(60,60))
        self.image = self.__meteor_img
        self.rect = self.image.get_rect(center=pos)
        self.pos =  pygame.math.Vector2(self.rect.topleft)
        self.direcao = pygame.math.Vector2(uniform(-0.5,0.5),1)
        self.speed = randint(400,600)
        self.dt = dt
    
    def update(self):
        self.pos += (self.direcao * self.speed)*self.dt # type: ignore   
        self.rect.topleft = (round(self.pos.x),round(self.pos.y)) # type: ignore
