# Day 8: Seven Segment Search

import load_data as ld

def split_data(data):
    patterns = []
    output = []
    for line in data:
        patterns_, output_ = line.split('|')
        patterns.append(patterns_)
        output.append(output_) 
    return patterns, output

def part1(output):
    count = 0
    for line in output:
        segments = line.split(' ')
        for segment in segments:
            if(len(segment) == 2): # digit = 1
                count += 1
            elif(len(segment) == 3): # digit = 7
                count += 1
            elif(len(segment) == 4): # digit = 4
                count += 1
            elif(len(segment) == 7): # digit = 8
                count += 1
    return count 

def part2(patterns, output):
    sum = 0
    for pattern, line in patterns, output:
        signals = pattern.split(' ')
        segments = line.split(' ')
        digit_dict = {'0':'', '1':'','2':'', '3':'','4':'', '5':'','6':'', '7':'','8':'', '9':'',}
        wire_dict = {'top': '', 'middle': '', 'bottom': '', 'upleft': '', 'upright': '', 'botleft': '', 'botright': ''}
        undecoded_5 = []
        undecoded_6 = []
        for signal in signals:
            if(len(signal) == 2):
                digit_dict['1'] = signal
            elif(len(signal) == 3):
                digit_dict['7'] = signal
            elif(len(signal) == 4):
                digit_dict['4'] = signal
            elif(len(signal) == 7):
                digit_dict['8'] = signal
            elif(len(signal) == 5): # 5, 2, 3
                undecoded_5.append(signal)
            elif(len(signal) == 6): # 0, 6, 9
                undecoded_6.append(signal)
        # Initial deductions
        right_letters = [letter for letter in digit_dict['1']]
        letters_of_7 = [letter for letter in digit_dict['7']]
        wire_dict['top'] = [letter for letter in letters_of_7 if letter not in right_letters]
        letters_of_4 = [letter for letter in digit_dict['4']]
        upleft_and_middle_letters = [letter for letter in letters_of_4 if letter not in right_letters]
        for sig in undecoded_6: # 0, 6, 9
            signal_letters = [letter for letter in sig]
            letters_in_signal_and_upleft_and_middle = [letter for letter in upleft_and_middle_letters not in signal_letters] # may need to swap the lists
            letters_in_signal_and_right_letters = [letter for letter in right_letters not in signal_letters] # may need to swap the lists
            # 0 does not have middle letter
            if(len(letters_in_signal_and_upleft_and_middle) > 0):
                digit_dict['0'] = sig
                wire_dict['middle'] = 
            # 6 does not have one of the right letters
            elif(len(letters_in_signal_and_right_letters) > 0):
                digit_dict['6'] = sig
                wire_dict['upright'] = 
            # 9 is the other one
            else:
                digit_dict['9'] = sig
                wire_dict['botleft'] = 

            

            
        for sig in undecoded_5: # 5, 2, 3
            # 5 is the one with both the upleft and middle letters

            # 3 is the one with both right letters

            # 2 is the other one
            


    return sum

# data = ld.load_data('example08a.txt')
# data = ld.load_data('example08b.txt')
data = ld.load_data('input08.txt')
patterns, output = split_data(data)
print(f'{part1(output)}') # 534
print(f'{part2(patterns, output)}') 