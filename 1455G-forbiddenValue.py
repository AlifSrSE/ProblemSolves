# Author: AlifSrSE

import sys
sys.setrecursionlimit(10**7)

def solve():
    n, s = map(int, sys.stdin.readline().split())
    prog = [sys.stdin.readline().split() for _ in range(n)]
    pos = 0

    def dfs():
        nonlocal pos
        dp = {0: 0}

        while pos < n:
            line = prog[pos]
            pos += 1

            if line[0] == 'set':
                y = int(line[1])
                v = int(line[2])
                ndp = {}
                for x, cost in dp.items():
                    if y == s:
                        ndp[x] = min(ndp.get(x, 10**30), cost + v)
                    else:
                        ndp[y] = min(ndp.get(y, 10**30), cost)
                        ndp[x] = min(ndp.get(x, 10**30), cost + v)
                dp = ndp

            elif line[0] == 'if':
                cond = int(line[1])
                inner = dfs()
                ndp = {}
                for x, cost in dp.items():
                    if x == cond:
                        for y, c2 in inner.items():
                            ndp[y] = min(ndp.get(y, 10**30), cost + c2)
                    else:
                        ndp[x] = min(ndp.get(x, 10**30), cost)
                dp = ndp

            else:  # end
                break

        return dp

    res = dfs()
    print(min(res.values()))

if __name__ == "__main__":
    solve()
