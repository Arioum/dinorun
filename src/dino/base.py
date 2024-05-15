import pygame


class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        dino_walk_1, dino_walk_2, dino_walk_3 = base_dino(pygame=pygame)
        self.dino_walk = [dino_walk_1, dino_walk_2, dino_walk_3]
        self.dino_index = 0
        self.dino_jump = pygame.image.load('graphics/dino/dino-jump.png').convert_alpha()

        self.image = self.dino_walk[self.dino_index]
        self.rect = self.image.get_rect(midbottom=(100, 318))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.1)

    def dino_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 318:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity

        if self.rect.bottom >= 318:
            self.rect.bottom = 318

    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.dino_jump
        else:
            self.dino_index += 0.1
            if (self.dino_index >= len(self.dino_walk)):
                self.dino_index = 0
            self.image = self.dino_walk[int(self.dino_index)]

    def update(self):
        self.dino_input()
        self.apply_gravity()
        self.animation_state()


def base_dino(pygame):
    dino_walk_1 = pygame.image.load('graphics/dino/dino-walk-1.png').convert_alpha()
    dino_walk_2 = pygame.image.load('graphics/dino/dino-walk-2.png').convert_alpha()
    dino_walk_3 = pygame.image.load('graphics/dino/dino-walk-3.png').convert_alpha()
    return dino_walk_1, dino_walk_2, dino_walk_3
