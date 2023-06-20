import pygame,os

class Laser(pygame.sprite.Sprite):
    def __init__(self,pos,dt,groups) -> None:
        super().__init__(groups)
        self.__image = pygame.image.load(os.path.join("assets","img","laser.png")).convert_alpha()
        self.__image =pygame.transform.scale(self.__image,(4,40))
        self.image = self.__image
        self.rect = self.image.get_rect(midbottom=pos)
        #Configurando Delta Time de disparo
        self.__dt = dt
        self.__pos = pygame.math.Vector2(self.rect.topleft)
        self.__direcao = pygame.math.Vector2(0,-1)
        self.__speed = 600

    def update(self): 
        self.__pos += (self.__direcao * self.__speed)*self.__dt # type: ignore   
        self.rect.topleft = (round(self.__pos.x),round(self.__pos.y)) # type: ignore
