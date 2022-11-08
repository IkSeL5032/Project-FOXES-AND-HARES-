import time
import math
import random
import os
field = [[0 for i in range(10)] for i in range(10)]
harexy = []
step = 0
def eatgrass(i , x, y):
    global field
    field[y][x] -= 1
def grassposition():
    global field
    xygrass =[]
    grass = []
    for i in range(random.randint(7,15)):
        x = random.randint(0,9)
        y = random.randint(0,9)
        while [x,y] in xygrass:
            x = random.randint(0,9)
            y = random.randint(0,9)
        xygrass.append([x,y])
        grass.append(random.randint(1, 9))
    for i in range(len(grass)):
        field[xygrass[i][1]][xygrass[i][0]] = grass[i]
def positionhare():
    global harexy
    global field
    for i in range(7):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if not([x,y] in harexy):
            harexy.append([x,y,6])
        else:
            while [x,y] in harexy:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
    for i in range(5):
        field[harexy[i][1]][harexy[i][0]] = 10
def move(i, x, y):
    global harexy
    global field
    xi = harexy[i][0]
    yi = harexy[i][1]
    if (xi + x <= 9 and xi + x >= 0) and (yi + y <= 9 and yi + y >= 0):
        field[yi][xi] -= 10
        xi += x
        yi += y
        harexy[i][0] = xi
        harexy[i][1] = yi
        field[yi][xi] += 10
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
            if (x + xj < 10 and x + xj >= 0) and (y + yi < 10 and y + yi >= 10): 
                vision.append([x + xj, y + yi, field[y + yi][x + xj]])
    for j in range(len(vision)):
        if vision[i][2] > 70:
            fox.append([vision[j][0],vision[j][1],((vision[j][0] - x) ** 2 + (vision[j][1] - y) ** 2) ** 0.5])
        elif vision[i][2] < 20:
            grass.append([vision[j][0],vision[j][1],((vision[j][0] - x) ** 2 + (vision[j][1] - y) ** 2) ** 0.5])
    for j in range(len(grass)):
        distancegrass.append(grass[j][2])
    for j in range(len(fox)):
        distancefox.append(fox[j][2])
    if len(distancegrass) > 0:
        xg = grass[distancegrass.index(min(distancegrass))][0]
        yg = grass[distancegrass.index(min(distancegrass))][1]
        if abs(xg - x) == 0 and abs(yg - y) == 0:
            eatgrass(i,x,y)
        else:
            xmod = (xg - x) / abs(xg - x)
            ymod = (yg - y) / abs(yg - y)
            move(i, xmod , ymod)
            xyhare[i][2] -= 1
    else:
        xg = random.randint(-1,1)
        yg = random.randint(-1,1)
        if (x + xg >= 10 and x + xg < 0) and (y + yg >= 10 and y + yg < 0):
            while (x + xg >= 10 and x + xg < 0) and (y + yg >= 10 and y + yg < 0):
                xg = random.randint(-1,1)
                yg = random.randint(-1,1)
        move(i , xg , yg)
                
def diehare(i):
    global xyhare
    global field
    field[xyhare[i][1]][xyhare[i][0]] -= 10
    xyhare.pop(i)
grassposition()
positionhare()
while len(harexy) > 0:
    step += 1
    time1 = time.time()
    if step % 5 == 0:
        grassposition()
    for i in range(len(harexy)):
        if harexy[i][2] == 0:
            diehare(i)
        else:
            logichare(i)
    os.system('cls')
    print()
    for i in range(len(field)):
        print(*field[i])
    time.sleep(10)
    os.system('cls')
    time2 = time.time()
    time.sleep(1)
    
    
    
    
    
        
