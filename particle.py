import pygame
import constants as s
import random

class Particle(pygame.sprite.Sprite):
    def __init__(self):
        super(Particle, self).__init__()
        self.width = random.randrange(1, 6)
        self.height = self.width
        self.size = (self.width, self.height)
        self.image = pygame.image.load('images/laserGreenShot.png')
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 0.2, self.image.get_height() * 0.2))
        self.rect = self.image.get_rect()
        self.kill_timer = 10
        self.vel_x = random.randrange(-10, 10)
        self.vel_y = random.randrange(-10, 10)

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if self.kill_timer == 0:
            self.kill()
        else:
            self.kill_timer -= 1