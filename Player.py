import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/player.png").convert_alpha()
        self.rect = self.image.get_rect(center=(300, 380))

    def update(self, direction): # When the function is called, it will pass the direction as a integer variable
        if direction == 1: # This if statement determines if the button pressed was [A] and moves the player left if so
            self.rect.x -= 5
        elif direction == -1: # This else if statement determines if the [D] button was pressed and moves the player right if so
            self.rect.x += 5
        elif direction == 2: # This else if statement determines if the [W] button was pressed and moves the player right if so
            self.rect.y -= 5
        elif direction == -2: # This else if statement determines if the [S] button was pressed and moves the player right if so
            self.rect.y += 5