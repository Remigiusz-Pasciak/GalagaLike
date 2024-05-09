import pygame
from enemy import Enemy
from enemy_2 import Enemy2
import constants as c
import random
import threading


class EnemySpawner:
    def __init__(self):
        self.enemy_group = pygame.sprite.Group()
        self.spawn_timer = random.randrange(30, 120)
        self.spawn_lock = threading.Lock()

    def update(self):
        self.enemy_group.update()
        for enemy in self.enemy_group:
            if enemy.rect.y >= c.DISPLAY_HEIGHT:
                self.enemy_group.remove(enemy)
        if self.spawn_timer == 0:
            self.spawn_thread()
            self.spawn_timer = random.randrange(60, 180)
        else:
            self.spawn_timer -= 1

    def spawn_thread(self):
        thread = threading.Thread(target=self.spawn_enemy)
        thread.start()

    def spawn_enemy(self):
        random_number = random.randrange(0, 100)
        if random_number <= 80:
            new_enemy = Enemy()
        elif random_number >= 81:
            new_enemy = Enemy2()
        with self.spawn_lock:
            self.enemy_group.add(new_enemy)

    def clear_enemies(self):
        for enemy in self.enemy_group:
            enemy.kill()