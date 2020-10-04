import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((880, 560))

rect(screen, (255, 213, 170), (0, 0, 880, 560))
polygon(screen, (178, 68, 68), [(0, 400), (0, 298), (152, 372), (193, 314), (256, 344), (283, 271), (362, 288), (420, 330), (505, 313), (721, 315), (758, 273), (796, 295), (812, 270), (850, 273), (880, 225), (880, 400)])
circle(screen, (178, 68, 68), (656, 413), 178)
ellipse(screen, (255, 213, 170), (540, -339, 436, 657))
rect(screen, (250, 214, 195), (0, 148, 880, 112))
polygon(screen, (178, 68, 68), [(729, 345), (721, 315), (758, 273), (796, 295), (812, 270), (850, 273), (880, 225), (880, 400)])


rect(screen, (250, 214, 195), (0, 148, 880, 112))
polygon(screen, (255, 145, 34), [(5, 280), (12, 248), (140, 180), (181,138), (216, 146), (228, 163), (339, 234), (396, 226), (429, 237), (470, 200), (510, 210), (529, 192), (598, 150), (658, 130), (698, 165), (733, 157), (791, 184), (819, 169), (882, 197)])
surface = pygame.Surface([300, 200], pygame.SRCALPHA)
pygame.draw.ellipse(surface, (250, 214, 195), [-106, -292, 214, 335])
screen.blit(surface, [534, 148])
ellipse(screen, (255, 145, 34), (610, 117, 60, 96))
ellipse(screen, (255, 145, 34), (607, 121, 65, 90))
ellipse(screen, (255, 145, 34), (603, 128, 71, 68))

surface = pygame.Surface([300, 200], pygame.SRCALPHA)
pygame.draw.ellipse(surface, (250, 214, 195), [-280, -485, 489, 556])
screen.blit(surface, [12, 180])

circle(screen, (178, 68, 68), (600, 312), 62)
ellipse(screen, (178, 68, 68), (20, 246, 135, 288))
polygon(screen, (183, 131, 158), [(0, 392), (880, 373), (880, 569), (0, 560)])
ellipse(screen, (255, 255, 0), (368, 93, 100, 91))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
