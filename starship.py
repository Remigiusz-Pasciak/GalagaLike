import pygame
import constants as c
from hud import HUD
from bullet import Playerbullet


class Starship(pygame.sprite.Sprite):
    def __init__(self):
        super(Starship, self).__init__()
        self.image = pygame.image.load('images/player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*0.7, self.image.get_height()*0.7))
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH // 2
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height * 2
        self.bullets = pygame.sprite.Group()
        self.snd_shoot = pygame.mixer.Sound('sounds/Laser_Shoot_PL.wav')
        self.max_hp = 3
        self.lives = 0
        self.hp = self.max_hp
        self.snd_hit = pygame.mixer.Sound('sounds/Hit_Hurt2.wav')
        self.hud = HUD(self.hp, self.lives)
        self.is_alive = True
        self.hud_group = pygame.sprite.Group()
        self.hud_group.add(self.hud)
        self.is_invincible = False
        self.max_invincible_timer = 60
        self.invincible_timer = 0
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5
        self.hard_timer = 60
        self.upd = False

    def update(self):
        self.bullets.update()
        self.hud_group.update()
        for bullet in self.bullets:
            if bullet.rect.y <= 0:
                self.bullets.remove(bullet)
        self.rect.x += self.vel_x
        if self.rect.x < 0:
            self.rect.x = c.DISPLAY_WIDTH - self.rect.width
        elif self.rect.x > c.DISPLAY_WIDTH - self.rect.width:
            self.rect.x = 0
        self.rect.y += self.vel_y

        # Check for invincibility
        if self.invincible_timer > 0:
            self.invincible_timer -= 1
        else:
            self.is_invincible = False

        if self.hard_timer > 0:
            self.hard_timer -= 1
        elif self.hard_timer == 0:
            self.upd = True
            self.hard_timer = -1

        if self.upd:
            self.speed -= 1
            self.upd = False
            print(self.speed)

    def shoot(self):
        if self.is_alive:
            self.snd_shoot.play()
            new_bullet = Playerbullet()
            new_bullet.rect.x = self.rect.x + (self.rect.width // 2) - 2
            new_bullet.rect.y = self.rect.y
            self.bullets.add(new_bullet)

    def get_hit(self):
        if self.is_alive:
            self.hp -= 1
            self.snd_hit.play()
            self.hud.health_bar.decrease_hp_value()
            if self.hp <= 0:
                self.hp = 0
                self.death()


    def death(self):
        self.lives -= 1
        if self.lives < 0:
            self.lives = 0
            self.is_alive = False
            self.image = pygame.Surface((0, 0))
        self.hp = self.max_hp
        self.hud.health_bar.reset_health_to_max()
        self.hud.lives.decrement_life()
        self.rect.x = c.DISPLAY_WIDTH // 2
        self.is_invincible = True
        self.invincible_timer = self.max_invincible_timer



