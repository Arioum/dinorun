def base_dino(pygame):
    dino_walk_1 = pygame.image.load(
        'graphics/dino/dino-walk-1.png').convert_alpha()
    dino_walk_2 = pygame.image.load(
        'graphics/dino/dino-walk-2.png').convert_alpha()
    dino_walk_3 = pygame.image.load(
        'graphics/dino/dino-walk-3.png').convert_alpha()
    return dino_walk_1, dino_walk_2, dino_walk_3
    # dino_jump = pygame.image.load(
    #     'graphics/dino/dino-jump.png').convert_alpha()

    # dino_walk = [dino_walk_1, dino_walk_2, dino_walk_3]
    # dino_index = 0

    # dino_surf = dino_walk[dino_index]
    # dino_rect = dino_surf.get_rect(midbottom=(100, 318))
