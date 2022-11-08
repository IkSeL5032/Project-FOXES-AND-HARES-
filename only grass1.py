import time
import math
import random
import os
field = [[0 for i in range(10)] for i in range(10)]
grass = []
step = 0
import pygame
import sys
from pygame.color import THECOLORS

def getTable(screen):
    for i in range(12):     
        r = pygame.Rect(0 + i*715/10, 0, 5, 720)
        pygame.draw.rect(screen, (0, 0, 0), r, 0)
        y = pygame.Rect(0 ,0+ i*715/10, 720, 5)
        pygame.draw.rect(screen, (0, 0, 0), y, 0)
        
def setPosition(table, screen):
    for j in range(10):
        for i in range(10):
            if table[j][i] % 10 <=9 and table[j][i] % 10 > 0:
                d = pygame.Rect(5+i*71.5,5 + j * 71.5, 67, 67)
                pygame.draw.rect(screen, (0,255,0), d, 0)
            
def showScreen(table):


    pygame.init()

    screen = pygame.display.set_mode((720, 720))
    screen.fill(THECOLORS['white'])
    r = pygame.Rect(50, 50, 100, 200)
    getTable(screen)
    setPosition(table, screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.flip()
        

def grassposition():
    global field
    global grass
    for i in range(10):
        for j in range(10):
            grass.append([j, i, 3])
            field[i][j] = 1

def grassgrow():
    global field
    global grass
    for i in range(10):
        for j in range(10):
            if field[i][j] == 0:
                near = 0
                if i == 9 and j == 0:
                    near += field[i][j + 1] + field[i - 1][j] + field[i - 1][j + 1]
                elif i == j == 9:
                    near += field[i - 1][j] + field[i - 1][j - 1] + field[i][j - 1]
                elif i == 9:
                    near += field[i][j + 1] + field[i][j - 1] + sum(field[i - 1][(j - 1):(j + 2)])
                elif i == j == 0:
                    near += field[i][j + 1] + field[i + 1][j] + field[i + 1][j + 1]
                elif i == 0 and j == 9:
                    near += field[i + 1][j] + field[i + 1][j - 1] + field[i][j - 1]
                elif i == 0:
                    near += field[i][j + 1] + field[i][j - 1] + sum(field[i + 1][(j - 1):(j + 2)])
                elif j == 0 and i != 9 and i != 0:
                    near += field[i + 1][j] + field[i - 1][j] + field[i - 1][j + 1] + field[i][j + 1] + field[i + 1][j + 1]
                elif j == 9 and i != 9 and i != 0:
                    near += field[i + 1][j] + field[i - 1][j] + field[i - 1][j - 1] + field[i][j - 1] + field[i + 1][j - 1]
                else:
                    near += sum(field[i - 1][(j - 1):(j + 2)]) + field[i][j - 1] + field[i][j + 1] + sum(field[i + 1][(j - 1):(j + 2)])
                if near >= 2:
                    field[i][j] = 1
                    grass.append([j, i, 3])                    

def grassdie():
    global field
    global grass
    grass1 = grass[:]
    for i in range(0, len(grass)):
        if grass[i][2] == 0:
            field[grass[i][0]][grass[i][1]] -= 1
            grass1.remove(grass[i])
        else:
            grass[i][2] -= 1
    grass = grass1[:]

grassposition()
for i in range(len(field)):
    print(*field[i])
time.sleep(5)
os.system('cls')
while True:
    grassgrow()
    if grass:
        grassdie()
    showScreen(field)
    print(" " * 8, step)
    for i in range(len(field)):
        print(*field[i])
    step += 1
    time.sleep(5)
    os.system('cls')
time2 = time.time()
time.sleep(abs(5 - (time2 - time1)))
    
    
    
    
    
        
