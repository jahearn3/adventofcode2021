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

def decode_line(pattern, line):
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
    wire_dict['top'] = [letter for letter in letters_of_7 if letter not in right_letters][0]
    letters_of_4 = [letter for letter in digit_dict['4']]
    letters_of_8 = [letter for letter in digit_dict['8']]
    upleft_and_middle_letters = [letter for letter in letters_of_4 if letter not in right_letters]
    for sig in undecoded_6: # 0, 6, 9
        signal_letters = [letter for letter in sig]
        letters_in_signal_and_upleft_and_middle = set(signal_letters) & set(upleft_and_middle_letters)
        letters_in_signal_and_right_letters = set(signal_letters) & set(right_letters)
        # 0 does not have middle letter
        if(len(letters_in_signal_and_upleft_and_middle) == 1):
            digit_dict['0'] = sig
            upleft_and_middle_letter_not_in_signal = set(upleft_and_middle_letters) - set(signal_letters)
            wire_dict['middle'] = upleft_and_middle_letter_not_in_signal.pop()
            wire_dict['upleft'] = letters_in_signal_and_upleft_and_middle.pop()
        # 6 does not have one of the right letters
        elif(len(letters_in_signal_and_right_letters) == 1):
            digit_dict['6'] = sig
            right_letter_not_in_signal = set(right_letters) - set(signal_letters)
            remaining_letter = set(right_letters) - set(right_letter_not_in_signal)
            wire_dict['upright'] = right_letter_not_in_signal.pop()
            wire_dict['botright'] = remaining_letter.pop()
        # 9 is the other one
        else:
            digit_dict['9'] = sig
            top_and_bottom_letters = set(signal_letters) - set(letters_in_signal_and_right_letters) - set(letters_in_signal_and_upleft_and_middle)
            bottom_letter = set(top_and_bottom_letters) - set(letters_of_7)
            wire_dict['bottom'] = bottom_letter.pop()
    # print(wire_dict)
    last_letter = set(letters_of_8) - set(wire_dict.values())
    wire_dict['botleft'] = last_letter.pop()
    # wire_dict is now solved
    for sig in undecoded_5: # 5, 2, 3
        signal_letters = [letter for letter in sig]
        letters_in_signal_and_upleft_and_middle = set(signal_letters) & set(upleft_and_middle_letters)
        letters_in_signal_and_right_letters = set(signal_letters) & set(right_letters)
        # 5 is the one with both the upleft and middle letters
        if(len(letters_in_signal_and_upleft_and_middle) == 2):
            digit_dict['5'] = sig
        # 3 is the one with both right letters
        elif(len(letters_in_signal_and_right_letters) == 2):
            digit_dict['3'] = sig
        # 2 is the other one
        else:
            digit_dict['2'] = sig
    output_value = ''
    for element in segments:
        ele_letters = [letter for letter in element]
        for key, value in digit_dict.items():
            val_letters = [letter for letter in value]
            common_letters = list(set(ele_letters).intersection(val_letters))
            if(len(common_letters) == len(ele_letters)):
                output_value += key
                break
    output_value = int(output_value)
    print(output_value)
    return output_value

def part2(patterns, output):
    sum = 0
    print(len(patterns))
    for i in range(len(patterns)):
        sum += decode_line(patterns[i], output[i])
    return sum

# data = ld.load_data('example08a.txt')
data = ld.load_data('example08b.txt')
# data = ld.load_data('input08.txt')
patterns, output = split_data(data)
# print(f'{part1(output)}') # 534
print(f'{part2(patterns, output)}') 
# 55593 is too low for exampleb, should be 61229
# 684560 is too low for input


