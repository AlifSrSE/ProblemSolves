# Author : AlifSrSE
# Date : 2025-03-17
# Problem link : https://codeforces.com/contest/2070/problem/C

def solve():
    n, k = map(int, input().split())
    s = input()
    a = list(map(int, input().split()))
    l, r = 0, 10**9
    res = -1

    def check(d):
        last = 'R'
        cnt = 0
        for i in range(n):
            if a[i] > d:
                if s[i] == 'B' and last != 'B':
                    cnt += 1
                last = s[i]
        return cnt <= k

    while l <= r:
        m = (l + r) // 2
        if check(m):
            res = m
            r = m - 1
        else:
            l = m + 1
    print(res)

for _ in range(int(input())):
    solve()