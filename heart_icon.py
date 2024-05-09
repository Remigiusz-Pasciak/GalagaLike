import pygame
import constants as c

class HeartIcon(pygame.sprite.Sprite):
    def __init__(self):
        super(HeartIcon, self).__init__()
        self.image = pygame.image.load('images/life.png')

        self.rect = self.image.get_rect()
        self.vel_x = 0
        self.vel_y = 0
        self.rect.x = 20
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height - 30

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

