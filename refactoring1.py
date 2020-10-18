import pygame
from pygame.draw import *
import math as m

pygame.init()

FPS = 30

black = (0, 0, 0)
white = (255, 255, 255)
col2 = (225, 200, 0)
col1 = (169, 169, 169)
green = (0, 255, 100)
blue = (0, 200, 255)

#sky
screen = pygame.display.set_mode((500, 700))
screen.fill((blue))

#grass
surf1 = pygame.Surface((500, 300))
surf1.fill((green))
screen.blit(surf1, (0, 400))

#zabor
def Zabor(a, color):
    x1 = a + 0; y1 = 1.5*a + 140
    x2 = a + 700; y2 = 1.5*a + 400
    N = abs(a) // 5
    rect(screen, color, (x1, y1 - 2, x2 - x1, y2 - y1 + 2), 2)
    h = (x2 - x1) // (N + 1)
    for i in range(N):
        rect(screen, (255, 200, 0), (x1, y1, h, y2 - y1))
        rect(screen, (color), (x1, y1, h, y2 - y1), 1)
        x1 += h

#konura
def Konura(x, y, color, black1):
    polygon(screen, (color), ((x, y),(x + 100,y + 50),(x + 100, y + 150),(x ,y + 100)))
    polygon(screen, (black1), ((x, y),(x + 100,y + 50),(x + 100, y + 150),(x ,y + 100)), 2)

    polygon(screen, (color), ((x + 100 ,y + 50),(x + 150 ,y + 10),(x + 150, y + 110),(x + 100, y + 125)))
    polygon(screen, (black1), ((x + 100 ,y + 50),(x + 150 ,y + 10),(x + 150, y + 110),(x + 100, y + 125)), 2)

    polygon(screen, (color), ((x, y),(x + 50,y - 50),(x + 100, y + 50)))
    polygon(screen, (black1), ((x, y),(x + 50,y - 50),(x + 100, y + 50)), 2)

    polygon(screen, (color), ((x + 50, y - 50),(x + 110, y - 80),(x + 150, y + 10), (x + 100, y + 50)))
    polygon(screen, (black1), ((x + 50, y - 50),(x + 110, y - 80),(x + 150, y + 10), (x + 100, y + 50)), 2)

    hole = rect(screen, (color), (x + 25, y + 45, 45, 60))
    ellipse(screen, (black1), hole)


#tsep
def tsep (x, y, b1, gr):
    ellipse(screen, (b1), (x + 90, y - 13, 10, 20), 1)

    ellipse(screen, (b1), (x + 74, y + 2, 20, 10), 1)

    three = rect(screen, (gr), (x + 64, y + 7, 20, 10), 1)
    ellipse(screen, (b1), three, 1)

    four = rect(screen, (gr), (x + 54, y + 10, 20, 10), 1)
    ellipse(screen, (b1), four, 1)

    five = rect(screen, (gr), (x + 40, y + 7, 20, 10), 1)
    ellipse(screen, (b1), five, 1)

    six = rect(screen, (gr), (x + 30, y + 10, 20, 10), 1)
    ellipse(screen, (b1), six, 1)

    seven = rect(screen, (gr), (x + 20, y + 7, 20, 10), 1)
    ellipse(screen, (b1), seven, 1)

    eight = rect(screen, (gr), (x + 10, y + 5, 20, 10), 1)
    ellipse(screen, (b1), eight, 1)

    nine = rect(screen, (gr), (x, y, 20, 10), 1)
    ellipse(screen, (b1), nine, 1)

