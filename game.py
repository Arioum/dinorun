import pygame
from sys import exit


def display_score():
    current_time = pygame.time.get_ticks()//1000 - start_time
    score_surface = score_font.render(
        f'score: {current_time}', False, '#eeeeee')
    score_rect = score_surface.get_rect(center=(700, 40))
    screen.blit(score_surface, score_rect)
    return current_time


def dino_animation():
    global dino_surf, dino_index

    if dino_rect.bottom < 318:
        dino_surf = dino_jump
    else:
        dino_index += 0.1
        if dino_index >= len(dino_walk):
            dino_index = 0
        dino_surf = dino_walk[int(dino_index)]


# Starts pygame game engine
pygame.init()

# Creates display window
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('DinoRun')
pygame.display.set_icon(pygame.image.load('graphics/icon.png'))
clock = pygame.time.Clock()
score_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_font = pygame.font.Font('font/Pixeltype.ttf', 80)
game_active = False
start_time = 0
score = 0

# Surface imports and rectangles

# Scenery
sky_surface = pygame.image.load('graphics/scenery/map-1/sky.png').convert()
mount_large_surf = pygame.image.load(
    'graphics/scenery/map-1/mtn-large.png').convert_alpha()
mount_med_surf = pygame.image.load(
    'graphics/scenery/map-1/mtn-medium.png').convert_alpha()
mount_small_surf = pygame.image.load(
    'graphics/scenery/map-1/mtn-small.png').convert_alpha()
cloud_back_1_surf = pygame.image.load(
    'graphics/scenery/map-1/cloud-back-1.png').convert_alpha()
cloud_back_2_surf = pygame.image.load(
    'graphics/scenery/map-1/cloud-back-2.png').convert_alpha()
cloud_back_3_surf = pygame.image.load(
    'graphics/scenery/map-1/cloud-back-3.png').convert_alpha()
ground_surface = pygame.image.load(
    'graphics/scenery/map-1/ground.png').convert_alpha()


# player and obstacles
# player
dino_walk_1 = pygame.image.load(
    'graphics/dino/dino-walk-1.png').convert_alpha()
dino_walk_2 = pygame.image.load(
    'graphics/dino/dino-walk-2.png').convert_alpha()
dino_walk_3 = pygame.image.load(
    'graphics/dino/dino-walk-3.png').convert_alpha()
dino_walk = [dino_walk_1, dino_walk_2, dino_walk_3]
dino_index = 0
dino_jump = pygame.image.load(
    'graphics/dino/dino-jump.png').convert_alpha()

dino_surf = dino_walk[dino_index]
dino_rect = dino_surf.get_rect(midbottom=(100, 318))


dino_stand = pygame.image.load(
    'graphics/scenery/map-1/dino.png').convert_alpha()
dino_stand = pygame.transform.scale2x(dino_stand)
dino_stand_rect = dino_stand.get_rect(center=(350, 200))

# Rectangles
cactus_surface = pygame.image.load(
    'graphics/scenery/map-1/cactus-1.png').convert_alpha()
cactus_rect = cactus_surface.get_rect(midbottom=(800, 330))

# pause screen
game_name = game_font.render('DinoRun', False, '#eeeeee')
game_name_rect = game_name.get_rect(center=(400, 70))
game_message = game_font.render('Press space to run', False, '#eeeeee')
game_message_rect = game_message.get_rect(center=(400, 340))

# Starting position of surfaces
default_pos_X = 0
mount_large_pos_X = 0
mount_med_pos_X = 0
mount_small_pos_X = 0
cloud_back_1_pos_X = 60
cloud_back_2_pos_X = 500
cloud_back_3_pos_X = 700
ground_pos_X = 0

# Gravity
dino_gravity = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if dino_rect.bottom == 318:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if dino_rect.collidepoint(event.pos):
                    dino_gravity = -22

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                dino_gravity = -22

        if game_active is False:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                cactus_rect.left = 800
                start_time = pygame.time.get_ticks()//1000

    if game_active:
        # scenery
        screen.blit(sky_surface, (default_pos_X, 0))
        screen.blit(cloud_back_1_surf, (cloud_back_1_pos_X, 80))
        screen.blit(cloud_back_2_surf, (cloud_back_2_pos_X, 40))
        screen.blit(cloud_back_3_surf, (cloud_back_3_pos_X, 90))
        screen.blit(mount_large_surf, (mount_large_pos_X, 100))
        screen.blit(mount_med_surf, (mount_med_pos_X, 180))
        screen.blit(mount_small_surf, (mount_small_pos_X, 230))
        screen.blit(ground_surface, (ground_pos_X, 300))

        score = display_score()
        screen.blit(cactus_surface, cactus_rect)

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

        cactus_rect.x -= 10
        if cactus_rect.right <= 0:
            cactus_rect.left = 800

        dino_gravity += 1
        dino_rect.y += dino_gravity

        if dino_rect.bottom >= 318:
            dino_rect.bottom = 318

        dino_animation()
        screen.blit(dino_surf, dino_rect)

        if cactus_rect.colliderect(dino_rect):
            game_active = False

    else:
        screen.fill("#CA3247")
        screen.blit(dino_stand, dino_stand_rect)
        score_message = score_font.render(
            f'Your score: {score}', False, "#eeeeee")
        score_message_rect = score_message.get_rect(center=(400, 330))
        screen.blit(game_name, game_name_rect)

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)

    # Updates display surface
    pygame.display.update()
    clock.tick(60)
