import pygame

class Enemy(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("images/enemy.png").convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.y += 5
        if self.rect.y >= 480:
            self.rect.y = 0