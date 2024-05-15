import pygame
from random import randint


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()

        if type == 'fly':
            fly_frame1 = pygame.image.load('graphics/fly/fly_start.png').convert_alpha()
            fly_frame2 = pygame.image.load('graphics/fly/fly_mid.png').convert_alpha()
            fly_frame3 = pygame.image.load('graphics/fly/fly_end.png').convert_alpha()
            self.frames = [fly_frame1, fly_frame2, fly_frame3]
            y_pos = 200
        else:
            cactus_frame = pygame.image.load('graphics/scenery/map-1/cactus-1.png').convert_alpha()
            self.frames = [cactus_frame]
            y_pos = 330

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1

        if self.animation_index >= len(self.frames):
            self.animation_index = 0

        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 10
        self.destory()

    def destory(self):
        if self.rect.x <= -100:
            self.kill()
