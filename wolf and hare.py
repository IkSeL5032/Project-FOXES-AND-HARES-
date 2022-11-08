import time
import math
field = [[0 for i in range(10)] for i in range(10)]
def positionhare():
    global harexy = []
    global field
    for i in range(5):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if not([x,y] in harexy):
            harexy.append([x,y])
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
        field[yi][xi] = 0
        xi += x
        yi += y
        harexy[i][0] = xi
        harexy[i][1] = yi
        field[yi][xi] = 10
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
            vision.append([x + xj, y + yi, field[y + yi][x + xj]])
    for j in range(len(vision)):
        if vision[i][2] > 70:
            fox.append(vision[j][0],vision[j][1], sqrt((vision[j][0] - x) ** 2 + (vision[j][1] - y) ** 2))
        elif vision[i][2] < 20:
            grass.append(vision[j][0],vision[j][1], sqrt((vision[j][0] - x) ** 2 + (vision[j][1] - y) ** 2))
    for j in range(len(grass)):
        distancegrass.append(grass[j][2])
    for j in range(len(fox)):
        distancefox.append(fox[j][2])
    xg = grass[distancegrass.index(min(distancegrass))][0]
    yg = grass[distancegrass.index(min(distancegrass))][1]
            
        
