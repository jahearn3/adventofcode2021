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

def count_overlaps(grid, gridsize):
    count = 0
    # Count the points where 2 or more lines overlap 
    for i in range(gridsize):
        # print(grid[i])
        for j in range(gridsize):
            if(grid[i][j] >= 2):
                # print(i, j)
                count += 1
    return count

def produce_hv_lines(x1, y1, x2, y2, grid):
    # Produce the lines
    for i in range(len(x1)):
        # print(x1[i], y1[i], x2[i], y2[i])
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
    return grid 

def produce_hvd_lines(x1, y1, x2, y2, grid):
    # Produce the lines
    for i in range(len(x1)):
        # print(x1[i], y1[i], x2[i], y2[i])
        if(x1[i] == x2[i]): # vertical 
            low_y = min(y1[i], y2[i])
            high_y = max(y1[i], y2[i])
            for j in range(1 + high_y - low_y):
                grid[x1[i]][low_y + j] += 1
                # print('vertical', x1[i], low_y + j)
        elif(y1[i] == y2[i]): # horizontal
            low_x = min(x1[i], x2[i])
            high_x = max(x1[i], x2[i])
            for j in range(1 + high_x - low_x):
                grid[low_x + j][y1[i]] += 1
                # print('horizontal', low_x + j, y1[i])
        else: # diagonal
            # print('diagonal', x1[i], y1[i], x2[i], y2[i])
            # either forward slash or back slash
            low_x = min(x1[i], x2[i])
            high_x = max(x1[i], x2[i])
            low_y = min(y1[i], y2[i])
            high_y = max(y1[i], y2[i])
            # forward slash
            # e.g. 6,4 -> 2,0
            if(((x1[i] > x2[i]) and (y1[i] > y2[i])) or ((x1[i] < x2[i]) and (y1[i] < y2[i]))):
                for j in range(1 + high_x - low_x):
                    # print('forward slash', low_x + j, low_y + j)
                    grid[low_x + j][low_y + j] += 1
            # back slash
            # e.g. 8,0 -> 0,8
            else:
                for j in range(1 + high_x - low_x):
                    # print('back slash', low_x + j, high_y - j)
                    grid[low_x + j][high_y - j] += 1
    return grid


def part1(x1, y1, x2, y2, gridsize=1000):   
    grid = produce_hv_lines(x1, y1, x2, y2, np.zeros((gridsize, gridsize)))
    return count_overlaps(grid, gridsize)

def part2(x1, y1, x2, y2, gridsize=1000):   
    grid = produce_hvd_lines(x1, y1, x2, y2, np.zeros((gridsize, gridsize)))
    return count_overlaps(grid, gridsize)

data = ld.load_data('example05.txt')
data = ld.load_data('input05.txt')
x1, y1, x2, y2 = split_data(data)
print(f'{part1(x1, y1, x2, y2)}') # 7473
print(f'{part2(x1, y1, x2, y2)}') # 24164