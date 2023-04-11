import pygame

from pygame.locals import *
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 600))
image = pygame.image.load("AnimatedStreet.png")
enemy = pygame.image.load("Enemy.png")
player = pygame.image.load("Player.png")
coin = pygame.image.load("coin.png")

x= 180
y =500
vel = 10
# class player_move():
#     key = pygame.key.get_pressed()
#     if key[pygame.K_UP]:
#         y -= vel
#         x += 0
#     if key[pygame.K_DOWN]:
#         y += vel
#         x += 0
#     if key[pygame.K_LEFT]:
#         x -= vel
#         y += 0
#     if key[pygame.K_RIGHT]:
#         x += vel
#         y += 0

class enemy_move():
    pass
class coins():
    pass


while True:

    # player_move()
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
         y -= vel
         x += 0
    if key[pygame.K_DOWN]:
         y += vel
         x += 0
    if key[pygame.K_LEFT]:
         x -= vel
         y += 0
    if key[pygame.K_RIGHT]:
         x += vel
         y += 0
    screen.blit (image,(0,0))
    screen.blit (player, (x, y))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    clock.tick(60)
    pygame.display.update()


