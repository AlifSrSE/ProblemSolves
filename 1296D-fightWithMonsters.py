# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1296/problem/D

import sys
import math

def alif():
    try:
        n, a, b, k = map(int, sys.stdin.readline().split())
        h = list(map(int, sys.stdin.readline().split()))
    except (IOError, ValueError):
        return

    spell_costs = []
    s = a + b
    
    for health in h:
        remaining_health = health % s
        if remaining_health == 0:
            remaining_health = s
            
        if remaining_health > a:
            spells_needed = math.ceil((remaining_health - a) / a)
            spell_costs.append(spells_needed)
        else:
            spell_costs.append(0)

    spell_costs.sort()
    monsters_defeated = 0
    
    for cost in spell_costs:
        if k >= cost:
            k -= cost
            monsters_defeated += 1
        else:
            break
    
    print(monsters_defeated)

def main():
    alif()

if __name__ == "__main__":
    main()