import pygame
from sys import exit

# Starts pygame game engine
pygame.init()

# Creates display window
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('DinoRun')
clock = pygame.time.Clock()
score_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# Surface imports
sky_surface = pygame.image.load('graphics/sky2.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
player_surface = pygame.image.load(
    'graphics/Player/player_walk_1.png').convert_alpha()
snail_surface = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
score_surface = score_font.render('DinoRun', False, 'Black')

# Starting positions of surfaces
sky_position_X = 0

# Rectangles
player_rect = player_surface.get_rect(midbottom=(80, 300))
snail_rect = snail_surface.get_rect(midbottom=(800, 300))
score_rect = score_surface.get_rect(center=(400, 50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print('collide')

    screen.blit(sky_surface, (sky_position_X, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, 'Pink', score_rect.inflate(10, 10))
    screen.blit(score_surface, score_rect)

    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)
    pygame.draw.ellipse(screen, 'Red', pygame.Rect(50, 200, 100, 100))

    sky_position_X -= 1
    if sky_position_X < -800:
        sky_position_X = 0

    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800

    # if player_rect.colliderect(snail_rect):
    #     print('collision')

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())

    # Updates display surface
    pygame.display.update()
    clock.tick(60)
