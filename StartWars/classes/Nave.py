import pygame,os


class Nave(pygame.sprite.Sprite):
    def __init__(self,groups) -> None:
        super().__init__(groups)
        self.__image = pygame.image.load(os.path.join("assets","img","ship.png")).convert_alpha()
        self.__image = pygame.transform.scale(self.__image,(35,30))
        self.image = self.__image
        self.__rect = self.image.get_rect(center=(1200/2, 650/2))
        self.rect = self.__rect