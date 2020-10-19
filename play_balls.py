import pygame
import math as m
from pygame.draw import *
from random import randint
pygame.init()

FPS = 8
#coordinates of screen
x0 = 1200
y0 = 900
screen = pygame.display.set_mode((x0, y0))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
#const
point = 0
dt = 0.1
g = 10

save_results = False
file = open('result.txt','a')
name = ''

def new_ball():
    '''draw the new ball '''
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

#move ball
def go_ball(color, x, y, r):
    circle(screen, color, (x, y), r)

#move target
def go_target1(color, x, y, r):
    rect(screen, color, (x, y, 2 * r, 2 * r))
    circle(screen, BLACK, (x, y), r)
    circle(screen, BLACK, (x + 2 * r, y), r)
    circle(screen, BLACK, (x, y + 2 * r), r)
    circle(screen, BLACK, (x + 2 * r, y + 2 * r), r)

#move target2
def go_target2(color1, color2, color3, a, b, c):
    circle(screen, color1, (a, b), c)
    circle(screen, color1, (a + 2 * c, b), c)
    circle(screen, color2, (a + c - round(c/1.5), b), round(c/1.5))
    circle(screen, color2, (a + c + round(c/1.5), b), round(c/1.5))
    circle(screen, color3, (a + c - round(c/2.5), b), round(c/2.5))
    circle(screen, color3, (a + c + round(c/2.5), b), round(c/2.5))


#count points for balls
def click1(event, x, y, r):
    if m.sqrt((x - event.pos[0]) ** 2 + (y - event.pos[1]) ** 2) <= r:
        return True

#count points for targets
def click2(event, x, y, r):
    if (m.sqrt((x - event.pos[0]) ** 2 + (y - event.pos[1]) ** 2) > r) and (m.sqrt((x + 2 * r - event.pos[0]) ** 2 + (y - event.pos[1]) ** 2) > r) and (m.sqrt((x + 2 * r - event.pos[0]) ** 2 + (y + 2 * r - event.pos[1]) ** 2) > r) and (m.sqrt((x - event.pos[0]) ** 2 + (y + 2 * r - event.pos[1]) ** 2) > r) and (event.pos[0] > x) and (event.pos[0] < x + 2 * r) and (event.pos[1] > y) and (event.pos[1] < y + 2 * r):
        return True
    
#count points for targets
def click3(event, x, y, r):
    if (m.sqrt((x - event.pos[0]) ** 2 + (y - event.pos[1]) ** 2) <= r) or (m.sqrt((x + 2 * r - event.pos[0]) ** 2 + (y - event.pos[1]) ** 2) <= r):
        return True

def print_comment(comment, x, y, size):
    font = pygame.font.Font(None, size)
    text = font.render(comment, True, MAGENTA)
    screen.blit(text, [x, y])

def save_scores(final_score, name):
    if name == '':
        name = 'Player'
    file.write(name + " : " + str(final_score) + '\n')

pygame.display.update()
clock = pygame.time.Clock()
finished = False

#CREATE NEW BALLS

n1 = 7 #quantity of balls

#start coordinates of balls
x = [randint(100, x0-100) for i in range(n1)]
y = [randint(100, y0-100) for i in range(n1)]
r = [randint(10, 100) for i in range(n1)]
color1 = [COLORS[randint(0, 5)] for i in range (n1)]

for i in range (n1):
    circle(screen, color1[i], (x[i], y[i]), r[i])
    
#start speed of balls
ve1 = [[randint(-100, 100), 0] for i in range(n1)]
for i in range(n1):
    ve1[i][1] = m.sqrt(100 ** 2 - ve1[i][0] ** 2) * ((-1) ** i)

#CREATE NEW TARGET1

n2 = 1 #quantity of targets

#start coordinates of targets
a = [randint(70, x0-210) for i in range(n2)]
b = [randint(70, y0-210) for i in range(n2)]
c = [randint(10, 70) for i in range(n2)]
color2 = [COLORS[randint(0, 5)] for i in range (n2)]

for i in range (n2):
    rect(screen, color2[i], (a[i], b[i], 2 * c[i], 2 * c[i]))
    circle(screen, BLACK, (a[i], b[i]), c[i])
    circle(screen, BLACK, (a[i] + 2 * c[i], b[i]), c[i])
    circle(screen, BLACK, (a[i], b[i] + 2 * c[i]), c[i])
    circle(screen, BLACK, (a[i] + 2 * c[i], b[i] + 2 * c[i]), c[i])

