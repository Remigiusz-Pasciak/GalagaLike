import pygame
from starship import Starship
import constants as c
from background import BG
from enemy_spawner import EnemySpawner
from particle_spawner import ParticleSpawner
from event_handler import EventHandler
from alert_box import Alert_Box
from leaderBoard import Leaderboard

# pygame initialization
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()
pygame.font.init()

# display setup
display = pygame.display.set_mode(c.DISPLAY_SIZE)  # pygame.FULLSCREEN | pygame.HWACCEL
fps = 60
clock = pygame.time.Clock()
black = (0, 0, 0)

# object setup
event_handler = EventHandler()
bg = BG()
bg_group = pygame.sprite.Group()
bg_group.add(bg)

player = Starship()
sprite_group = pygame.sprite.Group()
sprite_group.add(player)

enemy_spawner = EnemySpawner()

particle_spawner = ParticleSpawner()

alert_box_group = pygame.sprite.Group()
leaderboard = Leaderboard(display)

# Music setup
pygame.mixer_music.load('music/Space Heroes.ogg')
pygame.mixer.music.set_volume(.1)
pygame.mixer.music.play(loops=True)

running = True

while running:
    # Tick Clock
    clock.tick(fps)

    # Handle events
    event_handler.handle_events(player)

    # Update all objects
    bg_group.update()
    sprite_group.update()
    enemy_spawner.update()
    particle_spawner.update()
    alert_box_group.update()

    # Check collision
    collided = pygame.sprite.groupcollide(player.bullets, enemy_spawner.enemy_group, True, False)
    for bullet, enemy in collided.items():
        enemy[0].get_hit()
        if enemy[0].hp == 0:
            player.hud.score.update_score(enemy[0].point_value)
        if not enemy[0].is_invincible:
            particle_spawner.spawn_particles((bullet.rect.x, bullet.rect.y))
    collided = pygame.sprite.groupcollide(sprite_group, enemy_spawner.enemy_group, False, False)
    for player, enemy in collided.items():
        if not enemy[0].is_invincible and not player.is_invincible:
            player.get_hit()
            enemy[0].hp = 0
            enemy[0].get_hit()
    for enemy in enemy_spawner.enemy_group:
        collided = pygame.sprite.groupcollide(sprite_group, enemy.bullets, False, True)
        for player, bullet in collided.items():
            if not player.is_invincible:
                player.get_hit()

    # Check for game over
    if not player.is_alive:
        enemy_spawner.clear_enemies()
        alert_box = Alert_Box()
        alert_box_group.add(alert_box)
        leaderboard.append_to_name()




    # Render the display
    display.fill(black)
    bg_group.draw(display)
    sprite_group.draw(display)
    player.bullets.draw(display)
    enemy_spawner.enemy_group.draw(display)
    for enemy in enemy_spawner.enemy_group:
        enemy.bullets.draw(display)
    particle_spawner.particle_group.draw(display)
    player.hud_group.draw(display)
    player.hud.score_group.draw(display)
    player.hud.health_bar_group.draw(display)
    player.hud.icons_group.draw(display)
    alert_box_group.draw(display)
    if not player.is_alive:
        leaderboard.append_to_name()
        leaderboard.draw()

    pygame.display.update()
