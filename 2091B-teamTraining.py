# Author: AlifSrSe
# date: 2025-03-26
# https://codeforces.com/problemset/problem/2091/B
 
def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    
    teams = 0
    left = 0
    right = 0
    
    while right < n:
        if (right - left + 1) * a[right] >= x:
            teams += 1
            left = right + 1
            right = left
        else:
            right += 1
            
    print(teams)

t = int(input())
for _ in range(t):
    solve()