#Sobaka
def Sabaka2(k, c, d, color, black1, white1, a):
    b = (-1) * k
    ellipse(screen, (color), ((-1) * b + 205 + (-1) * round(120*d/a), c, round(120*d/a), round(60*d/a))) #body

    ellipse(screen, (color), ((-1) * (b + round(70/a)) + 205 + (-1) * round(90*d/a), c - round(15/a), round(90*d/a), round(50*d/a))) #butt

    ellipse(screen, (color), ((-1) * (b - round(15/a)) + 205 + (-1) * round(30*d/a), c + round(15/ a), round(30*d/a), round(80*d/a))) #leg1

    ellipse(screen, (color), ((-1) * (b + round(35/a)) + 205 + (-1) * round(30*d/a), c + round(30/a), round(30*d/a), round(80*d/a))) #leg2

    ellipse(screen, (color), ((-1) * (b - round(30/a)) + 205 + (-1) * round(40*d/a), c + round(90/a), round(40*d/a), round(15*d/a))) #foot1

    ellipse(screen, (color), ((-1) * (b + round(20/a)) + 205 + (-1) * round(40*d/a), c + round(105/a), round(40*d/a), round(15*d/a))) #foot2

    ellipse(screen, (color), ((-1) * (b + round(140/a)) + 205 + (-1) * round(35*d/a), c + round(10/a), round(35*d/a), round(40*d/a))) #thigh2

    ellipse(screen, (color), ((-1) * (b + round(75/a)) + 205 + (-1) * round(35*d/a), c - round(15/a), round(35*d/a), round(40*d/a))) #thigh1

    ellipse(screen, (color), ((-1) * (b + round(160/a)) + 205 + (-1) * round(15*d/a), c + round(30/a), round(15*d/a), round(45*d/a))) #leg4

    ellipse(screen, (color), ((-1) * (b + round(110/a)) + 205 + (-1) * round(15*d/a), c + round(20/a), round(15*d/a), round(45*d/a))) #leg3

    ellipse(screen, (color), ((-1) * (b + round(90/a)) + 205 + (-1) * round(35*d/a), c + round(60/a), round(35*d/a), round(15*d/a))) #foot3

    ellipse(screen, (color), ((-1) * (b + round(140/a)) + 205 + (-1) * round(35*d/a), c + round(70/a), round(35*d/a), round(15*d/a))) #foot4
    
    rect(screen, (color), ((-1) * (b - round(5/a)) + 205 + (-1) * round(70*d/a), c - round(30/a), round(70*d/a), round(70*d/a)))
    rect(screen, (black1), ((-1) * (b - round(5/a)) + 205 + (-1) * round(70*d/a), c - round(30/a), round(70*d/a), round(70*d/a)), m.ceil(1/a)) #hesd

    ellipse(screen, (color), ((-1) * (b - round(15/a)) + 205 + (-1) * round(15*d/a), c - round(30/a), round(15*d/a), round(20*d/a))) #ear1
    ellipse(screen, (black1), ((-1) * (b - round(15/a)) + 205 + (-1) * round(15*d/a), c - round(30/a), round(15*d/a), round(20*d/a)), m.ceil(1/a))
         
    ellipse(screen, (color), ((-1) * (b + round(60/a)) + 205 + (-1) * round(15*d/a), c - round(30/a), round(15*d/a), round(20*d/a))) #ear2
    ellipse(screen, (black1), ((-1) * (b + round(60/a)) + 205 + (-1) * round(15*d/a), c - round(30/a), round(15*d/a), round(20*d/a)), m.ceil(1/a))

    ellipse(screen, (white1), ((-1) * (b + round(11/a)) + 205 + (-1) * round(14*d/a), c - round(5/a), round(14*d/a), round(8*d/a))) #eye1
    ellipse(screen, (black1), ((-1) * (b + round(11/a)) + 205 + (-1) * round(14*d/a), c - round(5/a), round(14*d/a), round(8*d/a)), m.ceil(1/a))
    circle(screen, (black1), ((-1) * (b + round(18/a)) + 205, c - round(1/a)), round(2/a))
        
    ellipse(screen, (white1), ((-1) * (b + round(35/a)) + 205 + (-1) * round(14*d/a), c - round(5/a), round(14*d/a), round(8*d/a))) #eye2
    ellipse(screen, (black1), ((-1) * (b + round(35/a)) + 205 + (-1) * round(14*d/a), c - round(5/a), round(14*d/a), round(8*d/a)), m.ceil(1/a))
    circle(screen, (black1), ((-1) * (b + round(42/a)) + 205, c - round(1/a)), m.ceil(2/a))

    arc(screen, (black1), ((-1) * (b + round(5/a)) + 205 - round(50*d/a), c + round(20/a), round(50*d/a), round(20*d/a)), 0, m.pi , m.ceil(1/a)) #smile)=

