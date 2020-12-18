from character_gen import char_gen, town_gen
from world_gen_color_island import world_gen
from termcolor import cprint
import random

people = []
time = [0, 0]

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

"""while True:"""
for z in people:
    #print(z[3], z[0], str((z[1], z[2])).replace("'", ""), z[5])
    #print()
    if z[5] not in location_count:
        location_count[z[5]] = 1
    else:
        location_count[z[5]] = location_count[z[5]] + 1

for p in location_count:
    if location_count[p] >= 25:
        if p not in town_dict:
            if grid[p[0]][p[1]] == '\x1b[32m#\x1b[0m' and grid[p[0] - 1][p[1]] != '\x1b[36m=\x1b[0m' and grid[p[0] + 1][p[1]] != '\x1b[36m=\x1b[0m' and grid[p[0]][p[1] - 1] != '\x1b[36m=\x1b[0m' and grid[p[0]][p[1] + 1] != '\x1b[36m=\x1b[0m':
                town_dict[p] = town_gen('plains')
            elif grid[p[0]][p[1]] == '\x1b[37mΛ\x1b[0m' and grid[p[0] - 1][p[1]] != '\x1b[36m=\x1b[0m' and grid[p[0] + 1][p[1]] != '\x1b[36m=\x1b[0m' and grid[p[0]][p[1] - 1] != '\x1b[36m=\x1b[0m' and grid[p[0]][p[1] + 1] != '\x1b[36m=\x1b[0m':
                town_dict[p] = town_gen('mountains')
            elif grid[p[0]][p[1]] == '\x1b[32m∩\x1b[0m' and grid[p[0] - 1][p[1]] != '\x1b[36m=\x1b[0m' and grid[p[0] + 1][p[1]] != '\x1b[36m=\x1b[0m' and grid[p[0]][p[1] - 1] != '\x1b[36m=\x1b[0m' and grid[p[0]][p[1] + 1] != '\x1b[36m=\x1b[0m':
                town_dict[p] = town_gen('hills')
            else:
                town_dict[p] = town_gen('coast')
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

grid_length = [len(str(num)) for x in grid for num in x]
width = max(grid_length)
for a in grid:
    a = ''.join(str(num).ljust(width + 2) for num in a)
    cprint(a)

if time[0] < 365:
    time[0] += 1
else:
    time[1] += 1