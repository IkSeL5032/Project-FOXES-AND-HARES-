import time
import math
import random
import os
field = [[0 for i in range(10)] for i in range(10)]
grass = []
harexy = []
wolfxy = []
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
        
def setPosition(harexy, xygrass,wolfxy, screen):
        for i in range(len(xygrass)):
            x = xygrass[i][0]
            y = xygrass[i][1]
            d = pygame.Rect(5+x*71.5,5 + y * 71.5, 62, 62)
            pygame.draw.rect(screen, (0,255,0), d, 0)
        for i in range(len(harexy)):
            x = harexy[i][0]
            y = harexy[i][1]
            d = pygame.Rect(5+x*71.5,5 + y * 71.5, 62, 62)
            pygame.draw.rect(screen, (0,0,255), d, 0)
        for i in range(len(wolfxy)):
            x = wolfxy[i][0]
            y = wolfxy[i][1]
            d = pygame.Rect(5+x*71.5,5 + y * 71.5, 62, 62)
            pygame.draw.rect(screen, (255,0,0), d, 0)
        

            
            
def showScreen(harexy, xygrass, wolfxy):


    pygame.init()

    screen = pygame.display.set_mode((720, 720))
    screen.fill(THECOLORS['white'])
    r = pygame.Rect(50, 50, 100, 200)
    getTable(screen)
    setPosition(harexy, xygrass,wolfxy, screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.flip()
        


def visionwolf(i, hare):
    global field
    global wolfxy
    x, y = wolfxy[i][0], wolfxy[i][0]
    visibility = []
    for yi in range(-2,3):
        for xj in range(-2,3):
            if ((x + xj <= 9) and (x + xj >= 0)) and ((y + yi <= 9) and (y + yi >= 0)):
                visibility.append([x + xj, y + yi, field[y + yi][x + xj]])
    for j in range(len(visibility)):
        if 70 > visibility[j][2] >= 10:
            #print(1)
            hare.append([visibility[j][0],visibility[j][1],((visibility[j][0] - x) ** 2 + (visibility[j][1] - y) ** 2) ** 0.5])
    return hare

def wolfspawn():
    global field
    global wolf
    for i in range(3):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        while field[y][x] >= 10:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        field[y][x] += 70
        wolf.append([x, y, 5])

def wolfdie(i):
    global field
    global wolf
    if wolf[i][2] == 0:
        field[wolf[i][1]][wolf[i][0]] -=70
        wolf.remove(wolf[i])

def eathare(i, x, y):
    global field
    global hare
    field[y][x] -= 10
    hare.remove(hare[i])
    wolf[i][2] += 1

def logicwolf(i):
    global wolfxy
    global field
    distancehare = []
    hare = visionwolf(i)[:]
    for j in range(len(hare)):
        distancehare.append(hare[j][2])
    if len(distancehare) > 0:
        xh = hare[distancehare.index(min(distancehare))][0]
        yh = hare[distancehare.index(min(distancehare))][1]
        if abs(xh - x) == 0 and abs(yh - y) == 0:
            eathare(i,x,y)
        elif (xw - x) == 0:
            ymod = int((yh - y) / abs(yh - y))
            move(i, 0 , ymod)
            wolfxy[i][2] -= 1
        elif (yh - y) == 0:
            xmod = int((xh - x) / abs(xh - x))
            move(i, xmod, 0)
            wolfxy[i][2] -= 1
        else:
            xmod = int((xh - x) / abs(xh - x))
            ymod = int((yh - y) / abs(yh - y))
            move(i, xmod , ymod)
            wolfxy[i][2] -= 1
    else:
        xw = random.randint(-1,1)
        yw = random.randint(-1,1)
        if (x + xw >= 10 and x + xw < 0) and (y + yw >= 10 and y + yw < 0):
            while (x + xw >= 10 and x + xw < 0) and (y + yw >= 10 and y + yw < 0):
                xw = random.randint(-1,1)
                yw = random.randint(-1,1)
        move(i , xw , yw)
        wolfxy[i][2] -= 1
        


def eatgrass(i , x, y):
    global field
    global grass
    harexy[i][2] += 1
    for i in range(len(grass) - 1):
        if grass[i][0] == x and grass[i][1] == y:
            grass.pop(i)

def grassposition():
    global field
    global grass
    for i in range(10):
        for j in range(10):
            grass.append([j, i, random.randint(1 , 3)])
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
                    grass.append([j, i, random.randint(1 , 3)])

def positionhare():
    global harexy
    global field
    for i in range(20):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if not([x,y] in harexy):
            harexy.append([x,y,3])
        else:
            while [x,y] in harexy:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
def move(i, x, y):
    global harexy
    global field
    xi = harexy[i][0]
    yi = harexy[i][1]
    if (xi + x <= 9 and xi + x >= 0) and (yi + y <= 9 and yi + y >= 0):
        xi += x
        yi += y
        harexy[i][0] = xi
        harexy[i][1] = yi
def logichare(i):
    global harexy
    global field
    vision = []
    x = harexy[i][0]
    y = harexy[i][1]
    distancegrass = []
    distancefox = []
    grass = []
    fox = []
    for yi in range(-2,3):
        for xj in range(-2,3):
            if ((x + xj <= 9) and (x + xj >= 0)) and ((y + yi <= 9) and (y + yi >= 0)):
                vision.append([x + xj, y + yi, field[y + yi][x + xj]])
    for j in range(len(vision)):
        if vision[j][2] >= 70:
            fox.append([vision[j][0],vision[j][1],round(((vision[j][0] - x) ** 2 + (vision[j][1] - y) ** 2) ** 0.5)])
        if vision[j][2]% 10 > 0:
            grass.append([vision[j][0],vision[j][1],round(((vision[j][0] - x) ** 2 + (vision[j][1] - y) ** 2) ** 0.5)])
    for j in range(len(grass)):
        distancegrass.append(grass[j][2])
    for j in range(len(fox)):
        distancefox.append(fox[j][2])
    if len(distancegrass) > 0:
        mincorgrass = min(distancegrass)
    if len(distancefox) > 0:
        mincorfox = min(distancefox)
    if len(distancefox) > 0 and mincorfox < 1:
        mincor = min(distancefox)
        nb = []
        print(mincor)
        for j in range(len(distancefox)):
            if distancegrass[j] == mincor:
                nb.append(j)
        rand =nb[random.randint(1, len(nb)) - 1] 
        xg = grass[rand][0]
        yg = grass[rand][1]
        if (xg - x) == 0:
            ymod = -(int((yg - y) / abs(yg - y)))
            move(i, 0 , ymod)
            harexy[i][2] -= 1
        elif (yg - y) == 0:
            xmod = -(int((xg - x) / abs(xg - x)))
            move(i, xmod, 0)
            harexy[i][2] -= 1
        else:
            xmod = -(int((xg - x) / abs(xg - x)))
            ymod = -(int((yg - y) / abs(yg - y)))
            move(i, xmod , ymod)
            harexy[i][2] -= 1
    elif len(distancegrass) > 0:
        mincor = min(distancegrass)
        nb = []
        print(mincor)
        for j in range(len(distancegrass)):
            if distancegrass[j] == mincor:
                nb.append(j)
        rand =nb[random.randint(1, len(nb)) - 1] 
        xg = grass[rand][0]
        yg = grass[rand][1]
        if int(mincor) == 0:
            eatgrass(i,x,y)
        elif (xg - x) == 0:
            ymod = int((yg - y) / abs(yg - y))
            move(i, 0 , ymod)
            harexy[i][2] -= 1
        elif (yg - y) == 0:
            xmod = int((xg - x) / abs(xg - x))
            move(i, xmod, 0)
            harexy[i][2] -= 1
        else:
            xmod = int((xg - x) / abs(xg - x))
            ymod = int((yg - y) / abs(yg - y))
            move(i, xmod , ymod)
            harexy[i][2] -= 1
    else:
        xg = random.randint(-1,1)
        yg = random.randint(-1,1)
        if (x + xg >= 10 and x + xg < 0) and (y + yg >= 10 and y + yg < 0):
            while (x + xg >= 10 and x + xg < 0) and (y + yg >= 10 and y + yg < 0):
                xg = random.randint(-1,1)
                yg = random.randint(-1,1)
        move(i , xg , yg)
        harexy[i][2] -= 1
def grassdie():
    global field
    global grass
    grass1 = grass[:]
    for i in range(0, len(grass)):
        if grass[i][2] == 0:
            grass1.remove(grass[i])
        else:
            grass[i][2] -= 1
    grass = grass1[:]
def diehare(i):
    global harexy
    global field
    harexy.pop(i)
grassposition()
for i in range(len(field)):
    print(*field[i])
time.sleep(0.5)
os.system('cls')
positionhare()
for i in range(len(field)):
    print(*field[i])
time.sleep(0.5)
while len(harexy) > 0:
    field = [[0 for i in range(10)] for i in range(10)]
    for i in range(len(harexy)):
        field[harexy[i][1]][harexy[i][0]] += 10
    for i in range(len(grass)):
        field[grass[i][1]][grass[i][0]] += 1
    for i in range(len(wolfxy)):
        field[wolfxy[i][1]][wolfxy[i][0]] += 100
    step += 1
    time1 = time.time()
    if grass:
        grassdie()
    if step % 4 == 0:
        grassgrow()
    i = 0
    while i < len(harexy):
        if harexy[i][2] == 0:
            diehare(i)
            i -= 1
        else:
            logichare(i)
        i+=1
    os.system('cls')
    print(" " * 8, step)
    showScreen(harexy, grass, wolfxy)
    print('\n'.join('\t'.join(map(str, row)) for row in field))
    for i in range(len(harexy)):
        print(harexy[i])
    time2 = time.time()
    time.sleep(2.5)
        
