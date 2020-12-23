import random
from termcolor import colored

def world_gen(rows, columns):
    grid = []
    square_gradient = []
    print_grid = []
    
    for g in range(0, rows):
        temp = []
        for u in range(0, columns):
            temp.append(int(random.randint(0, 255) * round(random.uniform(0, 1), 3)))
        grid.append(temp)
    
    i = 0
    temp = []
    while i < columns:
        temp.append(255)
        i += 1
    for k in range(0, rows):
        square_gradient.append(temp)

    squ = []
    square = []
    if len(square_gradient) % 2 == 0:
        squ.append(square_gradient[0])
        square.append(square_gradient[0])
        for x in range(1, int((len(square_gradient) / 2) + 0.5)):
            temp = squ[x - 1].copy()
            for y in range(x, (len(square_gradient[x]) - x)):
                if y == 0:
                    temp[y] = 255
                else:
                    temp[y] = int(255 * (1 / (1.5 * x)))
            squ.append(temp)
            square.append(temp)
        for z in range(1, len(squ)):
            square.append(squ[-z])
        square.append(squ[0])
    else:
        squ.append(square_gradient[0])
        square.append(square_gradient[0])
        for x in range(1, int((len(square_gradient) / 2) + 0.5)):
            temp = squ[x - 1].copy()
            for y in range(x, (len(square_gradient[x]) - x)):
                if y == 0:
                    temp[y] = 255
                else:
                    temp[y] = int(255 * (1 / (1.5 * x)))
            squ.append(temp)
            square.append(temp)
        for z in range(2, len(squ)):
            square.append(squ[-z])
        square.append(squ[0])

    new_grid = []
    for a in range(0, len(grid)):
        temp = []
        for b in range(0, len(grid[a])):
            val = ((grid[a][b]) - (square[a][b]))
            if val > 255:
                temp.append(255)
            elif val < 0:
                temp.append(0)
            else:
                temp.append(val)
        new_grid.append(temp)
        

    for c in new_grid:
        temp = []
        for d in c:
            if d < 2:
                temp.append(colored('=', 'cyan'))
            elif 2 <= d < 110:
                temp.append(colored('#', 'green'))
            elif 110 <= d < 145:
                temp.append(colored('\u2229', 'green'))
            else:
                temp.append(colored('\u039B', 'white'))
        print_grid.append(temp)

    return print_grid
