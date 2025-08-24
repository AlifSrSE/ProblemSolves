# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys
from bisect import bisect_left, bisect_right

def alif():
    t = int(sys.stdin.readline())
    while t > 0:
        nr, ng, nb = map(int, sys.stdin.readline().split())
        r = list(map(int, sys.stdin.readline().split()))
        g = list(map(int, sys.stdin.readline().split()))
        b = list(map(int, sys.stdin.readline().split()))

        r.sort()
        g.sort()
        b.sort()

        ans = float('inf')

        def calc_sq(x, y, z):
            return (x - y)**2 + (y - z)**2 + (z - x)**2

        for x in r:
            idx_g = bisect_left(g, x)
            idx_b = bisect_left(b, x)

            if idx_g < ng and idx_b < nb:
                ans = min(ans, calc_sq(x, g[idx_g], b[idx_b]))
            if idx_g < ng and idx_b > 0:
                ans = min(ans, calc_sq(x, g[idx_g], b[idx_b-1]))
            if idx_g > 0 and idx_b < nb:
                ans = min(ans, calc_sq(x, g[idx_g-1], b[idx_b]))
            if idx_g > 0 and idx_b > 0:
                ans = min(ans, calc_sq(x, g[idx_g-1], b[idx_b-1]))

        for x in g:
            idx_r = bisect_left(r, x)
            idx_b = bisect_left(b, x)

            if idx_r < nr and idx_b < nb:
                ans = min(ans, calc_sq(r[idx_r], x, b[idx_b]))
            if idx_r < nr and idx_b > 0:
                ans = min(ans, calc_sq(r[idx_r], x, b[idx_b-1]))
            if idx_r > 0 and idx_b < nb:
                ans = min(ans, calc_sq(r[idx_r-1], x, b[idx_b]))
            if idx_r > 0 and idx_b > 0:
                ans = min(ans, calc_sq(r[idx_r-1], x, b[idx_b-1]))

        for x in b:
            idx_r = bisect_left(r, x)
            idx_g = bisect_left(g, x)

            if idx_r < nr and idx_g < ng:
                ans = min(ans, calc_sq(r[idx_r], g[idx_g], x))
            if idx_r < nr and idx_g > 0:
                ans = min(ans, calc_sq(r[idx_r], g[idx_g-1], x))
            if idx_r > 0 and idx_g < ng:
                ans = min(ans, calc_sq(r[idx_r-1], g[idx_g], x))
            if idx_r > 0 and idx_g > 0:
                ans = min(ans, calc_sq(r[idx_r-1], g[idx_g-1], x))
                
        print(ans)
        t -= 1

if __name__ == "__main__":
    alif()