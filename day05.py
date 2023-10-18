# Day 5: Hydrothermal Venture

import load_data as ld
import numpy as np 

def split_data(data):
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    for line in data:
        start, stop = line.split('->')
        x1_, y1_ = start.split(',')
        x2_, y2_ = stop.split(',')
        x1.append(int(x1_))
        y1.append(int(y1_))
        x2.append(int(x2_))
        y2.append(int(y2_))
    return x1, y1, x2, y2

def part1(x1, y1, x2, y2):
    gridsize = 1000
    grid = np.zeros((gridsize, gridsize))
    count = 0
    # Produce the lines
    for i in range(len(x1)):
        print(x1[i], y1[i], x2[i], y2[i])
        # Only considering horizontal or vertical lines
        if(x1[i] == x2[i]): # vertical 
            low_y = min(y1[i], y2[i])
            high_y = max(y1[i], y2[i])
            for j in range(1 + high_y - low_y):
                grid[x1[i]][low_y + j] += 1
        elif(y1[i] == y2[i]): # horizontal
            low_x = min(x1[i], x2[i])
            high_x = max(x1[i], x2[i])
            for j in range(1 + high_x - low_x):
                grid[low_x + j][y1[i]] += 1
        else:
            print('Error: line is not horizontal or vertical')
            
    
    # Count the points where 2 or more lines overlap 
    for i in range(gridsize):
        print(grid[i])
        for j in range(gridsize):
            if(grid[i][j] >= 2):
                print(i, j)
                count += 1

    return count

# data = ld.load_data('example05.txt')
data = ld.load_data('input05.txt')
x1, y1, x2, y2 = split_data(data)
print(f'{part1(x1, y1, x2, y2)}') # 7473
# print(f'{part2(data)}')