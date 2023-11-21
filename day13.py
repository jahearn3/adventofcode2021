# Day 13: Transparent Origami

import load_data as ld

data = ld.load_data('example13.txt')
data = ld.load_data('input13.txt') 

transparency = [] 
instructions = []
blank = False

for line in data:
    if len(line) == 0:
        blank = True
        continue
    if blank:
        orientation, foldline = line.split('=')
        instructions.append([orientation[-1], foldline])
    else:
        transparency.append(line)

# print(transparency)
# print('...')
# print(instructions)
print(len(transparency))
prev_transparency = transparency
for fold in instructions:
    next_transparency = []
    orientation = fold[0]
    foldline = int(fold[1])
    # print(orientation, foldline)
    if(orientation == 'y'): # fold up
        # all x values remain the same
        for dot in prev_transparency:
            x, y = dot.split(',')
            x, y = int(x), int(y)
            if(y > foldline):
                y = foldline - (y - foldline) 
                dot = f'{x},{y}'
            next_transparency.append(dot)
    elif(orientation == 'x'): # fold left
        # all y values remain the same
        for dot in prev_transparency:
            x, y = dot.split(',')
            x, y = int(x), int(y)
            if(x > foldline):
                x = foldline - (x - foldline)
                dot = f'{x},{y}'
            next_transparency.append(dot)
    prev_transparency = next_transparency
    print(len(set(prev_transparency)))

# Part 1 answer was 695

# Part 2
