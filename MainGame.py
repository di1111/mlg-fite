import pygame
import sys
from pygame.locals import *
from Player import Player
from Enemy import Enemy

pygame.init()

screen = pygame.display.set_mode((640, 480))

background = pygame.image.load("images/background.png").convert_alpha();
screen.blit(background, (0, 0))

pygame.display.set_caption('Game Base')
font = pygame.font.SysFont(None, 36)

player = Player()
enemy = Enemy(500, 100)

enemy_group = pygame.sprite.Group()
enemp_group.add(enemy)

all_group = pygame.sprite.Group()
all_group.add(player)
all_group.add(enemy)


main_clock = pygame.time.Clock()

direction = -1

while True:
    # check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    
    if keys[K_a]:
        direction = 1
    elif keys[K_d]:
        direction = -1
    elif keys[K_w]:
        direction = 2
    elif keys[K_s]:
        direction = -2
    else:
        direction = 0

    main_clock.tick(60)

    collide_list = pygame.sprite.spritecollide(player, enemy_group, False, collided = None)
    if len(collide_list) > 0:
        player.subtract_lives()
        for enemy in collide_list:
            enemy.collision()

    player.update(direction)
    enemy.update()
    all_group.clear(screen, background)
    all_group.draw(screen)
    pygame.display.update()