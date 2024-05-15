class Button:
    def __init__(self, pygame, text, pos):
        self.text = text
        self.pos = pos
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (260, 40))

    def draw(self):
        pass
