import pygame
import constants as c
import random
from bullet import Enemybullet



class Enemy2(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy2, self).__init__()

        self.img_expl_01 = pygame.image.load('images/boom01.png').convert_alpha()
        self.img_expl_01 = pygame.transform.scale(self.img_expl_01, (self.img_expl_01.get_width()*0.4,
                                                                    self.img_expl_01.get_height()*0.4))
        self.img_expl_02 = pygame.image.load('images/boom02.png').convert_alpha()
        self.img_expl_02 = pygame.transform.scale(self.img_expl_02, (self.img_expl_02.get_width() * 0.4,
                                                                     self.img_expl_02.get_height() * 0.4))
        self.img_expl_03 = pygame.image.load('images/boom03.png').convert_alpha()
        self.img_expl_03 = pygame.transform.scale(self.img_expl_03, (self.img_expl_03.get_width() * 0.4,
                                                                     self.img_expl_03.get_height() * 0.4))
        self.img_expl_04 = pygame.image.load('images/boom04.png').convert_alpha()
        self.img_expl_04 = pygame.transform.scale(self.img_expl_04, (self.img_expl_04.get_width() * 0.4,
                                                                     self.img_expl_04.get_height() * 0.4))
        self.img_expl_05 = pygame.image.load('images/boom05.png').convert_alpha()
        self.img_expl_05 = pygame.transform.scale(self.img_expl_05, (self.img_expl_05.get_width() * 0.4,
                                                                     self.img_expl_05.get_height() * 0.4))
        self.img_expl_06 = pygame.image.load('images/boom06.png').convert_alpha()
        self.img_expl_06 = pygame.transform.scale(self.img_expl_06, (self.img_expl_06.get_width() * 0.4,
                                                                     self.img_expl_06.get_height() * 0.4))
        self.img_expl_07 = pygame.image.load('images/boom07.png').convert_alpha()
        self.img_expl_07 = pygame.transform.scale(self.img_expl_07, (self.img_expl_07.get_width() * 0.4,
                                                                     self.img_expl_07.get_height() * 0.4))
        self.img_expl_08 = pygame.image.load('images/boom08.png').convert_alpha()
        self.img_expl_08 = pygame.transform.scale(self.img_expl_08, (self.img_expl_08.get_width() * 0.4,
                                                                     self.img_expl_08.get_height() * 0.4))
        self.img_expl_09 = pygame.image.load('images/boom09.png').convert_alpha()
        self.img_expl_09 = pygame.transform.scale(self.img_expl_09, (self.img_expl_09.get_width() * 0.4,
                                                                     self.img_expl_09.get_height() * 0.4))
        self.img_expl_10 = pygame.image.load('images/boom10.png').convert_alpha()
        self.img_expl_10 = pygame.transform.scale(self.img_expl_10, (self.img_expl_10.get_width() * 0.4,
                                                                     self.img_expl_10.get_height() * 0.4))
        self.img_expl_11 = pygame.image.load('images/boom11.png').convert_alpha()
        self.img_expl_11 = pygame.transform.scale(self.img_expl_11, (self.img_expl_11.get_width() * 0.4,
                                                                     self.img_expl_11.get_height() * 0.4))

        self.anim_explosion = [self.img_expl_01,
                               self.img_expl_02,
                               self.img_expl_03,
                               self.img_expl_04,
                               self.img_expl_05,
                               self.img_expl_06,
                               self.img_expl_07,
                               self.img_expl_08,
                               self.img_expl_09,
                               self.img_expl_10,
                               self.img_expl_11]
        self.anim_index = 0
        self.frame_lenght_max = 1
        self.frame_lenght = self.frame_lenght_max
        self.image = pygame.image.load('images/enemyShip.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 0.6, self.image.get_height() * 0.6))
        self.is_destroy = False
        self.is_invincible = False
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPLAY_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.snd_hit = pygame.mixer.Sound('sounds/Hit_Hurt2.wav')
        self.hp = 3
        self.randomHeight = random.randrange(200, 300)
        self.bullets = pygame.sprite.Group()
        self.bullet_timer_max = 60
        self.bullet_timer = self.bullet_timer_max
        self.states = {'FLY_DOWN': 'FLY_DOWN',
                       'ATTACK': 'ATTACK'}
        self.state = self.states['FLY_DOWN']
        self.init_state = True
        self.point_value = 5
        self.vel_x = 0
        self.vel_y = random.randrange(3, 4)

    def update(self):
        self.bullets.update()
        if self.state == 'FLY_DOWN':
            self.state_fly_down()
        elif self.state == 'ATTACK':
            self.state_attack()

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if self.is_destroy:
            max_index = len(self.anim_explosion) - 1
            if self.frame_lenght == 0:
                self.anim_index += 1
                if self.anim_index > max_index:
                    self.kill()
                else:
                    self.image = self.anim_explosion[self.anim_index]
                    self.frame_lenght = self.frame_lenght_max
            else:
                self.frame_lenght -= 1

    def state_fly_down(self):
        if self.init_state:
            self.init_state = False
        if self.rect.y >= self.randomHeight:  #add random y between 200 to 350
            self.state = self.states['ATTACK']
            self.init_state = True

    def state_attack(self):
        if self.init_state:
            self.vel_y = 0
            while self.vel_x == 0:
                self.vel_x = random.randrange(-4, 4)
            self.init_state = False
        if self.bullet_timer == 0:
            self.shoot()
            self.bullet_timer = self.bullet_timer_max
        else:
            self.bullet_timer -= 1
        if self.rect.x <= 0:
            self.vel_x *= -1
        elif self.rect.x + self.rect.width >= c.DISPLAY_WIDTH:
            self.vel_x *= -1

    def shoot(self):
        new_bullet = Enemybullet()
        new_bullet.rect.x = self.rect.x + (self.rect.width // 2)
        new_bullet.rect.y = self.rect.y + self.rect.height
        self.bullets.add(new_bullet)



    def get_hit(self):
        if not self.is_invincible:
            self.snd_hit.play()
            self.hp -= 1
            if self.hp <= 0:
                self.is_destroy = True
                self.is_invincible = True
                self.vel_x = 0
                self.vel_y = 0
            else:
                pass






