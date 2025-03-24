# Author: AlifSrSe
# date: 2025-03-23
# https://codeforces.com/problemset/problem/2090/A
 
def solve_treasure_digging():
    t = int(input())
    
    for _ in range(t):
        x, y, a = map(int, input().split())
        target = a + 0.5
        
        if x >= target:
            print("NO") 
            continue
            
        cycle_depth = x + y 
        cycles = int(target // cycle_depth)
        total_so_far = cycles * cycle_depth
        remaining = target - total_so_far
        if remaining <= x:
            print("NO")
        else:
            print("YES")
solve_treasure_digging()