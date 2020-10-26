import pygame
from pygame.draw import *

def bird(x, y, a, color):
    polygon(screen, color, [(x, y), (x - round(31/a), y - round(15 / a)), (x - round(36/a), y - round(18 / a)), (x - round(34/a), y - round(22 / a)), (x - round(22/a), y - round(20 / a)), (x + round(2/a), y - round(10 / a)), (x + round(7/a), y - round(16 / a)), (x + round(12/a), y - round(19 / a)), (x + round(25/a), y - round(22 / a)), (x + round(42/a), y - round(21 / a))])

pygame.init()

FPS = 30
#background
screen = pygame.display.set_mode((880, 560))

#colors
orange = (255, 213, 170)
pirpl = (178, 68, 68)
orange2 = (250, 214, 195)
mount2 = (255, 145, 34)
yellow = (255, 255, 0)
BLUE = (183, 131, 158)
birdcolor = (71, 35, 35)
mount3 = (45, 0, 45)

#mountain1
rect(screen, orange, (0, 0, 880, 560))
polygon(screen, pirpl, [(0, 400), (0, 298), (152, 372), (193, 314), (256, 344), (283, 271), (362, 288), (420, 330), (505, 313), (721, 315), (758, 273), (796, 295), (812, 270), (850, 273), (880, 225), (880, 400)])
circle(screen, pirpl, (656, 413), 178)
ellipse(screen, orange, (540, -339, 436, 657))
rect(screen, (BLUE), (0, 148, 880, 112))
polygon(screen, pirpl, [(729, 345), (721, 315), (758, 273), (796, 295), (812, 270), (850, 273), (880, 225), (880, 400)])

#mountain2
rect(screen, orange2, (0, 148, 880, 112))
polygon(screen, mount2, [(5, 280), (12, 248), (140, 180), (181,138), (216, 146), (228, 163), (339, 234), (396, 226), (429, 237), (470, 200), (510, 210), (529, 192), (598, 150), (658, 130), (698, 165), (733, 157), (791, 184), (819, 169), (882, 197)])
surface = pygame.Surface([300, 200], pygame.SRCALPHA)
pygame.draw.ellipse(surface, (250, 214, 195), [-106, -292, 214, 335])
screen.blit(surface, [534, 148])
ellipse(screen, mount2, (610, 117, 60, 96))
ellipse(screen, mount2, (607, 121, 65, 90))
ellipse(screen, mount2, (603, 128, 71, 68))

surface = pygame.Surface([300, 200], pygame.SRCALPHA)
pygame.draw.ellipse(surface, (250, 214, 195), [-280, -485, 489, 556])
screen.blit(surface, [12, 180])

circle(screen, pirpl, (600, 312), 62)
ellipse(screen, pirpl, (20, 246, 135, 288))
polygon(screen, BLUE, [(0, 392), (880, 373), (880, 569), (0, 560)])
ellipse(screen, mount2, (704, 156, 57, 44))
ellipse(screen, mount2, (698, 159, 72, 42))
ellipse(screen, mount2, (716, 164, 62, 32))
ellipse(screen, mount2, (715, 167, 71, 34))
ellipse(screen, mount2, (728, 172, 67, 34))

polygon(screen, (BLUE), [(0, 392), (880, 373), (880, 569), (0, 560)]) #lake
ellipse(screen, yellow, (368, 93, 100, 91))  #sun

#mountain3
polygon(screen, mount3, [(0, 294), (106, 320), (187, 416), (254, 506), (340, 553), (415, 555), (558, 479), (597, 497), (731, 477), (757, 448), (880, 560), (0, 560)])
circle(screen, (BLUE), (343, 447), 107)
circle(screen, (BLUE), (653, 408), 105)
ellipse(screen, mount3, (716, 308, 604, 565))
polygon(screen, pirpl, [(242, 386), (329, 290), (469, 382)])
polygon(screen, pirpl, [(507, 381), (647, 277), (800, 373)])

#birds
bird(686, 461, 1, birdcolor)
bird(602, 429, 21/13, birdcolor)
bird(553, 391, 1.4, birdcolor)
bird(700, 416, 42/25, birdcolor)
bird(350, 281, 42/29, birdcolor)
bird(419, 257, 1.5, birdcolor)
bird(418, 229, 1.5, birdcolor)
bird(339, 222, 14/9, birdcolor)
bird(130, 130, 1.8, birdcolor)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
