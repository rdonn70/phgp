from character_gen import char_gen, town_gen
from world_gen import world_gen
from termcolor import cprint
import random
import time
#doesn't work in my IDE
"""import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'linux':
        os.system('clear')
    else:
        print('\n' * 120)"""

def person_proc(person, location_count, grid, rows, columns):
    rows -= 1
    columns -= 1
    if person[4][3] == 1 and person[4][8] == 0 and person[4][10] == 1:
        move_chance = random.randint(0, 2)
    elif person[4][3] == 1 or person[4][8] == 0 or person[4][10] == 1:
        move_chance = random.randint(1, 2)
    else:
        move_chance = random.randint(0, 5)
    if location_count[person[5]] == 1 and move_chance < 2:
        if person[5][0] >= rows and person[5][1] >= columns:
            move_dir = random.randint(0, 1)
            if move_dir == 0 and grid[rows - 1][columns] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = ((rows - 1), columns)
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
            elif move_dir == 1 and grid[rows][columns - 1] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = (rows, (columns - 1))
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
        elif person[5][0] == 0 and person[5][1] == 0 and move_chance < 2:
            move_dir = random.randint(0, 1)
            if move_dir == 0 and grid[rows + 1][columns] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = ((rows + 1), columns)
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
            elif move_dir == 1 and grid[rows][columns + 1] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = (rows, (columns + 1))
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
        elif person[5][0] >= rows and person[5][1] == 0 and move_chance < 2:
            move_dir = random.randint(0, 1)
            if move_dir == 0 and grid[rows - 1][columns] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = ((rows - 1), columns)
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
            elif move_dir == 1 and grid[rows][columns + 1] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = (rows, (columns + 1))
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
        elif person[5][0] == 0 and person[5][1] >= columns and move_chance < 2:
            move_dir = random.randint(0, 1)
            if move_dir == 0 and grid[rows + 1][columns] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = ((rows + 1), columns)
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
            elif move_dir == 1 and grid[rows][columns - 1] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = (rows, (columns - 1))
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
        elif person[5][0] >= rows and person[5][1] != 0 and person[5][1] != columns and move_chance < 2:
            move_dir = random.randint(0, 2)
            if move_dir == 0 and grid[rows - 1][columns] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = ((rows - 1), columns)
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
            elif move_dir == 1 and grid[rows][columns - 1] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = (rows, (columns - 1))
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
            elif move_dir == 2 and grid[rows][columns + 1] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = (rows, (columns + 1))
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
        elif person[5][0] != 0 and person[5][0] != rows and person[5][1] >= columns and move_chance < 2:
            move_dir = random.randint(0, 2)
            if move_dir == 0 and grid[rows - 1][columns] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = ((rows - 1), columns)
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
            elif move_dir == 1 and grid[rows + 1][columns] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = ((rows + 1), columns)
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
            elif move_dir == 2 and grid[rows][columns - 1] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = (rows, (columns - 1))
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
        elif person[5][0] != 0 and person[5][0] != rows and person[5][1] != 0 and person[5][1] != columns and move_chance < 2:
            move_dir = random.randint(0, 3)
            if move_dir == 0 and grid[rows - 1][columns] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = ((rows - 1), columns)
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
            elif move_dir == 1 and grid[rows + 1][columns] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = ((rows + 1), columns)
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
            elif move_dir == 2 and grid[rows][columns - 1] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = (rows, (columns - 1))
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
            elif move_dir == 3 and grid[rows][columns + 1] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = (rows, (columns + 1))
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
    elif 1 < location_count[person[5]] < 4 and move_chance < 2 and person[4][3] == 1:
        if person[5][0] >= rows and person[5][1] >= columns:
            move_dir = random.randint(0, 1)
            if move_dir == 0 and grid[rows - 1][columns] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = ((rows - 1), columns)
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
            elif move_dir == 1 and grid[rows][columns - 1] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = (rows, (columns - 1))
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
        elif person[5][0] == 0 and person[5][1] == 0 and move_chance < 2:
            move_dir = random.randint(0, 1)
            if move_dir == 0 and grid[rows + 1][columns] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = ((rows + 1), columns)
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
            elif move_dir == 1 and grid[rows][columns + 1] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = (rows, (columns + 1))
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
        elif person[5][0] >= rows and person[5][1] == 0 and move_chance < 2:
            move_dir = random.randint(0, 1)
            if move_dir == 0 and grid[rows - 1][columns] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = ((rows - 1), columns)
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
            elif move_dir == 1 and grid[rows][columns + 1] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = (rows, (columns + 1))
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
        elif person[5][0] == 0 and person[5][1] >= columns and move_chance < 2:
            move_dir = random.randint(0, 1)
            if move_dir == 0 and grid[rows + 1][columns] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = ((rows + 1), columns)
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
            elif move_dir == 1 and grid[rows][columns - 1] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = (rows, (columns - 1))
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
        elif person[5][0] >= rows and person[5][1] != 0 and person[5][1] != columns and move_chance < 2:
            move_dir = random.randint(0, 2)
            if move_dir == 0 and grid[rows - 1][columns] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = ((rows - 1), columns)
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
            elif move_dir == 1 and grid[rows][columns - 1] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = (rows, (columns - 1))
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
            elif move_dir == 2 and grid[rows][columns + 1] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = (rows, (columns + 1))
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
        elif person[5][0] != 0 and person[5][0] != rows and person[5][1] >= columns and move_chance < 2:
            move_dir = random.randint(0, 2)
            if move_dir == 0 and grid[rows - 1][columns] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = ((rows - 1), columns)
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
            elif move_dir == 1 and grid[rows + 1][columns] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = ((rows + 1), columns)
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
            elif move_dir == 2 and grid[rows][columns - 1] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = (rows, (columns - 1))
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
        elif person[5][0] != 0 and person[5][0] != rows and person[5][1] != 0 and person[5][1] != columns and move_chance < 2:
            move_dir = random.randint(0, 3)
            if move_dir == 0 and grid[rows - 1][columns] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = ((rows - 1), columns)
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
            elif move_dir == 1 and grid[rows + 1][columns] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = ((rows + 1), columns)
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
            elif move_dir == 2 and grid[rows][columns - 1] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = (rows, (columns - 1))
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
            elif move_dir == 3 and grid[rows][columns + 1] != '\x1b[36m=\x1b[0m':
                location_count[person[5]] -= 1
                person[5] = (rows, (columns + 1))
                try:
                    location_count[person[5]] += 1
                except:
                    location_count[person[5]] = 1
    return person, location_count

