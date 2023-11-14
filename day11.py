# Day 11: Dumbo Octopus

import load_data as ld
import numpy as np 

def flash_check(x, y, energy_grid, flash_list, flashed_list, flashing, flashes):
    if energy_grid[x][y] > 9:
        # print(f'flash at ({x}, {y})')
        if [x,y] not in flash_list and [x,y] not in flashed_list:
            flash_list.append([x, y])
            flashes += 1
            flashing = True
    return energy_grid, flash_list, flashed_list, flashing, flashes

data = ld.load_data('example11.txt')
# data = ld.load_data('input11.txt') 

size = 10
energy_grid = np.zeros((size, size))

for i, line in enumerate(data):
    for j, char in enumerate(line):
        energy_grid[i][j] = int(char)

flashes = 0
steps = 3       
for step in range(steps):
    print(f'Step {step}: {flashes} so far')
    # Increase energy level of each octopus by 1
    for i in range(size):
        for j in range(size):
            energy_grid[i][j] += 1
    # Flashes
    flashing = False
    flash_list = []
    flashed_list = []
    for i in range(size):
        for j in range(size):
            energy_grid, flash_list, flashed_list, flashing, flashes = flash_check(i, j, energy_grid, flash_list, flashed_list, flashing, flashes)
            # if(energy_grid[i][j] > 9):
            #     print(f'flash at ({i}, {j})')
            #     flash_list.append((i, j))
            #     flashing = True
            # Increase energy level of adjacent octopuses 
            # count = 0
            while(flashing): 
                print(f'flash list: {flash_list}')
                [a, b] = flash_list[0]
                print(f'a, b: {a}, {b}')
                # Row above   
                if(a > 0):
                    if(b > 0):
                        energy_grid, flash_list, flashed_list, flashing, flashes = flash_check(a - 1, b - 1, energy_grid, flash_list, flashed_list, flashing, flashes)
                    energy_grid, flash_list, flashed_list, flashing, flashes = flash_check(a - 1, b, energy_grid, flash_list, flashed_list, flashing, flashes)
                    if(b + 1 < size):
                        energy_grid, flash_list, flashed_list, flashing, flashes = flash_check(a - 1, b + 1, energy_grid, flash_list, flashed_list, flashing, flashes)
                # Same row
                if(j > 0):
                    energy_grid, flash_list, flashed_list, flashing, flashes = flash_check(a, b - 1, energy_grid, flash_list, flashed_list, flashing, flashes)
                if(j + 1 < size):
                    energy_grid, flash_list, flashed_list, flashing, flashes = flash_check(a, b + 1, energy_grid, flash_list, flashed_list, flashing, flashes)
                # Row below
                if(a + 1 < size):
                    if(b > 0):
                        energy_grid, flash_list, flashed_list, flashing, flashes = flash_check(a + 1, b - 1, energy_grid, flash_list, flashed_list, flashing, flashes)
                    energy_grid, flash_list, flashed_list, flashing, flashes = flash_check(a + 1, b, energy_grid, flash_list, flashed_list, flashing, flashes)
                    if(b + 1 < size):
                        energy_grid, flash_list, flashed_list, flashing, flashes = flash_check(a + 1, b + 1, energy_grid, flash_list, flashed_list, flashing, flashes)
                
                flashed_list = flash_list.pop(0)
                if(len(flash_list) == 0):
                    flashing = False
                # count += 1
                # if(count > 10):
                #     flashing = False
    
    # Reset energy level of flashed octopuses to 0
    for i in range(size):
        for j in range(size):
            if(energy_grid[i][j] > 9):
                energy_grid[i][j] = 0


print(flashes)