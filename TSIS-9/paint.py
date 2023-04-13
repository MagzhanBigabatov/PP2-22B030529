import pygame, sys

pygame.init()
width = 1000
height = 800
screen = pygame.display.set_mode((width, height))

#color 
Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)
color = White

class Objects:
    def draw(self):
        raise NotImplementedError
    def handle(self):
        raise NotImplementedError

#кнопки
class buttons:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.rect = pygame.draw.rect(screen, White, (self.x, self.y, x,y) )
    def draw(self):
        self.rect = pygame.draw.rect(screen, White, (self.x, self.y, 40, 40))

class Pen(Objects):
    def __init__(self, color, start_pos):
        self.points = []
        self.start_pos = start_pos
        self.end_pos = start_pos
        self.color = color
    def draw(self):
        for i, point in enumerate(self.points[: -1]):
            pygame.draw.line(screen, color,
            start_pos = point,
            end_pos = self.points[i + 1],
            width=5 
            )
    def handle(self, mouse_pos):
        self.points.append(mouse_pos)

class Rectangle(object):
    def __init__(self, color, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos
        self.color = color

    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])

        pygame.draw.rect(screen, self.color, 
            (
                start_pos_x,
                start_pos_y,
                end_pos_x - start_pos_x,
                end_pos_y - start_pos_y,
            ), width=5,
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos

class triangle(object):
    def __init__(self, color, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos
        self.color = color

    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])

        pygame.draw.polygon(
            screen,
            self.color,
            (
            (start_pos_x, start_pos_y),
            (start_pos_x, end_pos_y),
            (end_pos_x, end_pos_y)
            ),
            width=5,
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos

class circle(object):
    def __init__(self, color, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos
        self.color = color

    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])

        pygame.draw.circle(
            screen,
            self.color,
            [start_pos_x, start_pos_y],
            end_pos_x-start_pos_x, 
            width=5,
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos

class romb(object):
    def __init__(self, color, start_pos):
        self.start_pos = start_pos
        self.end_pos = start_pos
        self.color = color

    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])

        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])

        pygame.draw.polygon(
            screen,
            self.color,
            (
                (start_pos_x + (end_pos_x - start_pos_x) // 2, start_pos_y),
                (start_pos_x, start_pos_y + (end_pos_y - start_pos_y) // 2),
                (start_pos_x + (end_pos_x - start_pos_x) // 2, end_pos_y),
                (end_pos_x, start_pos_y + (end_pos_y - start_pos_y) // 2),
            ), 
            width=5,
        )

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos

#radius = 50
class Eraser(Objects):
    def __init__(self, color, start_pos):
        self.points = []
        self.start_pos = start_pos
        self.end_pos = start_pos
        self.color = color
        #self.radius = radius
    def draw(self):
        for i, point in enumerate(self.points[: -1]):
            pygame.draw.line(screen, Black,
            start_pos = point,
            end_pos = self.points[i + 1],
            width=60
            )
    def handle(self, mouse_pos):
        self.points.append(mouse_pos)

#paint setting (buttons, objects etc)
run = True
active = None
button = buttons(30,20)
buttonRect = buttons(90,20)
buttonTri = buttons(150,20)
buttonCir = buttons(210,20)
buttonRom = buttons(270,20)
buttonEra = buttons(930,20)
obj = [button, buttonRect, buttonTri, buttonCir, buttonRom, buttonEra]
clock = pygame.time.Clock()
current = 'pen'

while run:
    screen.fill(Black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                color = White
            if event.key == pygame.K_l:
                color = Black
            if event.key == pygame.K_r:
                color = Red
            if event.key == pygame.K_g:
                color = Green
            if event.key == pygame.K_b:
                color = Blue
            # if current == 'eraser' and event.key == pygame.K_PLUS:
            #     Eraser.width += 1
            # if current == 'eraser' and event.key == pygame.K_MINUS:
            #     Eraser.width -= 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.rect.collidepoint(pygame.mouse.get_pos()):
                current = "pen"
            if buttonRect.rect.collidepoint(pygame.mouse.get_pos()):
                current = "rectangle"
            elif buttonTri.rect.collidepoint(pygame.mouse.get_pos()):
                current = "triangle"
            elif buttonCir.rect.collidepoint(pygame.mouse.get_pos()):
                current = "circle"
            elif buttonRom.rect.collidepoint(pygame.mouse.get_pos()):
                current = "romb"
            elif buttonEra.rect.collidepoint(pygame.mouse.get_pos()):
                current = "eraser"
            else:
                if current == 'pen':
                    active = Pen(color, start_pos= event.pos)
                if current == 'rectangle':
                    active = Rectangle(color, start_pos=event.pos)
                elif current == 'triangle':
                    active = triangle(color, start_pos=event.pos)
                elif current == 'circle':
                    active = circle(color, start_pos=event.pos)
                elif current == 'romb':
                    active = romb(color, start_pos=event.pos)
                elif current == 'eraser':
                    active = Eraser(Black, start_pos=event.pos)
        
        
        if event.type == pygame.MOUSEMOTION and active is not None:
            active.handle(mouse_pos= pygame.mouse.get_pos())
            active.draw()
        if event.type == pygame.MOUSEBUTTONUP and active is not None:
                obj.append(active)
                active = None
    
    for i in obj:
        i.draw()
    
    clock.tick(60)
    pygame.display.flip()