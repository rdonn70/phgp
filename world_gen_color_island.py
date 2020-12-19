import random
from termcolor import colored

def world_gen(rows, columns):
    grid = []
    print_grid = []
    j = 0
    while j < (rows * columns):
        grid.append(round(random.uniform(0, 1), 3))
        j += 1
    
    for e in range(0, len(grid)):
        nx = ((e % columns) / columns) - 0.5
        ny = ((e // rows) / rows) - 0.5
        d = ((2 * max(abs(nx), abs(ny))) ** 2)
        grid[e] = ((1 + grid[e] - d) / 2)

     
    for g in range(0, len(grid)):
        if(grid[g] < 0.5):
            grid[g] = (colored('=', 'cyan'))
        elif(grid[g] < 0.8):
            grid[g] = (colored('#', 'green'))
        elif(grid[g] < 0.9):
            grid[g] = (colored('\u2229', 'green'))
        else:
            grid[g] = (colored('\u039B', 'white'))        
        
    o = 0
    while(o < len(grid)):
        print_grid.append(grid[o:o+columns])
        o += columns

    return print_grid

if __name__ == "__main__":
    row_input = int(input("Enter grid rows: "))
    column_input = int(input("Enter grid columns: "))
    world_gen(row_input, column_input)
