# Day 10: Syntax Scoring

import load_data as ld

data = ld.load_data('example10.txt')
# data = ld.load_data('input10.txt') 

round_count  = 0
square_count = 0
curly_count  = 0
angle_count  = 0
line_classification = []

for i, line in enumerate(data):
    round_layer  = 0
    square_layer = 0
    curly_layer  = 0
    angle_layer  = 0
    print(i, line)
    # Classify as corrupted or incomplete
    for char in line:
        if(char == ')'):
            if(round_layer > 0):
                round_layer -= 1 
            else:
                round_count += 1
                line_classification.append('corrupted')
                break
        elif(char == ']'):
            if(square_layer > 0):
                square_layer -= 1
            else:
                square_count += 1
                line_classification.append('corrupted')
                break
        elif(char == '}'):
            if(curly_layer > 0):
                curly_layer -= 1
            else:
                curly_count += 1
                line_classification.append('corrupted')
                break
        elif(char == '>'):
            if(angle_layer > 0):
                angle_layer -= 1
            else:
                angle_count += 1
                line_classification.append('corrupted')
                break
        elif(char == '('):
            round_layer += 1
        elif(char == '['):
            square_layer += 1
        elif(char == '{'):
            curly_layer += 1
        elif(char == '<'):
            angle_layer += 1
    if(len(line_classification) < i):
        if(round_layer + square_layer + curly_layer + angle_layer == 0):
            line_classification.append('complete')
        else:
            line_classification.append('incomplete')
    else:
        print('Weird error for line: \n', line)
    print(line, line_classification[i])

syntax_error_score = (3 * round_count) + (57 * square_count) + (1197 * curly_count) + (25137 * angle_count)

print(syntax_error_score)  
        