# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys
from itertools import product
input = sys.stdin.readline

INF = int(1e9)

def solve():
    n = 12
    n = int(input())

    ar = [[[123455 for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ar[i][j] = list(map(int, input().split()))

    dp = [[INF] * (1 << n) for _ in range(1 << n)]
    dp[0][0] = 0

    vc = [[] for _ in range(n + 1)]
    nxt = [[] for _ in range(1 << n)]

    for i in range(1 << n):
        vc[bin(i).count('1')].append(i)

    for i in range(1 << n):
        for j in range(n):
            if (i & (1 << j)) == 0:
                nxt[i].append((j, i | (1 << j)))

    for i in range(n):
        for bp1 in vc[i]:
            for p1, nbp1 in nxt[bp1]:
                for bp2 in vc[i]:
                    for p2, nbp2 in nxt[bp2]:
                        dp[nbp1][nbp2] = min(dp[nbp1][nbp2], ar[i][p1][p2] + dp[bp1][bp2])

    print(dp[(1 << n) - 1][(1 << n) - 1])


def main():
    T = 1
    # T = int(input())
    for _ in range(T):
        solve()

if __name__ == "__main__":
    main()
