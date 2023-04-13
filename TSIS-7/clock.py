import pygame 
import math
from datetime import datetime
from pygame.locals import *
pygame.init()

width = 830
height = 830
screen = pygame.display.set_mode((width, height))

background = pygame.image.load('mikkimouse.jpeg')
min = pygame.image.load('minute.png')
sec = pygame.image.load('second.png')

clock = pygame.time.Clock()
a1 = -48 #start angle
a2 = 60 #start angle

# clock60 = dict(zip(range(60), range(a1, (360-a1), 6)))
# clock1 = dict(zip(range(60), range(a2, (360-a2), 1 )))
# half_W = width//2
# half_H = height//2
# radius = half_H - 50
# def clock_pos(clock_dict, clock_hand):
#     x = half_W + radius* math.cos(math.radians(clock_dict[clock_hand])- math.pi/2)
#     y = half_H + radius* math.sin(math.radians(clock_dict[clock_hand])- math.pi/2)
#     return x,y

run = True
while run:
    screen.fill((255,255,255))
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # time  = datetime.now()
    # minut = time.minute 
    # secon = time.second

    minute = pygame.transform.rotate(min, a1)
    # p1 = minute.get_rect((415,412), (clock_pos(clock60, minute)))
    p1 = minute.get_rect(center = (415,412))
    screen.blit(minute, p1)
    second = pygame.transform.rotate(sec, a2)
    p2 = second.get_rect(center= (415,412))
    screen.blit(second, p2)

    a2-=1
    if a2 == 360:
        a2 = 0
        a2-=1
    if (a2-60)%360 == 0:
        a1-=6

    pygame.display.update()
    clock.tick(60)