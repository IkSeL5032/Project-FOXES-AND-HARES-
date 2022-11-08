import pygame
import sys
from pygame.color import THECOLORS

pygame.init()

screen = pygame.display.set_mode((720, 720))
screen.fill(THECOLORS['white'])
r = pygame.Rect(50, 50, 100, 200)
for i in range(12):     
    r = pygame.Rect(0 + i*715/10, 0, 5, 720)
    pygame.draw.rect(screen, (0, 0, 0), r, 0)
    y = pygame.Rect(0 ,0+ i*715/10, 720, 5)
    pygame.draw.rect(screen, (0, 0, 0), y, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
