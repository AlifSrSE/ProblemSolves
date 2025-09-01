# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t = int(sys.stdin.readline())

    for _ in range(t):
        n = int(sys.stdin.readline())
        if n == 0:
            print("YES")
            continue
        a = list(map(int, sys.stdin.readline().split()))

        a.sort()
        odd_count = sum(1 for x in a if x % 2 != 0)
        has_consecutive = False

        for i in range(1, n):
            if a[i] == a[i - 1] + 1:
                has_consecutive = True
                break

        if odd_count % 2 == 0 or has_consecutive:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    alif()