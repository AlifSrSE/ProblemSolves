# Author : AlifSrSE
# Date : 2025-03-15
# Problem link : https://codeforces.com/contest/2074/problem/B

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split())) 

        ans = a[-1]
        for i in range(n - 2, -1, -1):
            ans = ans + a[i] - 1

        print(ans)

solve()
