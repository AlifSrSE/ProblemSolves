# Author: AlifSrSe
# date: 2025-03-25
# https://codeforces.com/problemset/problem/2089/B1
 
def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    pre = [0] * (n + 1)
    for i in range(n):
        pre[i + 1] = pre[i] + a[i] - b[i]
    
    x = pre.index(min(pre))
    a_rotated = a[x:] + a[:x]
    b_rotated = b[x:] + b[:x]
    
    def check(x):
        stk = []
        sum_val = 0
        na = a_rotated[:]
        nb = b_rotated[:]
        for i in range(n):
            stk.append(i)
            while stk and nb[i] > 0:
                j = stk[-1]
                if i - j >= x:
                    sum_val += na[j]
                    stk.pop()
                else:
                    t = min(na[j], nb[i])
                    nb[i] -= t
                    na[j] -= t
                    if na[j] == 0:
                        stk.pop()
        return sum_val <= k
    
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi) // 2
        if check(mid):
            hi = mid
        else:
            lo = mid + 1
    
    print(lo)

t = int(input())
for _ in range(t):
    solve()