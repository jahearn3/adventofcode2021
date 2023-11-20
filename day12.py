# Day 12: Passage Pathing

import load_data as ld
from collections import deque

def adjacency_list(data):
    # Build dict of paths (adjacency list)
    paths_dict = {'start': [], 'end': []}
    for line in data:
        a, b = line.split('-')
        
        if a in paths_dict:
            val_list = paths_dict[a]
            if b not in val_list:
                val_list.append(b)
                paths_dict[a] = val_list
        else:
            paths_dict[a] = [b]
        if b in paths_dict:
            val_list = paths_dict[b]
            if a not in val_list:
                val_list.append(a)
                paths_dict[b] = val_list
        else:
            paths_dict[b] = [a]
    return paths_dict

# Solutions based on Jonathan Paulson's solutions            
def part_1(paths_dict):
    # Part 1: Traverse all possible paths without revisiting small caves
    start = ('start', set(['start'])) # current position and set of small caves not to revisit
    ans = 0 # Number of possible paths
    Q = deque([start]) # Using a queue for breadth-first search

    while Q: # Keep searching until the queue is empty
        pos, small = Q.popleft() # Look at the front of the queue
        if pos == 'end': # if we are at the end,
            ans += 1 # add to the number of possible paths
            continue # and go to the next element in the queue
        for y in paths_dict[pos]: # For each key
            if y not in small: # If it is not in small
                new_small = set(small) # Get updated small set
                if y.lower() == y: # If the key is a small cave,
                    new_small.add(y) # add it to the list of small caves
                Q.append((y, new_small)) # Update the queue with the current key and small cave list
    return ans 
            
def part_2(paths_dict):
    # Part 2: Traverse all possible paths with allowing one small cave revisit
    start = ('start', set(['start']), None) # Keeping track also whether a small cave has been visited twice yet
    ans = 0
    Q = deque([start])

    while Q:
        pos, small, twice = Q.popleft()
        if pos == 'end':
            ans += 1
            continue 
        for y in paths_dict[pos]:
            if y not in small:
                new_small = set(small)
                if y.lower() == y:
                    new_small.add(y)
                Q.append((y, new_small, twice))
            elif y in small and twice is None and y not in ['start', 'end']: # If we still haven't used our second small cave visit
                Q.append((y, small, y))
    return ans

# data = ld.load_data('example12a.txt')
# data = ld.load_data('example12b.txt')
# data = ld.load_data('example12c.txt')
data = ld.load_data('input12.txt') 
paths_dict = adjacency_list(data)
print(f'part 1: {part_1(paths_dict)}') # 3856
print(f'part 2: {part_2(paths_dict)}') # 116692