people = []
clock = [1, 1, 1]

amount_of_characters = int(input("Amount of Characters: "))
for x in range(amount_of_characters):
    people.append(char_gen())
for i in range(0, len(people)):
    people[i][1]

user_rows = int(input("Enter rows: "))
user_columns = int(input("Enter columns: "))
grid = world_gen(user_rows, user_columns)

for y in range(0, len(people)):
    while True:
        rows = random.randint(0, (user_rows - 1))
        columns = random.randint(0, (user_columns - 1))
        if grid[rows][columns] != '\x1b[36m=\x1b[0m' and grid[rows][columns] != '\x1b[37mΛ\x1b[0m':
            people[y][5] = (rows, columns)
            break
        else:
            pass

location_count = dict()
town_dict = dict()

for z in people:
    #print(z[3], z[0], str((z[1], z[2])).replace("'", ""), z[5])
    #print()
    if z[5] not in location_count:
        location_count[z[5]] = 1
    else:
        location_count[z[5]] = location_count[z[5]] + 1
while True:   
    for p in location_count:
        if location_count[p] >= 25:
            if p not in town_dict:
                if p[0] < rows and p[1] < columns and p[0] > 0 and p[1] > 0:
                    if grid[p[0]][p[1]] == '\x1b[32m#\x1b[0m' and grid[p[0] - 1][p[1]] != '\x1b[36m=\x1b[0m' and grid[p[0] + 1][p[1]] != '\x1b[36m=\x1b[0m' and grid[p[0]][p[1] - 1] != '\x1b[36m=\x1b[0m' and grid[p[0]][p[1] + 1] != '\x1b[36m=\x1b[0m':
                        town_dict[p] = town_gen(town_dict, 'plains')
                    elif grid[p[0]][p[1]] == '\x1b[37mΛ\x1b[0m' and grid[p[0] - 1][p[1]] != '\x1b[36m=\x1b[0m' and grid[p[0] + 1][p[1]] != '\x1b[36m=\x1b[0m' and grid[p[0]][p[1] - 1] != '\x1b[36m=\x1b[0m' and grid[p[0]][p[1] + 1] != '\x1b[36m=\x1b[0m':
                        town_dict[p] = town_gen(town_dict, 'mountains')
                    elif grid[p[0]][p[1]] == '\x1b[32m∩\x1b[0m' and grid[p[0] - 1][p[1]] != '\x1b[36m=\x1b[0m' and grid[p[0] + 1][p[1]] != '\x1b[36m=\x1b[0m' and grid[p[0]][p[1] - 1] != '\x1b[36m=\x1b[0m' and grid[p[0]][p[1] + 1] != '\x1b[36m=\x1b[0m':
                        town_dict[p] = town_gen(town_dict, 'hills')
                    else:
                        town_dict[p] = town_gen(town_dict, 'coast')
                else:
                    if grid[p[0]][p[1]] == '\x1b[32m#\x1b[0m':
                        town_dict[p] = town_gen(town_dict, 'plains')
                    elif grid[p[0]][p[1]] == '\x1b[37mΛ\x1b[0m':
                        town_dict[p] = town_gen(town_dict, 'mountains')
                    elif grid[p[0]][p[1]] == '\x1b[32m∩\x1b[0m':
                        town_dict[p] = town_gen(town_dict, 'hills')
                    else:
                        town_dict[p] = town_gen(town_dict, 'coast')
        #hamlet
        if 25 <= location_count[p] <= 150:
            grid[p[0]][p[1]] = '\x1b[37m×\x1b[0m'
        #village
        elif 150 < location_count[p] <= 1000:
            grid[p[0]][p[1]] = '\x1b[37mø\x1b[0m'
        #township
        elif 1000 < location_count[p] <= 10000:
            grid[p[0]][p[1]] = '\x1b[37mµ\x1b[0m'
        #town
        elif 10000 < location_count[p] <= 100000:
            grid[p[0]][p[1]] = '\x1b[37m¥\x1b[0m'
        #city
        elif 100000 < location_count[p] <= 1000000:
            grid[p[0]][p[1]] = '\x1b[37m¶\x1b[0m'
        #metropolis
        elif 1000000 < location_count[p] <= 3000000:
            grid[p[0]][p[1]] = '\x1b[37mÞ\x1b[0m'
        #megalopolis
        elif location_count[p] > 3000000:
            grid[p[0]][p[1]] = '\x1b[37mß\x1b[0m'
    
    if len(town_dict) > 0:
        for loc in town_dict:
            if location_count[loc] == 0:
                grid[loc[0]][loc[1]] = str(grid[loc[0]][loc[1]]).replace('7', '5')
            elif location_count[loc] < 25 and grid[loc[0]][loc[1]] == '\x1b[37m×\x1b[0m':
                grid[loc[0]][loc[1]] = str(grid[loc[0]][loc[1]]).replace('7', '5')
    
    """clear()"""
    #debugging
    print('\n' * 120)
    
    print("Day: {} Month: {} Year: {}".format(clock[0], clock[1], clock[2]))
    grid_length = [len(str(num)) for x in grid for num in x]
    width = max(grid_length)
    for a in grid:
        a = ''.join(str(num).ljust(width + 1) for num in a)
        cprint(a)
    
    for pers in range(0, len(people)):
        if people[pers][1][0] == clock[0] and people[pers][1][1] == clock[1]:
            people[pers][1][2] += 1

    if clock[0] == 31 and clock[1] == 12:
        clock[0] = 1
        clock[1] = 1
        clock[2] += 1
    if clock[0] == 28 and clock[1] == 2 and ((clock[2] % 4) != 0):
        clock[0] = 1
        clock[1] += 1
    elif clock[0] == 29 and clock[1] == 2 and ((clock[2] % 4) == 0):
        clock[0] = 1
        clock[1] += 1
    elif clock[0] == 30 and ((clock[1] % 2) == 0) and clock[1] <= 7:
        clock[0] = 1
        clock[1] += 1
    elif clock[0] == 31 and ((clock[1] % 2) != 0) and clock[1] <= 7:
        clock[0] = 1
        clock[1] += 1
    elif clock[0] == 30 and ((clock[1] % 2) != 0) and clock[1] > 7:
        clock[0] = 1
        clock[1] += 1
    elif clock[0] == 31 and ((clock[1] % 2) == 0) and clock[1] > 7:
        clock[0] = 1
        clock[1] += 1
    else:
        clock[0] += 1
        
    for per in range(0, len(people)):
        people[per], location_count = person_proc(people[per], location_count, grid, rows, columns)
    
    if clock[2] == 2:
        break
    time.sleep(0.5)
