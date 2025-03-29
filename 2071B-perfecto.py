# Author : AlifSrSE
# Date : 2025-03-29
# Problem link : https://codeforces.com/contest/2071/problem/B

import math

def solve():
    n = int(input())
    d = n * (n + 1) // 2
    k = int(math.sqrt(d))
    if k * k == d:
        print(-1)
    else:
        q = list(range(1, n + 1))
        s = 0
        result = []
        while q:
            p = q.pop(0)
            x = s + p
            k = int(math.sqrt(x))
            if k * k == x:
                q.append(p)
            else:
                s += p
                result.append(p)
        print(*result)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()