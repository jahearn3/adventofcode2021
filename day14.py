# Day 14: Extended Polymerization

import load_data as ld
from collections import Counter 

data = ld.load_data('example14.txt')
data = ld.load_data('input14.txt') 

template = data[0]
pair_insertion_rules = {}

for line in data[2:]:
    pair, insertion = line.split(' -> ')
    pair_insertion_rules[pair] = insertion 

# 10 steps of pair insertion
for i in range(10):
    next_template = ''
    for j in range(1, len(template)):
        sequence = template[j-1:j+1]
        for k,v in pair_insertion_rules.items():
            if(sequence == k):
                next_template += sequence[0] + v 
                continue
    next_template += template[-1]
    template = next_template

# Find most common and least common elements
frequencies = Counter(template).most_common()
most_common = frequencies[0]
least_common = frequencies[-1]
ans = most_common[1] - least_common[1]
print(ans) # Part 1 answer: 2068 