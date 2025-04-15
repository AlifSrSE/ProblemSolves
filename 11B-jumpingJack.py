# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/11/B

def solve():
    n = int(input())
    if n < 0:
        n = -n
    
    sum_val = 0
    ans = 0
    p = 1
    
    while sum_val < n:
        sum_val += p
        p += 1
        ans += 1
    
    diff = sum_val - n
    
    if n == 0:
        print(0)
    elif diff % 2 == 0:
        print(ans)
    elif (diff + p) % 2 == 0:
        print(ans + 1)
    else:
        print(ans + 2)

solve()