def Sabaka1(b, c, d, color, black1, white1, a):
    ellipse(screen, (color), (b, c, round(120*d/a), round(60*d/a))) #body

    ellipse(screen, (color), (b + round(70/a), c - round(15/a), round(90*d/a), round(50*d/a))) #butt

    ellipse(screen, (color), (b - round(15/a), c + round(15/ a), round(30*d/a), round(80*d/a))) #leg1

    ellipse(screen, (color), (b + round(35/a), c + round(30/a), round(30*d/a), round(80*d/a))) #leg2

    ellipse(screen, (color), (b - round(30/a), c + round(90/a), round(40*d/a), round(15*d/a))) #foot1

    ellipse(screen, (color), (b + round(20/a), c + round(105/a), round(40*d/a), round(15*d/a))) #foot2

    ellipse(screen, (color), (b + round(140/a), c + round(10/a), round(35*d/a), round(40*d/a))) #thigh2

    ellipse(screen, (color), (b + round(75/a), c - round(15/a), round(35*d/a), round(40*d/a))) #thigh1

    ellipse(screen, (color), (b + round(160/a), c + round(30/a), round(15*d/a), round(45*d/a))) #leg4

    ellipse(screen, (color), (b + round(110/a), c + round(20/a), round(15*d/a), round(45*d/a))) #leg3

    ellipse(screen, (color), (b + round(90/a), c + round(60/a), round(35*d/a), round(15*d/a))) #foot3

    ellipse(screen, (color), (b + round(140/a), c + round(70/a), round(35*d/a), round(15*d/a))) #foot4
    
    rect(screen, (color), (b - round(5/a), c - round(30/a), round(70*d/a), round(70*d/a)))
    rect(screen, (black1), (b - round(5/a), c - round(30/a), round(70*d/a), round(70*d/a)), m.ceil(1/a)) #hesd

    ellipse(screen, (color), (b - round(15/a), c - round(30/a), round(15*d/a), round(20*d/a))) #ear1
    ellipse(screen, (black1), (b - round(15/a), c - round(30/a), round(15*d/a), round(20*d/a)), m.ceil(1/a))
         
    ellipse(screen, (color), (b + round(60/a), c - round(30/a), round(15*d/a), round(20*d/a))) #ear2
    ellipse(screen, (black1), (b + round(60/a), c - round(30/a), round(15*d/a), round(20*d/a)), m.ceil(1/a))

    ellipse(screen, (white1), (b + round(11/a), c - round(5/a), round(14*d/a), round(8*d/a))) #eye1
    ellipse(screen, (black1), (b + round(11/a), c - round(5/a), round(14*d/a), round(8*d/a)), m.ceil(1/a))
    circle(screen, (black1), (b + round(18/a), c - round(1/a)), round(2/a))
        
    ellipse(screen, (white1), (b + round(35/a), c - round(5/a), round(14*d/a), round(8*d/a))) #eye2
    ellipse(screen, (black1), (b + round(35/a), c - round(5/a), round(14*d/a), round(8*d/a)), m.ceil(1/a))
    circle(screen, (black1), (b + round(42/a), c - round(1/a)), m.ceil(2/a))

    arc(screen, (black1), (b + round(5/a), c + round(20/a), round(50*d/a), round(20*d/a)), 0, m.pi , m.ceil(1/a)) #smile)=

Zabor(-50, black)
Zabor(50, black)
Zabor(100, black)
Zabor(-200, black)
Sabaka2(290, 413, 1, col1, black, white, 1.6)
Konura(280, 425, col2, black)
tsep (250, 543, black, green)
Sabaka2(-20, 582, 1, col1, black, white, 1.1)
Sabaka1(328, 579, 1, col1, black, white, 0.4) 
Sabaka1(36, 448, 1, col1, black, white, 1.1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()




