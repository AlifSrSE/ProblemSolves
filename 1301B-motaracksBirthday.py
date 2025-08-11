# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1301/problem/B

import sys

def solve():
    try:
        n_str = sys.stdin.readline()
        if not n_str: return
        n = int(n_str)
        a = list(map(int, sys.stdin.readline().split()))
    except (IOError, ValueError):
        return
    
    mn = float('inf')
    mx = float('-inf')
    diff = 0

    for p in range(n):
        if p + 1 < n and a[p] >= 0 and a[p+1] == -1:
            mn = min(mn, a[p])
            mx = max(mx, a[p])
        if p + 1 < n and a[p] == -1 and a[p+1] >= 0:
            mn = min(mn, a[p+1])
            mx = max(mx, a[p+1])
        if p + 1 < n and a[p] >= 0 and a[p+1] >= 0:
            current_diff = abs(a[p] - a[p+1])
            diff = max(diff, current_diff)
    
    pick = 0
    if mn == float('inf') or mx == float('-inf'):
        pick = 0
    else:
        pick = (mn + mx) // 2
        tmp = abs(mx - pick)
        diff = max(diff, tmp)
    print(diff, pick)

def main():
    try:
        t_str = sys.stdin.readline()
        if not t_str: return
        t = int(t_str)
    except (IOError, ValueError):
        return
        
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()