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
    # print(i + 1, len(template))

# Find most common and least common elements
frequencies = Counter(template).most_common()
most_common = frequencies[0]
least_common = frequencies[-1]
ans = most_common[1] - least_common[1]
print(ans) # Part 1 answer: 2068 

# Part 2 with help from Jonathan Paulson
template = data[0]

pair_counter = Counter()
for i in range(len(template) - 1):
    pair_counter[template[i]+template[i+1]] += 1

for i in range(40):
    C2 = Counter()
    for k in pair_counter:
        C2[k[0]+pair_insertion_rules[k]] += pair_counter[k]
        C2[pair_insertion_rules[k]+k[1]] += pair_counter[k]
    pair_counter = C2

    if i + 1 in [10, 40]:
        CF = Counter()
        for k in pair_counter:
            CF[k[0]] += pair_counter[k]
        CF[template[-1]] += 1
        print(max(CF.values()) - min(CF.values()))

# 5647232997696 too high
# Part 2 answer: 2158894777814 