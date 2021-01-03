import random
from termcolor import colored

def world_gen(rows=20, columns=20, k=0.2, i=50):
    grid = []
    for x in range(0, rows):
        grid.append([0 for y in range(0, columns)])

    if rows == columns:
        maxk = (k * rows)
    else:
        maxk = int(k * ((rows + columns) / 2))
 
    for y in range(0, i):
        p = [random.randint(0, (rows - 1)), random.randint(0, (columns - 1))]
        r = random.uniform(0, maxk)
        x2 = p[0]
        y2 = p[1]
        for g in range(0, rows):
            for h in range(0, columns):
                z = ((r ** 2) - (((x2 - g) ** 2) + ((y2 - h) ** 2)))
                if z >= 0:
                    z = 255 * (z / 10)
                    if z >= 255:
                        z = 255
                    grid[g][h] = int(z)

    print_grid = []
    for c in grid:
        temp = []
        for d in c:
            if d < 11:
                temp.append(colored('=', 'cyan'))
            elif 11 <= d < 135:
                temp.append(colored('#', 'green'))
            elif 135 <= d < 220:
                t = random.randint(0, 2)
                if t < 2:
                    temp.append(colored('\u2229', 'green'))
                else:
                    temp.append(colored('#', 'green'))
            else:
                t = random.randint(0, 2)
                if t < 2:
                    temp.append(colored('\u039B', 'white'))
                else:
                    temp.append(colored('\u2229', 'green'))
        print_grid.append(temp)
    
    return print_grid
