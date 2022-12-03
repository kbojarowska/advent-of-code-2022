from string import ascii_lowercase, ascii_uppercase

def calc_priority(character):
    if character in ascii_lowercase:
        return (ord(character)-96)
    elif character in ascii_uppercase:
        return (ord(character)-38)

with open('input.txt', 'r') as f:
    data = f.read().split()
f.close()

priority = 0
for rucksack in data:
    com1, com2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    for item in (set(com1) & set(com2)):
        priority += calc_priority(item)

print(priority)
priority = 0

for i in range(0, len(data), 3):
    rucksack1, rucksack2, rucksack3 = set(data[i]), set(data[i+1]), set(data[i+2])
    for item in (rucksack1 & rucksack2 & rucksack3):
        priority += calc_priority(item)

print(priority)
