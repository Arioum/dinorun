import pygame
import time
from src.utils import loader
from src.screens import loading, mainmenu
from src.obstacle.base import Obstacle
from src.dino.base import Dino
from src.maps import redmarsh
from random import choice
from sys import exit


def display_score():
    current_time = pygame.time.get_ticks()//1000 - start_time
    score_surface = score_font.render(f'score: {current_time}', False, '#eeeeee')
    score_rect = score_surface.get_rect(center=(700, 40))
    screen.blit(score_surface, score_rect)
    return current_time


def collision_sprite():
    if pygame.sprite.spritecollide(dino.sprite, obstacle_group, True):
        obstacle_group.empty()
        return False
    return True


# Starts pygame game engine
pygame.init()

# Creates display window
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('DinoRun')
pygame.display.set_icon(pygame.image.load('graphics/icon.png'))
clock = pygame.time.Clock()
score_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = False
show_loading_screen = not True
start_time = 0
score = 0

# Music
bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.set_volume(0.5)
bg_music.play(loops=-1)

# Map Surface imports and rectangles
map_surf = redmarsh.map_init(pygame=pygame)

# Player and Obstacle Sprites
dino = pygame.sprite.GroupSingle()
dino.add(Dino())
obstacle_group = pygame.sprite.GroupSingle()


# Starting position of surfaces
starting_pos = redmarsh.get_starting_pos()
default_pos_X, mount_large_pos_X, mount_med_pos_X, mount_small_pos_X, cloud_back_1_pos_X, cloud_back_2_pos_X, cloud_back_3_pos_X, ground_pos_X = starting_pos

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 2000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly', 'cactus', 'cactus', 'cactus'])))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()//1000

    if game_active:
        # scenery
        # redmarsh.render_map(screen, map_surf, starting_pos)
        sky_surface, mount_large_surf, mount_med_surf, mount_small_surf, cloud_back_1_surf, cloud_back_2_surf, cloud_back_3_surf, ground_surface = map_surf
        screen.blit(sky_surface, (default_pos_X, 0))
        screen.blit(cloud_back_1_surf, (cloud_back_1_pos_X, 80))
        screen.blit(cloud_back_2_surf, (cloud_back_2_pos_X, 40))
        screen.blit(cloud_back_3_surf, (cloud_back_3_pos_X, 90))
        screen.blit(mount_large_surf, (mount_large_pos_X, 100))
        screen.blit(mount_med_surf, (mount_med_pos_X, 180))
        screen.blit(mount_small_surf, (mount_small_pos_X, 230))
        screen.blit(ground_surface, (ground_pos_X, 300))

        score = display_score()

        cloud_back_1_pos_X -= .2
        if cloud_back_1_pos_X < -240:
            cloud_back_1_pos_X = 800 + 100

        cloud_back_2_pos_X -= .2
        if cloud_back_2_pos_X < -140:
            cloud_back_2_pos_X = 800 + 200

        cloud_back_3_pos_X -= .2
        if cloud_back_3_pos_X < -140:
            cloud_back_3_pos_X = 800 + 200

        mount_large_pos_X -= .1
        if mount_large_pos_X < -800:
            mount_large_pos_X = 0

        mount_med_pos_X -= .3
        if mount_med_pos_X < -800:
            mount_med_pos_X = 0

        mount_small_pos_X -= .8
        if mount_small_pos_X < -800:
            mount_small_pos_X = 0

        ground_pos_X -= 10
        if ground_pos_X <= -800:
            ground_pos_X = 0

        dino.draw(screen)
        dino.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        game_active = collision_sprite()

    else:
        if show_loading_screen:
            show_loading_screen = loader.loader_time(time, show_loading_screen, 5)
            loading.loading(pygame, screen)
        else:
            mainmenu.main_menu(pygame, screen, score, score_font)
            select_map = 'rm'

    # Updates display surface
    pygame.display.update()
    clock.tick(60)
