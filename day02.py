# Day 2: Dive!

import load_data as ld 

def navigate(data):
    position = 0
    depth = 0
    for command in data:
        direction, steps = command.split()
        if(direction == 'forward'):
            position += int(steps)
        elif(direction == 'down'):
            depth += int(steps)
        elif(direction == 'up'):
            depth -= int(steps)
        else:
            print(command)
    return position * depth 

def navigate2(data):
    position = 0
    depth = 0
    aim = 0
    for command in data:
        direction, steps = command.split()
        if(direction == 'forward'):
            position += int(steps)
            depth += int(steps) * aim
        elif(direction == 'down'):
            aim += int(steps)
        elif(direction == 'up'):
            aim -= int(steps)
        else:
            print(command)
    return position * depth 

# data = ld.load_data('example02.txt')
data = ld.load_data('input02.txt')
print(f'{navigate(data)}') # 1840243
print(f'{navigate2(data)}') # 1727785422