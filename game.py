import pygame
from sys import exit


def display_score():
    current_time = pygame.time.get_ticks()//1000 - start_time
    score_surface = score_font.render(
        f'score: {current_time}', False, '#eeeeee')
    score_rect = score_surface.get_rect(center=(400, 50))
    screen.blit(score_surface, score_rect)


# Starts pygame game engine
pygame.init()

# Creates display window
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('DinoRun')
clock = pygame.time.Clock()
score_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_font = pygame.font.Font('font/Pixeltype.ttf', 80)
game_active = True
start_time = 0

# Surface imports and rectangles

# Scenery
sky_surface = pygame.image.load('graphics/scenery/map-1/sky.png').convert()
mount_large_surf = pygame.image.load(
    'graphics/scenery/map-1/mtn-large.png').convert_alpha()
mount_med_surf = pygame.image.load(
    'graphics/scenery/map-1/mtn-medium.png').convert_alpha()
mount_small_surf = pygame.image.load(
    'graphics/scenery/map-1/mtn-small.png').convert_alpha()
ground_surface = pygame.image.load(
    'graphics/scenery/map-1/ground.png').convert_alpha()

# player and obstacles
# player
player_surface = pygame.image.load(
    'graphics/scenery/map-1/dino.png').convert_alpha()
player_stand = pygame.image.load(
    'graphics/scenery/map-1/dino.png').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_rect = player_surface.get_rect(midbottom=(80, 318))
player_stand_rect = player_stand.get_rect(center=(350, 200))

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
ground_pos_X = 0

# Gravity
player_gravity = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if player_rect.bottom == 318:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -22

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                player_gravity = -22

        if game_active is False:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                cactus_rect.left = 800
                start_time = pygame.time.get_ticks()//1000

    if game_active:
        # scenery
        screen.blit(sky_surface, (default_pos_X, 0))
        screen.blit(mount_large_surf, (mount_large_pos_X, 100))
        screen.blit(mount_med_surf, (mount_med_pos_X, 180))
        screen.blit(mount_small_surf, (mount_small_pos_X, 230))
        screen.blit(ground_surface, (ground_pos_X, 300))

        display_score()
        screen.blit(cactus_surface, cactus_rect)

        mount_large_pos_X -= .1
        if mount_large_pos_X < -800:
            mount_large_pos_X = 0

        mount_med_pos_X -= .3
        if mount_med_pos_X < -800:
            mount_med_pos_X = 0

        mount_small_pos_X -= .8
        if mount_small_pos_X < -800:
            mount_small_pos_X = 0

        ground_pos_X -= 5
        if ground_pos_X <= -800:
            ground_pos_X = 0

        cactus_rect.x -= 10
        if cactus_rect.right <= 0:
            cactus_rect.left = 800

        player_gravity += 1
        player_rect.y += player_gravity

        if player_rect.bottom >= 318:
            player_rect.bottom = 318

        screen.blit(player_surface, player_rect)

        if cactus_rect.colliderect(player_rect):
            game_active = False

    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_name, game_name_rect)
        screen.blit(game_message, game_message_rect)

    # Updates display surface
    pygame.display.update()
    clock.tick(60)
