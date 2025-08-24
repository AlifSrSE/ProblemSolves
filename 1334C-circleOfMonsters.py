# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())
    while t > 0:
        n = int(sys.stdin.readline())
        a = []
        b = []
        for _ in range(n):
            x, y = map(int, sys.stdin.readline().split())
            a.append(x)
            b.append(y)
        
        total_cost = 0
        for i in range(n):
            prev_explosion_damage = b[(i - 1 + n) % n]
            bullets_needed = max(0, a[i] - prev_explosion_damage)
            total_cost += bullets_needed

        initial_cost = 0
        initial_cost += a[0]
        
        for i in range(1, n):
            damage = b[i - 1]
            initial_cost += max(0, a[i] - damage)
        min_cost = float('inf')

        for i in range(n):
            current_cost = 0
            current_cost += a[i]
            
            for j in range(1, n):
                monster_index = (i + j) % n
                prev_monster_index = (i + j - 1) % n
                
                damage_from_prev = b[prev_monster_index]
                current_cost += max(0, a[monster_index] - damage_from_prev)
            
            min_cost = min(min_cost, current_cost)
        
        sys.stdout.write(str(min_cost) + '\n')
        t -= 1

alif()