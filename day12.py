# Day 12: Passage Pathing

import load_data as ld

data = ld.load_data('example12a.txt')
# data = ld.load_data('example12b.txt')
# data = ld.load_data('example12c.txt')
# data = ld.load_data('input12.txt') 


# Build nested dict of paths
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
            

print(paths_dict)

# Traverse the paths, counting along the way
paths_list = []
exploring = True

# Step 1: Initially queue and visited arrays are empty
visited = []
queue = []
small_visited = []

while exploring:
    cave = 'start'
    # Step 2: Push node 0 into queue and mark it visited
    queue.append(cave)
    visited.append(cave)
    small_visited.append(cave)
    this_path = [cave]
    
    # Step 3: Remove node from the front of queue and visit the unvisited neighbors and push them into queue
    while len(queue) > 0:
        cave = queue.pop(0)
        neighbors = paths_dict[cave]
        for n in neighbors:
            if n not in small_visited:
                queue.append(n)
                visited.append(n)
                this_path.append(n) #TODO: See if I need a depth-first search instead; It seems hard to manage the paths_list and this_path otherwise
                paths_list.append(this_path)
                if !n.isupper():
                    small_visited.append(n)



print(len(paths_list))