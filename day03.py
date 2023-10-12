# Day 3: Binary Diagnostic

import load_data as ld 

def decipher(data):
    gamma_rate = ''
    epsilon_rate = ''
    for i in range(len(data[0])):
        ones = 0
        zeros = 0
        for j in range(len(data)):
            if(data[j][i] == '0'):
                zeros += 1
            else:
                ones += 1
        if(zeros > ones):
            gamma_rate += '0'
            epsilon_rate += '1'
        else:
            gamma_rate += '1'
            epsilon_rate += '0'
    return int(gamma_rate, 2), int(epsilon_rate, 2)

def narrow_down(curr_data, i, mode):
    if(len(curr_data) == 1):
        return int(curr_data[0], 2)
    else:
        next_data = []
        # Count the ones and zeros for that bit
        ones = 0
        zeros = 0
        for j in range(len(curr_data)):
            if(curr_data[j][i] == '0'):
                zeros += 1
            else:
                ones += 1
        # Determine most common or least common digit for that bit (i)
        if(mode == 'most'):
            if(zeros > ones): 
                for j in range(len(curr_data)):
                    if(curr_data[j][i] == '0'):
                        next_data.append(curr_data[j])
            else:
                for j in range(len(curr_data)):
                    if(curr_data[j][i] == '1'):
                        next_data.append(curr_data[j])
        else:
            if(zeros > ones): 
                for j in range(len(curr_data)):
                    if(curr_data[j][i] == '1'):
                        next_data.append(curr_data[j])
            else:
                for j in range(len(curr_data)):
                    if(curr_data[j][i] == '0'):
                        next_data.append(curr_data[j])
        return narrow_down(next_data, i+1, mode)

def decipher2(data): 
    oxygen_generator_rating = narrow_down(data, 0, 'most')
    co2_scrubber_rating = narrow_down(data, 0, 'least')
    return oxygen_generator_rating, co2_scrubber_rating

def part1(data):
    gamma_rate, epsilon_rate = decipher(data)
    return gamma_rate * epsilon_rate

def part2(data):
    oxygen_generator_rating, co2_scrubber_rating = decipher2(data)
    return oxygen_generator_rating * co2_scrubber_rating

# data = ld.load_data('example03.txt')
data = ld.load_data('input03.txt')
print(f'{part1(data)}') # 3687446
print(f'{part2(data)}') # 4406844