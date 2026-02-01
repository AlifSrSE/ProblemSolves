

import sys
from itertools import permutations

def solve():
    t = int(sys.stdin.readline())
    INF = 10**30

    for _ in range(t):
        pts = [tuple(map(int, sys.stdin.readline().split())) for _ in range(4)]
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]

        ans = INF

        for lx in xs:
            for rx in xs:
                if rx < lx:
                    continue
                side = rx - lx
                for ly in ys:
                    ry = ly + side
                    corners = [(lx, ly), (lx, ry), (rx, ly), (rx, ry)]
                    for perm in permutations(pts):
                        cost = 0
                        for i in range(4):
                            cost += abs(perm[i][0] - corners[i][0]) + abs(perm[i][1] - corners[i][1])
                        ans = min(ans, cost)

        print(ans)

if __name__ == "__main__":
    solve()
