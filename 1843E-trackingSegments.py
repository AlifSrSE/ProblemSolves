# Author : AlifSrSE
# Date : 2025-03-09
# Problem link : https://codeforces.com/contest/1843/problem/E

def check(n, l, r, x, change_num):
    a = [0] * n
    for i in range(change_num):
        a[x[i] - 1] = 1
    
    prefix_sums = [0] * n
    for i in range(n):
        prefix_sums[i] = (0 if i == 0 else prefix_sums[i-1]) + a[i]
    
    return any(
        2 * (prefix_sums[r[i]-1] - (0 if l[i] == 1 else prefix_sums[l[i]-2])) > r[i] - l[i] + 1
        for i in range(len(l))
    )

def solve(n, l, r, x):
    result = -1
    lower = 0
    upper = len(x)
    while lower <= upper:
        middle = (lower + upper) // 2
        if check(n, l, r, x, middle):
            result = middle
            upper = middle - 1
        else:
            lower = middle + 1
    
    return result

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    l = []
    r = []
    for _ in range(m):
        li, ri = map(int, input().split())
        l.append(li)
        r.append(ri)
    
    q = int(input())
    x = list(map(int, input().split()))
    
    print(solve(n, l, r, x))