# sum = 0
# # for pattern, line in patterns, output:
# pattern = patterns[0]
# line = output[0]
# signals = pattern.split(' ')
# segments = line.split(' ')
# digit_dict = {'0':'', '1':'','2':'', '3':'','4':'', '5':'','6':'', '7':'','8':'', '9':'',}
# wire_dict = {'top': '', 'middle': '', 'bottom': '', 'upleft': '', 'upright': '', 'botleft': '', 'botright': ''}
# undecoded_5 = []
# undecoded_6 = []
# #%%
# for signal in signals:
#     if(len(signal) == 2):
#         digit_dict['1'] = signal
#     elif(len(signal) == 3):
#         digit_dict['7'] = signal
#     elif(len(signal) == 4):
#         digit_dict['4'] = signal
#     elif(len(signal) == 7):
#         digit_dict['8'] = signal
#     elif(len(signal) == 5): # 5, 2, 3
#         undecoded_5.append(signal)
#     elif(len(signal) == 6): # 0, 6, 9
#         undecoded_6.append(signal)
# #%%
# # Initial deductions
# right_letters = [letter for letter in digit_dict['1']]
# letters_of_7 = [letter for letter in digit_dict['7']]
# wire_dict['top'] = [letter for letter in letters_of_7 if letter not in right_letters][0]
# letters_of_4 = [letter for letter in digit_dict['4']]
# letters_of_8 = [letter for letter in digit_dict['8']]
# upleft_and_middle_letters = [letter for letter in letters_of_4 if letter not in right_letters]
# #%%
# # letters_of_0 = [letter for letter in digit_dict['0']]
# # letters_of_6 = [letter for letter in digit_dict['6']]
# # letters_of_9 = [letter for letter in digit_dict['9']]
# for sig in undecoded_6: # 0, 6, 9
#     signal_letters = [letter for letter in sig]
#     letters_in_signal_and_upleft_and_middle = set(signal_letters) & set(upleft_and_middle_letters)
#     letters_in_signal_and_right_letters = set(signal_letters) & set(right_letters)
#     # 0 does not have middle letter
#     if(len(letters_in_signal_and_upleft_and_middle) == 1):
#         digit_dict['0'] = sig
#         upleft_and_middle_letter_not_in_signal = set(upleft_and_middle_letters) - set(signal_letters)
#         wire_dict['middle'] = upleft_and_middle_letter_not_in_signal.pop()
#         wire_dict['upleft'] = letters_in_signal_and_upleft_and_middle.pop()
#     # 6 does not have one of the right letters
#     elif(len(letters_in_signal_and_right_letters) == 1):
#         digit_dict['6'] = sig
#         right_letter_not_in_signal = set(right_letters) - set(signal_letters)
#         remaining_letter = set(right_letters) - set(right_letter_not_in_signal)
#         wire_dict['upright'] = right_letter_not_in_signal.pop()
#         wire_dict['botright'] = remaining_letter.pop()
#     # 9 is the other one
#     else:
#         digit_dict['9'] = sig
#         top_and_bottom_letters = set(signal_letters) - set(letters_in_signal_and_right_letters) - set(letters_in_signal_and_upleft_and_middle)
#         bottom_letter = set(top_and_bottom_letters) - set(letters_of_7)
#         wire_dict['bottom'] = bottom_letter.pop()
#     last_letter = set(letters_of_8) - set(wire_dict.values())
#     wire_dict['botleft'] = last_letter.pop()
# # wire_dict is now solved
# #%%
# # letters_of_5 = [letter for letter in digit_dict['5']]
# # letters_of_3 = [letter for letter in digit_dict['3']]
# # letters_of_2 = [letter for letter in digit_dict['2']]
# for sig in undecoded_5: # 5, 2, 3
#     signal_letters = [letter for letter in sig]
#     letters_in_signal_and_upleft_and_middle = set(signal_letters) & set(upleft_and_middle_letters)
#     letters_in_signal_and_right_letters = set(signal_letters) & set(right_letters)
#     # 5 is the one with both the upleft and middle letters
#     if(len(letters_in_signal_and_upleft_and_middle) == 2):
#         digit_dict['5'] = sig
#     # 3 is the one with both right letters
#     elif(len(letters_in_signal_and_right_letters) == 2):
#         digit_dict['3'] = sig
#     # 2 is the other one
#     else:
#         digit_dict['2'] = sig
# #%% 
# output_value = ''
# digits = line.split()

# matching_keys = []
# for element in digits:
#     ele_letters = [letter for letter in element]
#     for key, value in digit_dict.items():
#         val_letters = [letter for letter in value]
#         common_letters = list(set(ele_letters).intersection(val_letters))
#         if(len(common_letters) == len(ele_letters)):
#             matching_keys.append(key)
#             output_value += key
#             break

# print(matching_keys)
# output_value = int(output_value)
# print(output_value)
# sum = 0
# # %%
