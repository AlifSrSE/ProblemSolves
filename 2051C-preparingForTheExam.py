# Author : AlifSrSE
# Date : 2025-03-17
# Problem link : https://codeforces.com/contest/2051/problem/C

def solve():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if k == n:
        print('1' * m)
    elif k <= n - 2:
        print('0' * m)
    else:
        mm = {}
        for i in range(k):
            mm[b[i]] = mm.get(b[i], 0) + 1
        result = ''
        for i in range(m):
            if mm.get(a[i], 0):
                result += '0'
            else:
                result += '1'
        print(result)

t = int(input())
for _ in range(t):
    solve()