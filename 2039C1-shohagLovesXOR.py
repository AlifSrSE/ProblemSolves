# Author : AlifSrSE
# Date : 2025-03-16
# Problem link : https://codeforces.com/contest/2039/problem/C1

import sys
import math

def binpow(a, b, m=None):
    if m is None:
        ans = 1
        while b > 0:
            if b & 1:
                ans *= a
            a *= a
            b >>= 1
        return ans
    else:
        a %= m
        ans = 1
        while b > 0:
            if b & 1:
                ans = ans * a % m
            a = a * a % m
            b >>= 1
        return ans

def solve():
    x, m = map(int, sys.stdin.readline().split())
    cnt = 0
    y_start = binpow(2, int(math.log2(x)))

    if y_start * 2 > m:
        max_y = m
    else:
        max_y = min(2 * x, m)

    for y in range(y_start, max_y + 1):
        exor = x ^ y
        if x != y and (x % exor == 0 or y % exor == 0):
            cnt += 1
    print(cnt)

def main():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()