import pygame,os

class Laser(pygame.sprite.Sprite):
    def __init__(self,pos,groups) -> None:
        super().__init__(groups)
        self.__image = pygame.image.load(os.path.join("assets","img","laser.png")).convert_alpha()
        self.__image =pygame.transform.scale(self.__image,(4,40))
        self.image = self.__image
        self.rect = self.image.get_rect(midbottom=pos)
    
    def update(self):
