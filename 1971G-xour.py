# Author: AlifSrSe
# date: 2025-03-20
# https://codeforces.com/problemset/problem/1971/G

from collections import defaultdict

def solve():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        groups = defaultdict(list)
        
        for i, num in enumerate(a):
            key = num >> 2 
            groups[key].append((num, i))
        
        for key in groups:
            group = sorted(groups[key])
            indices = sorted(pair[1] for pair in group)
            for idx, (val, _) in zip(indices, group):
                a[idx] = val
    
        print(*a)

if __name__ == "__main__":
    solve()     