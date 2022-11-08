import time
import math
import random
import os
field = [[0 for i in range(10)] for i in range(10)]
harexy = []
step = 0
xygrass = []
def eatgrass(i , x, y):
    global field
    field[y][x] -= 1
    harexy[i][2] += 1
def grassposition():
    global field
    global xygrass
    grass = []
    for i in range(random.randint(5,9)):
        x = random.randint(0, 9)
        y = random.randint(0,9)
        while [x,y] in xygrass:
            x = random.randint(0,9)
            y = random.randint(0,9)
        xygrass.append([x,y])
        grass.append(random.randint(1, 9))
    for i in range(len(grass)):
        field[xygrass[i][1]][xygrass[i][0]] += grass[i]
def positionhare():
    global harexy
    global field
    for i in range(2):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if not([x,y] in harexy):
            harexy.append([x,y,6])
        else:
            while [x,y] in harexy:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
    for i in range(2):
        field[harexy[i][1]][harexy[i][0]] += 10
def move(i, x, y):
    #print(i, x, y)
    global harexy
    global field
    xi = harexy[i][0]
    yi = harexy[i][1]
    #print(xi , yi)
    #time.sleep(10)
    if (xi + x <= 9 and xi + x >= 0) and (yi + y <= 9 and yi + y >= 0):
        field[yi][xi] -= 10
        xi += x
        yi += y
        harexy[i][0] = xi
        harexy[i][1] = yi
        field[yi][xi] += 10
    #time.sleep(10)
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
            fox.append([vision[j][0],vision[j][1],((vision[j][0] - x) ** 2 + (vision[j][1] - y) ** 2) ** 0.5])
        if vision[j][2]% 10 > 0:
            #print(1)
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
    #print(i)
    #print(vision)
    #print(grass)
    #print(distancegrass)
    #time.sleep(10)
def diehare(i):
    global harexy
    global field
    field[harexy[i][1]][harexy[i][0]] -= 10
    harexy.pop(i)
grassposition()
for i in range(len(field)):
    print(*field[i])
time.sleep(5)
os.system('cls')
positionhare()
for i in range(len(field)):
    print(*field[i])
time.sleep(5)
while len(harexy) > 0:
    step += 1
    time1 = time.time()
    if step % 8 == 0:
        grassposition()
    for i in range(len(harexy)):
        if harexy[i][2] == 0:
            diehare(i)
        else:
            logichare(i)
    os.system('cls')
    print(" " * 8, step)
    for i in range(len(field)):
        for j in range(len(field)):
            if len(str(field[i][j])) == 1:
                print(' ', field[i][j], end='')
            else:
                print(field[i][j], ' ', end='')
        print()
    for i in range(len(harexy)):
        print(harexy[i])
    time2 = time.time()
    time.sleep(abs(5 - (time2 - time1)))
    
    
    
    
    
        
