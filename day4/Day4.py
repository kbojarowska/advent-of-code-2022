import re

lines = [[*map(int, s.replace("-", ",").split(","))] for s in open("input.txt").read().split()]
overlap = 0
overlapRange = len(lines)

for pair in lines:
    elf1 = set([i for i in range(pair[0], pair[1] + 1)])
    elf2 = set([i for i in range(pair[2], pair[3] + 1)])
    if elf1.issubset(elf2) or elf2.issubset(elf1):
        overlap +=1 
    if pair[0] > pair[3] or pair[2] > pair[1]:
        overlapRange -= 1

print('Part 1:', overlap)
print('Part 2:', overlapRange)