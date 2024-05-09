import pygame
import constants as c


class BulletInterface:

    def update(self):
        pass


class Playerbullet(pygame.sprite.Sprite, BulletInterface):
    def __init__(self):
        super(Playerbullet, self).__init__()
        self.image = pygame.image.load('images/laserGreen.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 0.5, self.image.get_height() * 0.5))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += 0
        self.rect.y += -8


class Enemybullet(pygame.sprite.Sprite, BulletInterface):
    def __init__(self):
        super(Enemybullet, self).__init__()
        self.image = pygame.image.load('images/laserRed.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 0.5, self.image.get_height() * 0.5))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += 0
        self.rect.y += 4










