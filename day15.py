# Day 15: Chiton

import load_data as ld
import numpy as np 
from collections import deque

data = ld.load_data('example15.txt')
# data = ld.load_data('input15.txt') 

# Set up the grid
size = len(data)
grid = np.zeros((size, size))
for i in range(size):
    for j in range(size):
        grid[i][j] = int(data[i][j])
print(f'size: {size}')

# Part 1: Find risk level of path with lowest risk

# Set up breadth-first search
start = (0,0)
end = (size-1,size-1)
risk = 0
risk_levels = []
tracker = (start, set([start]), risk) # current position and set of grid coordinates not to revisit
Q = deque([tracker]) # Using a queue for breadth-first search
vis_max = 0

while Q: # Keep searching until the queue is empty
    pos, visited, risk = Q.popleft() # Look at the front of the queue
    if(len(visited) > vis_max):
        vis_max = len(visited)
        print(f'visited: {vis_max}')
    if pos == end: # if we are at the end,
        risk += grid[-1][-1] # add to the risk level
        risk_levels.append(risk)
        continue # and go to the next element in the queue
    next_possible_steps = []
    (x, y) = pos
    # if x > 0:
    #     next_possible_steps.append((x-1, y))
    # if y > 0:
    #     next_possible_steps.append((x, y-1))
    if x < size - 1:
        next_possible_steps.append((x+1, y))
    if y < size - 1:
        next_possible_steps.append((x, y+1))
    for g in next_possible_steps: # For each next possible step
        if g not in visited: # If it is not yet visited
            new_visited = set(visited) # Get updated visited set
            new_visited.add(g) # add it to the list of visited
            (x, y) = g
            risk += grid[x][y]
            Q.append((g, new_visited, risk)) # Update the queue with the current position, visited list, and risk level

print(min(risk_levels))