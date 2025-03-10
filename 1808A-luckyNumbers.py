# Author : AlifSrSE
# Date : 2025-03-10
# Problem link : https://codeforces.com/contest/1808/problem/A

import math
import sys

def main():
    t = int(input())
    for _ in range(t):
        l, r = map(int, input().split())
        ans = {}
        for i in range(l, min(r, l + 90) + 1):
            now = i
            mx = -1 
            mn = float('inf')
            
            while now:
                digit = now % 10
                mx = max(mx, digit)
                mn = min(mn, digit)
                now //= 10
            ans[mx - mn] = i
        
        for i in range(9, -1, -1):
            if i in ans:
                print(ans[i])
                break

if __name__ == "__main__":
    main()