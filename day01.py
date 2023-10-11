# Day 1: Sonar Sweep

import load_data as ld 

def count_increases(data):
    count = 0
    for i in range(1,len(data)):
        if(int(data[i]) > int(data[i-1])):
            count += 1
            # Finding the wrench
            if(data[i] <= data[i-1]):
                print(data[i], data[i-1])
                # 1009 986
                # 10019 9994
    return count

def count_window_increases(data):
    count = 0
    for i in range(3,len(data)):
        window_curr = int(data[i]) + int(data[i-1]) + int(data[i-2])
        window_prev = int(data[i-1]) + int(data[i-2]) + int(data[i-3])
        if(window_curr > window_prev):
            count += 1
    return count

# data = ld.load_data('example01.txt')
data = ld.load_data('input01.txt')
count = count_increases(data)
print(count)
# 1764 too low, needed to cast to int
# 1766 correct 

count = count_window_increases(data)
print(count)
# 1797 was correct