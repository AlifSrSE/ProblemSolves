# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1283/problem/B

import sys

def alif():
    try:
        t = int(sys.stdin.readline())
    except (IOError, ValueError):
        return

    for _ in range(t):
        try:
            n, k = map(int, sys.stdin.readline().split())
        except (IOError, ValueError):
            continue

        full_groups_count = n // k
        remaining_items = n % k
        ans = k * full_groups_count
        ans += min(remaining_items, k // 2)

        sys.stdout.write(str(ans) + "\n")

if __name__ == "__main__":
    alif()