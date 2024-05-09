import pygame
import constants as c

class Start_box(pygame.sprite.Sprite):
    def __init__(self ):
        super(Start_box, self).__init__()
        self.font = pygame.font.Font('fonts/bungee-regular.ttf', 50)
        self.color = (255, 0, 0)
        self.message = "Press l to start"
        self.image = self.font.render(self.message, 0, self.color)
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH // 2 - self.rect.width // 2
        self.rect.y = c.DISPLAY_HEIGHT // 2 - self.rect.height // 2
        self.vel_x = 0
        self.vel_y = 0


    def update(self):
        self.rect.x += self.vel_x
        self.rect.y = self.vel_y
