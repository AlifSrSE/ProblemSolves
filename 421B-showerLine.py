from itertools import permutations

def calculate_happiness(order, g):
    happiness = 0
    happiness += g[order[0]][order[1]] + g[order[1]][order[0]]
    happiness += g[order[2]][order[3]] + g[order[3]][order[2]]
    happiness += g[order[1]][order[2]] + g[order[2]][order[1]]
    happiness += g[order[3]][order[4]] + g[order[4]][order[3]]
    happiness += g[order[2]][order[3]] + g[order[3]][order[2]]
    happiness += g[order[3]][order[4]] + g[order[4]][order[3]]
    return happiness

def max_happiness(g):
    max_happiness_value = float('-inf')
    for order in permutations(range(5)):
        happiness = calculate_happiness(order, g)
        max_happiness_value = max(max_happiness_value, happiness)
    return max_happiness_value

g = []
for _ in range(5):
    g.append(list(map(int, input().split())))
result = max_happiness(g)
print(result)