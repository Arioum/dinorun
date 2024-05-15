# Red Marsh - mountainous desert (Dusk)

def get_starting_pos():
    default_pos_X = 0
    mount_large_pos_X = 0
    mount_med_pos_X = 0
    mount_small_pos_X = 0
    cloud_back_1_pos_X = 60
    cloud_back_2_pos_X = 500
    cloud_back_3_pos_X = 700
    ground_pos_X = 0
    return default_pos_X, mount_large_pos_X, mount_med_pos_X, mount_small_pos_X, cloud_back_1_pos_X, cloud_back_2_pos_X, cloud_back_3_pos_X, ground_pos_X


def map_init(pygame):
    sky_surface = pygame.image.load('graphics/scenery/map-1/sky.png').convert()
    mount_large_surf = pygame.image.load('graphics/scenery/map-1/mtn-large.png').convert_alpha()
    mount_med_surf = pygame.image.load('graphics/scenery/map-1/mtn-medium.png').convert_alpha()
    mount_small_surf = pygame.image.load('graphics/scenery/map-1/mtn-small.png').convert_alpha()
    cloud_back_1_surf = pygame.image.load('graphics/scenery/map-1/cloud-back-1.png').convert_alpha()
    cloud_back_2_surf = pygame.image.load('graphics/scenery/map-1/cloud-back-2.png').convert_alpha()
    cloud_back_3_surf = pygame.image.load('graphics/scenery/map-1/cloud-back-3.png').convert_alpha()
    ground_surface = pygame.image.load('graphics/scenery/map-1/ground.png').convert_alpha()
    return sky_surface, mount_large_surf, mount_med_surf, mount_small_surf, cloud_back_1_surf, cloud_back_2_surf, cloud_back_3_surf, ground_surface


def render_map(screen, default_pos_X, mount_large_pos_X, mount_med_pos_X, mount_small_pos_X,
               cloud_back_1_pos_X, cloud_back_2_pos_X, cloud_back_3_pos_X, ground_pos_X):
    # sky_surface, mount_large_surf, mount_med_surf, mount_small_surf, cloud_back_1_surf, cloud_back_2_surf, cloud_back_3_surf, ground_surface = map_surf

    # default_pos_X, mount_large_pos_X, mount_med_pos_X, mount_small_pos_X, cloud_back_1_pos_X, cloud_back_2_pos_X, cloud_back_3_pos_X, ground_pos_X = starting_pos

    # screen.blit(sky_surface, (default_pos_X, 0))
    # screen.blit(cloud_back_1_surf, (cloud_back_1_pos_X, 80))
    # screen.blit(cloud_back_2_surf, (cloud_back_2_pos_X, 40))
    # screen.blit(cloud_back_3_surf, (cloud_back_3_pos_X, 90))
    # screen.blit(mount_large_surf, (mount_large_pos_X, 100))
    # screen.blit(mount_med_surf, (mount_med_pos_X, 180))
    # screen.blit(mount_small_surf, (mount_small_pos_X, 230))
    # screen.blit(ground_surface, (ground_pos_X, 300))

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
