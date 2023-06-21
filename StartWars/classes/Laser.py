import pygame,os

class Laser(pygame.sprite.Sprite):
    def __init__(self,pos,dt,groups) -> None:
        super().__init__(groups)
        #1 . caregando a imagem
        self.__image = pygame.image.load(os.path.join("assets","img","laser.png")).convert_alpha()
        self.__image =pygame.transform.scale(self.__image,(4,40))
        self.image = self.__image
        self.rect = self.image.get_rect(midbottom=pos)
        #2. Configurando Delta Time de disparo e velocidade
        self.__dt = dt
        self.__pos = pygame.math.Vector2(self.rect.topleft)
        self.__direcao = pygame.math.Vector2(0,-1)
        self.__speed = 600
        #3.Implementando Máscara
        self.mascara = pygame.mask.from_surface(self.image)
        #4. sons
        self.som_explosao = pygame.mixer.Sound(os.path.join("assets","sound","explosao.wav"))

    def meteoro_colisor(self,meteor_group):
        if pygame.sprite.spritecollide(self,meteor_group,True,pygame.sprite.collide_mask): # type: ignore
            self.kill()
            self.som_explosao.play()

    def update(self,meteoro_group): 
        self.__pos += (self.__direcao * self.__speed)*self.__dt # type: ignore   
        self.rect.topleft = (round(self.__pos.x),round(self.__pos.y)) # type: ignore
        self.meteoro_colisor(meteoro_group)
        if self.rect.top < 0:
            self.kill()
            