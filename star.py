import pygame
import constants as c
import random


class Star(pygame.sprite.Sprite):
    def __init__(self):
        super(Star, self).__init__()
        self.WhichStar = random.randrange(1, 4)
        self.image = pygame.image.load('images/starSmall.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPLAY_WIDTH)

        self.vel_x = 0
        self.vel_y = random.randrange(5, 15)

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y




