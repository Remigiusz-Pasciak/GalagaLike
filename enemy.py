import pygame
import constants as c
import random

from score import Score

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()

        self.anim_explosion = []
        for i in range(1, 12):
            img_explosion = pygame.image.load(f'images/boom{i:02d}.png').convert_alpha()
            img_explosion = pygame.transform.scale(img_explosion, (int(img_explosion.get_width() * 0.4), int(img_explosion.get_height() * 0.4)))
            self.anim_explosion.append(img_explosion)

        self.anim_index = 0
        self.frame_length_max = 3
        self.frame_length = self.frame_length_max
        self.image = pygame.image.load('images/meteorBig.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * 0.6), int(self.image.get_height() * 0.6)))
        self.is_destroy = False
        self.is_invincible = False
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPLAY_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.snd_hit = pygame.mixer.Sound('sounds/Hit_Hurt2.wav')
        self.bullets = pygame.sprite.Group()

        self.hp = 3

        self.point_value = 5
        self.vel_x = 0
        self.vel_y = random.randrange(3, 4)

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if self.is_destroy:
            max_index = len(self.anim_explosion) - 1
            if self.frame_length == 0:
                self.anim_index += 1
                if self.anim_index > max_index:
                    self.kill()
                else:
                    self.image = self.anim_explosion[self.anim_index]
                    self.frame_length = self.frame_length_max
            else:
                self.frame_length -= 1

    def get_hit(self):
        if not self.is_invincible:
            self.snd_hit.play()
            self.hp -= 1
            if self.hp <= 0:
                self.is_destroy = True
                self.is_invincible = True
                self.vel_x = 0
                self.vel_y = 0