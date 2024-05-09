import sys
import re
import pygame
from pygame import gfxdraw
import constants as c

class Leaderboard():
    def __init__(self, display):
        self.screen = display
        self.best_players = []
        self.color_RED = (255, 0, 0)
        self.color_gold = (255, 215, 0)
        self.score = 0
        self.name = ''
        self.new_player_color = self.color_RED
        with open('scores.txt', 'r') as file:
            for line in file:
                if len(line) < 2:
                    continue
                split_line = line.split()
                self.best_players.append((split_line[0], int(split_line[1])))

    def set_score(self, score):
        self.score = score

    def exit(self):
        self.best_players.append((self.name, self.score))
        self.best_players.sort(key=lambda x: -x[1])
        if len(self.best_players) > 10:
            self.best_players.pop()
        lines = []
        for name, score in self.best_players:
            lines.append(f'{name} {score}\n')
        with open('scores.txt', 'w') as file:
            file.writelines(lines)

    def change_color(self):
        if self.new_player_color == self.color_RED:
            self.new_player_color = self.color_gold
            return 'ok'
        else:
            self.exit()
            return 'exit'

    def append_to_name(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and len(self.name) > 0:
                    self.name = self.name[:-1]
                elif event.key in range(pygame.K_0, pygame.K_9 + 1) or event.key in range(pygame.K_a, pygame.K_z + 1):
                    if len(self.name) < 8:
                        self.name += pygame.key.name(event.key)

    def draw(self):
        better_than = 0
        font = pygame.font.Font('fonts/bungee-regular.ttf', 32)
        for i, line in enumerate(self.best_players):
            name, score = line
            if score < self.score:
                better_than = i
                break

            text_surface = font.render(name, True, self.color_gold)
            self.screen.blit(text_surface, (100, 100 + 40 * i))

            text_surface = font.render(str(score), True, self.color_gold)
            self.screen.blit(text_surface, (400, 100 + 40 * i))

            if not self.name:
                text_surface = font.render('_', True, self.new_player_color)
                self.screen.blit(text_surface, (100, 100 + 40 * better_than))
            else:
                text_surface = font.render(self.name, True, self.new_player_color)
                self.screen.blit(text_surface, (100, 100 + 40 * better_than))

                text_surface = font.render(str(self.score), True, self.new_player_color)
                self.screen.blit(text_surface, (400, 100 + 40 * better_than))

            for i, line in enumerate(self.best_players[better_than:]):
                name, score = line
                text_surface = font.render(name, True, self.color_gold)
                self.screen.blit(text_surface, (100, 100 + 40 * (i + better_than + 1)))

                text_surface = font.render(str(score), True, self.color_gold)
                self.screen.blit(text_surface, (400, 100 + 40 * (i + better_than + 1)))
