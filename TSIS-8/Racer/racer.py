import pygame , sys
import random, time
from pygame.locals import *
pygame.init()

#screen sizes
height = 600
width = 400

#making game_mode
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height ))
image = pygame.image.load("AnimatedStreet.png")
score_font = pygame.font.SysFont("Time New Roman", 35)
Scores = 0
Dcoin_font = pygame.font.SysFont("Time New Roman", 30)
Dcoins = 0

#Color
RED = (255,0,0)

#Coordinate
# x= 180
# y =500

#create player moving
class player_move(pygame.sprite.Sprite):
     def __init__(self):
          super().__init__()
          self.speed = 5
          self.image = pygame.image.load("Player.png")
          self.rect = self.image.get_rect()
          self.rect.center = (180, 500)
     def draw(self , surface):
          surface.blit(self.image, self.rect)
     def update(self):
          key = pygame.key.get_pressed()
          if key[pygame.K_UP]:
               self.rect.move_ip(0, -self.speed)
          if key[pygame.K_DOWN]:
               self.rect.move_ip(0, +self.speed)
          if key[pygame.K_LEFT]:
               self.rect.move_ip(-self.speed, 0)
          if key[pygame.K_RIGHT]:
               self.rect.move_ip(+self.speed, 0)
        

class enemy_move(pygame.sprite.Sprite):
     def __init__(self):
          super().__init__()
          self.speed = 5
          self.image = pygame.image.load("Enemy.png")
          self.rect = self.image.get_rect()
          self.rect.center = (random.randint (20, width-20) , 0)
     def draw(self , surface):
          surface.blit(self.image, self.rect)
     def update(self):
          global Scores
          self.rect.move_ip(0, +self.speed)
          if self.rect.bottom > 700:
               Scores +=1
               self.rect.top = 0
               self.rect.center = (random.randint(30,370),0)
class Dogy_coins(pygame.sprite.Sprite):
     def __init__(self):
          super().__init__()
          self.image = pygame.image.load("coin.png")
          self.rect = self.image.get_rect()
          self.rect.center = (random.randint (20, width-20) , random.randint(20, height-20))
     def draw(self , surface):
          surface.blit(self.image, self.rect)
     def update(self):
          self.rect.center = (random.randint(30, width-30), random.randint(30, height-30))

#game setting
Game = True
player = player_move()
enemy = enemy_move()
coin = Dogy_coins()

#making sprite
#________________________
#sprite for enemy
enimies = pygame.sprite.Group()
enimies.add(enemy)
#sprite for coins
coins = pygame.sprite.Group()
coins.add(coin)
#________________________

while Game:
     #quit game
     for event in pygame.event.get():
          if event.type == QUIT:
               pygame.quit()
               sys.exit()
     
     #Score counter
     score = score_font.render(f" Your Score: {Scores}", True, (0,0,0))
     Dcoin = Dcoin_font.render(f" Your Coins: {Dcoins}", True, (0,0,0))

     if pygame.sprite.spritecollideany(player, enimies):
          Game = False
     if pygame.sprite.spritecollideany(player, coins):
          Dcoins+=1
          if Dcoins %5 == 0:
               enemy.speed+=1
          coin.update()
     
     #drawing sprite
     screen.blit(image, (0, 0))
     player.draw(screen)
     enemy.draw(screen)
     coin.draw(screen)
     screen.blit(score, (0,0))
     screen.blit(Dcoin, (0,20))
     
     #updating game process
     player.update()
     enemy.update()
     pygame.display.update()

     #FPS
     clock.tick(60)














#i needed it
#all sprites
# all_sprites = pygame.sprite.Group()
# all_sprites.add(player)
# all_sprites.add(enemy)
# all_sprites.add(coin)

#for 
# screen.fill(RED)
          # pygame.display.update()
          # for entity in all_sprites:
          #      entity.kill()
          # time.sleep(2)
          # pygame.quit()
          # sys.exit()

