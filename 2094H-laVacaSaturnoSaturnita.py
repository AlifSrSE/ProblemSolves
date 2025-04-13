# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import sys
from collections import defaultdict
from bisect import bisect_left

def divisors(x):
    result = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            result.add(i)
            result.add(x // i)
    return result

def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())
        a = [0] + list(map(int, input().split()))
        pos_map = defaultdict(list)
        for i in range(1, n + 1):
            pos_map[a[i]].append(i)
        for _ in range(q):
            k, l, r = map(int, input().split())
            pos = l
            total = 0
            current = k
            while pos <= r:
                divs = divisors(current)
                nxt = r + 1
                for d in divs:
                    if d < 2 or d not in pos_map:
                        continue
                    i = bisect_left(pos_map[d], pos)
                    if i < len(pos_map[d]):
                        nxt = min(nxt, pos_map[d][i])
                if nxt == r + 1:
                    total += (r - pos + 1) * current
                    break
                total += (nxt - pos) * current
                while current % a[nxt] == 0:
                    current //= a[nxt]
                total += current
                pos = nxt + 1
            print(total)

if __name__ == "__main__":
    main()
