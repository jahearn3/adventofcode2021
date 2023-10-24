# Day 7: The Treachery of Whales

import load_data as ld
import numpy as np 

def split_data(data):
    data_list = data[0].split(',')
    crab_list = []
    for crab in data_list:
        crab_list.append(int(crab))
    return crab_list

def part1fuel(i, crab):
    return abs(i - crab)

def part2fuel(i, crab):
    distance = abs(i - crab)
    fuel = 0
    for j in range(distance):
        fuel += (j + 1)
    return fuel

def calculate_fuel(i, data_list, part):
    fuel = 0
    for crab in data_list:
        if(part == 1):
            fuel += part1fuel(i, crab)
        elif(part == 2):
            fuel += part2fuel(i, crab)
    return fuel

def optimize_fuel(data_list, part):
    start_quartile = int(np.quantile(data_list, 0.25))
    stop_quartile = int(np.quantile(data_list, 0.75)) + 1
    for i in range(start_quartile, stop_quartile):
        fuel = calculate_fuel(i, data_list, part)
        if(i == start_quartile):
            min_fuel = fuel 
        elif(fuel < min_fuel):
            min_fuel = fuel
    return min_fuel

data = ld.load_data('example07.txt')
data = ld.load_data('input07.txt')
crab_list = split_data(data)
print(f'{optimize_fuel(crab_list, 1)}') # 352331
print(f'{optimize_fuel(crab_list, 2)}') # 99266250