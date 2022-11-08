from random import randint
field = [[0 for i in range(10)] for i in range(10)]
def grass_grow(side, wait):
    global field, grass
    coordinates = [randint(0, side), randint(0, side), 1]
    if wait == 0 and coordinates not in grass:
        grass.append(coordinates)
        field[grass[-1][0]][grass[-1][1]] += 1
    if wait == 0:
        for i in range(len(grass)):
            if (grass[i][2] < 10) or (grass[i][2] - 10 < 10) or (grass[i][2] - 80 < 10):
                grass[i][2] += 1


def hare_spawn(side, amount_hare):
    global field, hare
    count = 0
    while count != amount_hare:
        coordinates = [randint(0, side), randint(0, side), 5]
        if coordinates not in hare:
            hare.append(coordinates)
            field[hare[-1][0]][hare[-1][1]] = 10
            count += 1


def wolf_spawn(side, amount_wolf):
    global field, wolf
    count = 0
    while count != amount_wolf:
        coordinates = [randint(0, side), randint(0, side), 5]
        if coordinates not in hare and coordinates not in wolf:
            wolf.append(coordinates)
            field[wolf[-1][0]][wolf[-1][1]] = 80
            count += 1