#start speed of targets
ve2 = [[randint(-50, 50), 0] for i in range(n2)]
for i in range(n2):
    ve2[i][1] = m.sqrt(50 ** 2 - ve2[i][0] ** 2) * ((-1) ** i)

#CREATE NEW TARGET2

n3 = 3 #quantity of targets

#start coordinates of targets
a1 = [randint(70, x0-210) for i in range(n3)]
b1 = [randint(70, y0-210) for i in range(n3)]
c1 = [randint(40, 70) for i in range(n3)]
color31  = [COLORS[randint(0, 5)] for i in range (n3)]
color32  = [COLORS[randint(0, 5)] for i in range (n3)]
color33  = [COLORS[randint(0, 5)] for i in range (n3)]

for i in range (n3):
    circle(screen, color31[i], (a1[i], b1[i]), c1[i])
    circle(screen, color31[i], (a1[i] + 2 * c1[i], b1[i]), c1[i])
    circle(screen, color32[i], (a1[i] + c1[i] - round(c1[i]/1.5), b1[i]), round(c1[i]/1.5))
    circle(screen, color32[i], (a1[i] + c1[i] + round(c1[1]/1.5), b1[i]), round(c1[i]/1.5))
    circle(screen, color33[i], (a1[i] + c1[i] - round(c1[i]/2.5), b1[i]), round(c1[i]/2.5))
    circle(screen, color33[i], (a1[i] + c1[i] + round(c1[i]/2.5), b1[i]), round(c1[i]/2.5))

#start speed of targets
ve3 = [[randint(-50, 50), 0] for i in range(n3)]
for i in range(n3):
    ve3[i][1] = m.sqrt(50 ** 2 - ve3[i][0] ** 2) * ((-1) ** i)

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            save_results = True
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(n1):
                if click1(event, x[i], y[i], r[i]):
                    point += 1
            for i in range (n2):
                if click2(event, a[i], b[i], c[i]):
                    point += 5
            for i in range (n3):
                if click3(event, a1[i], b1[i], c1[i]):
                    point += 3
            print('Your points : ', point)
    screen.fill(BLACK)

    #make new coordinates of targets1
    for i in range (n2):
        a[i] += round(ve2[i][0] * dt)
        ve2[i][1] += g * dt
        b[i] += round(ve2[i][1] * dt)
        if b[i] > y0 - c[i] or b[i] < c[i]:
            ve2[i][1] = (-1) * ve2[i][1]
        if a[i] > x0 - c[i] or a[i] < c[i]:
            ve2[i][0] = (-1) * ve2[i][0]
        go_target1(color2[i], a[i], b[i], c[i])
        
    #make new coordinates of balls
    for i in range (n1):
        x[i] += round(ve1[i][0] * dt)
        y[i] += round(ve1[i][1] * dt)
        if y[i] > y0 - r[i] or y[i] < r[i]:
            ve1[i][1] = (-1) * ve1[i][1]
        if x[i] > x0 - r[i] or x[i] < r[i]:
            ve1[i][0] = (-1) * ve1[i][0]
        go_ball(color1[i], x[i], y[i], r[i])

    #make new coordinates of targets2
    for i in range (n3):
        a1[i] += round(ve3[i][0] * dt)
        ve3[i][1] += g * dt
        b1[i] += round(ve3[i][1] * dt)
        if b1[i] > y0 - c1[i] or b1[i] < c1[i]:
            ve3[i][1] = (-1) * ve3[i][1]
        if a1[i] > x0 - c1[i] or a1[i] < c1[i]:
            ve3[i][0] = (-1) * ve3[i][0]
        go_target2(color31[i], color32[i], color33[i], a1[i], b1[i], c1[i])

    pygame.display.update()

while save_results:
    screen.fill(BLACK)
    clock.tick(FPS)
    print_comment("Enter player's name:", 400, 300, 60)
    print_comment("Use only small letters and numbers, please", 400, 350, 30)
    print_comment("Press 'Enter' to save your result", 400, 500, 30)
    print_comment(name, 400, 400, 72)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_results = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                save_results = False
            elif (event.key < 123 and event.key > 96) or (event.key < 58 and event.key > 47):
                name += chr(event.key)
    pygame.display.update()

save_scores(point, name)
file.close()
pygame.quit()
