with open('input.txt', 'r') as f:
    data = f.read().split("\n")
f.close()

ruleABC = {'A': 1, 'B': 2, 'C': 3}
ruleXYZ = {'X': 1, 'Y': 2, 'Z': 3}
ruleLDW = {'X': 0, 'Y': 3, 'Z': 6}

totalPoints = 0

for r in data:
    totalPoints += ruleXYZ[r[2]]
    match ruleXYZ[r[2]] - ruleABC[r[0]]:
        case 0:
            totalPoints += 3
        case -2 | 1:
            totalPoints += 6
        case -1 | 2:
            totalPoints += 0

print('Part 1:',totalPoints)
totalPoints = 0

for r in data:
    match r[2]:
        case 'Z':
            totalPoints += 6 + ruleABC[r[0]] % 3 + 1
        case 'Y':
            totalPoints += 3 + ruleABC[r[0]]
        case 'X':
            totalPoints += 0 + (ruleABC[r[0]] + 1) % 3 + 1

print('Part 2:',totalPoints)