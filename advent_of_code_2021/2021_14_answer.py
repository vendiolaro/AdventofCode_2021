#%% Day 14 Part 2
import copy
from itertools import tee
import collections
with open('2021_14.txt') as f:
   inp = f.read()

polymer = inp.split('\n\n')[0]
template_raw = inp.split('\n\n')[1]

# Function to print sequential pairs
def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

# Create a dictionary of the template
template = {}
for line in template_raw.split('\n'):
    a, b = line.split(' -> ')
    template[a] = b

# Create a dictionary of all possible pairs in the polymer
counts = {k:0 for k,v in template.items()}
for a,b in pairwise(polymer):
    counts[a+b] += 1

# Count the atoms that are in the polymer before any steps
atoms = {a:polymer.count(a) for a in list(set((polymer + ''.join(template.values()) + ''.join(template.keys()))))}

# With each step, keep track of the pairs that are created from each pair and increase the count of that pair in "counts"
for _ in range(40):
    counts2 = {k:0 for k,v in template.items()}         #created so that you zero out "counts" before each new iteration. In other words, you are removing the old pairs as the polymer grows
    for k,v in counts.items():
        if v>0:
            p1, p2 = k[0]+template[k], template[k]+k[1]
            counts2[p1] += v
            counts2[p2] += v
            atoms[template[k]] += v                 #Increase the count of the atom that the "k" pair will create by the number of pairs created during this cycle
    counts = copy.deepcopy(counts2)

#Print answer
print(max(atoms.values()) - min(atoms.values()))