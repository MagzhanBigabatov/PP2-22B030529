import pygame
import sys
import random
from pygame.locals import *
import time

#screen sizes
height = 630
width = 630
#block size
block = 30

#making game_mode
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
pygame.init()

#Font for text
score_font = pygame.font.SysFont("Verdana", 30)
Scores = 0
Levels = 0

#colors
RED = (255, 0 , 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
White = (255, 255, 255)
Black = (0,0,0)

#создание координат
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#making food
class apple:
    def __init__(self):
        self.food = Point(random.randint(1,20), random.randint(1,20))
    def draw(self):
        apple = self.food
        rect = pygame.Rect(block*apple.x, block*apple.y, block, block)
        pygame.draw.rect(screen, GREEN, rect)
#making poison
class poison():
    def __init__(self):
        self.pois = Point(random.randint(1,20), random.randint(1,20))
    def draw(self):
        poisons = self.pois
        rect = pygame.Rect(block*poisons.x, block*poisons.y, block, block)
        pygame.draw.rect(screen, Black, rect)

#making and controling snake
class snake():
    def __init__(self):
        self.body = [Point(10,10)]
        self.dx = 0
        self.dy = 0
    def draw(self):
        snake = self.body[0]
        rect = pygame.Rect(block*snake.x, block*snake.y, block, block)
        pygame.draw.rect(screen, RED, rect)

        for snake in self.body[1:]:
            rect = pygame.Rect(block*snake.x, block*snake.y, block,block)
            pygame.draw.rect(screen, BLUE, rect)
    def move(self):
        #движение тела за головой
        for i in range(len(self.body)-1,0,-1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y
        
        #само движение
        self.body[0].x += self.dx
        self.body[0].y += self.dy

        #перемешение если вышел за границу
        if self.body[0].x *block > width:
            self.body[0].x = 0
        if self.body[0].y *block > height:
            self.body[0].y = 0
        if self.body[0].x < 0:
            self.body[0].x = width / block
        if self.body[0].y < 0:
            self.body[0].y = height / block 
    #взаимодействие с едой
    def collision1(self, apple):
        if apple.food.x != self.body[0].x:
            return False
        if apple.food.y != self.body[0].y:
            return False
        return True
    #взаимодействие с ядом
    def collision2(self, poison):
        global Game
        if poison.pois.x != self.body[0].x:
            return False
        if poison.pois.y != self.body[0].y :
            return False
        return True
    def cheak_wall(self):
        for i in self.body[1:]:
            if i.x == self.body[0].x and i.y == self.body[0].y:
                return True
    
class Wall:
    def __init__(self, x, y):
        self.location = Point(x,y)
    def draw(self):
        for i in range(0, height, block):
            for j in range(0, width, block):
                if i == 0 or j == 0 or i == height-block or j == width - block:
                    pygame.draw.rect(screen, Black, pygame.rect(i, j ,block, block))

#разделение на блоки
def draw_grid():
    for x in range(0, width, block):
        for y in range(0, height, block):
            rect = pygame.Rect( x, y, block, block)
            pygame.draw.rect(screen, Black, rect,1)

#game settings
snakes = snake()
food = apple()
poisons = poison()
Game = True
FPS = 5
Addfood = pygame.USEREVENT + 1
pygame.time.set_timer(Addfood, 10000)

while Game:

    screen.fill(White)
    
    score = score_font.render(f" Your Score: {Scores}", True, (0,0,0))
    level = score_font.render(f" Your Level: {Levels}", True, (0,0,0))
    fps = score_font.render(f" FPS: {FPS}", True, (0,0,0))
    
    #timer 
    ticks=pygame.time.get_ticks()
    seconds=int(ticks/1000)
    Timer = score_font.render(f" Time: {seconds}", True, (0,0,0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #меняет местоположение еды каждые 10с
        if event.type == Addfood:
            food.food.x = random.randint(1,20)
            food.food.y = random.randint(1,20)
        #проверка нажатия клавишь
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snakes.dx = 0
                snakes.dy = -1
            if event.key == pygame.K_DOWN:
                snakes.dx = 0
                snakes.dy = 1
            if event.key == pygame.K_LEFT:
                snakes.dx = -1
                snakes.dy = 0
            if event.key == pygame.K_RIGHT:
                snakes.dx = 1
                snakes.dy = 0 
    
    #прорисовка всего
    snakes.move()
    draw_grid()
    food.draw()
    poisons.draw()
    snakes.draw()
    screen.blit(score, (0,0))
    screen.blit(level, (0,30))
    screen.blit(fps, (400,0))
    screen.blit(Timer, (400,30))

    #змея может укусить себя
    if snakes.cheak_wall():
        Game = False

    #взаимодействие с едой и ядом
    if snakes.collision1(food):
        snakes.body.append(Point(food.food.x, food.food.y))
        
        food.food.x = random.randint(1,20)
        food.food.y = random.randint(1,20)
        Scores+=1
        if Scores%5==0:
            Levels +=1
            FPS+=1
        
    if snakes.collision2(poisons):
        if Scores == 0:
            pygame.quit()
            sys.exit()
        snakes.body.pop(len(snakes.body[1:]))

        poisons.pois.x = random.randint(1,20)
        poisons.pois.y = random.randint(1,20)
        Scores-=1
        
        if Scores%5>0 and Scores/Levels <= 5:
            Levels-=1
            FPS-=1
        elif Scores%5<0:
            Levels = 0
    

    pygame.display.update()
    clock.tick(FPS) 