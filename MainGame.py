import pygame
import sys
from pygame.locals import *
from Player import Player

pygame.init()

screen = pygame.display.set_mode((640, 480))

background = pygame.image.load("images/background.png").convert_alpha();
screen.blit(background, (0, 0))

pygame.display.set_caption('Game Base')
font = pygame.font.SysFont(None, 36)

player = Player()

all_group = pygame.sprite.Group()
all_group.add(player)

main_clock = pygame.time.Clock()

direction = -1

while True:
    # check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    main_clock.tick(60)

    player.update()
    all_group.clear(screen, background)
    all_group.draw(screen)
    pygame.display.update()