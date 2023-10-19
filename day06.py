# Day 6: Lanternfish 

import load_data as ld

def split_data(data):
    return [int(fish) for fish in data[0].split(',')]

def part1(fishlist, n_days = 80):
    for t in range(n_days):
        new_fish = 0
        # print(fishlist)
        for i in range(len(fishlist)):
            if(fishlist[i] == 0):
                fishlist[i] = 6
                new_fish += 1
            else:
                fishlist[i] -= 1
        for i in range(new_fish):
            fishlist.append(8)

    return len(fishlist)

def part2(fishlist):
    return 0

data = ld.load_data('example06.txt')
data = ld.load_data('input06.txt')
fishlist = split_data(data)
print(f'{part1(fishlist)}') # 386640
# print(f'{part2(fishlist)}') 