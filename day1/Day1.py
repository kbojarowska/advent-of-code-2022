with open('input.txt', 'r') as f:
    data = f.read().strip().split("\n\n")
f.close()

elf = []  
for calories in data:  
    elf.append(sum(int(cal) for cal in calories.split("\n")))  

elf.sort()  

print('Part 1:', elf[-1])    
print('Part 2:', sum(elf[-3:]))