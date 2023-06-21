import pygame,os,sys
from .Laser import Laser
class Nave(pygame.sprite.Sprite):
    def __init__(self,groups) -> None:
        super().__init__(groups)
        self.__image = pygame.image.load(os.path.join("assets","img","ship.png")).convert_alpha()
        self.__image = pygame.transform.scale(self.__image,(35,30))
        self.image = self.__image
        self.__rect = self.image.get_rect(center=(1200/2, 650/2))
        self.rect = self.__rect
        # Criando um timer para o disparo
        self.__pode_disparar = True
        self.__time_tiro = None
        # Implementado mascara
        self.mascara = pygame.mask.from_surface(self.image)
        #sound
        self.som_lase = pygame.mixer.Sound(os.path.join("assets","sound","laser.ogg"))
    
    def input_position(self):
        pos = pygame.mouse.get_pos()
        self.rect.center = pos
    
    def laser_time(self):
        if not self.__pode_disparar:
            t_atual = pygame.time.get_ticks()
            if self.__time_tiro is not None:
                if t_atual - self.__time_tiro >= 500:
                        self.__pode_disparar=True

    def disparo_laser(self,dt,laser_group):
        if pygame.mouse.get_pressed()[0] and self.__pode_disparar:
            self.__pode_disparar = False
            self.__time_tiro = pygame.time.get_ticks()
            Laser(self.rect.midtop,dt,laser_group)
            self.som_lase.play()
    
    def meteoro_colisor(self,meteor_group):
        if pygame.sprite.spritecollide(self,meteor_group,False,pygame.sprite.collide_mask): # type: ignore
            pygame.quit()
            sys.exit()

    def update(self,dt,laser_group,meteoro_group):
        self.laser_time()
        self.disparo_laser(dt,laser_group)
        self.input_position()
        self.meteoro_colisor(meteoro_group)
       

