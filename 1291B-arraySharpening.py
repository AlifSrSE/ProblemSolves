# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1291/problem/B

import sys

def alif():
    try:
        t = int(sys.stdin.readline())
    except (IOError, ValueError):
        return

    while t > 0:
        try:
            n = int(sys.stdin.readline())
            a = list(map(int, sys.stdin.readline().split()))
        except (IOError, ValueError):
            t -= 1
            continue

        left = [0] * n
        right = [0] * n
        
        for p in range(n):
            if p == 0:
                left[p] = 1 if a[p] >= p else 0
            else:
                left[p] = 1 if left[p - 1] and a[p] >= p else 0
        for p in range(n - 1, -1, -1):
            if p == n - 1:
                right[p] = 1 if a[p] >= n - 1 - p else 0
            else:
                right[p] = 1 if right[p + 1] and a[p] >= n - 1 - p else 0

        res = False
        for p in range(n):
            if left[p] and right[p]:
                res = True
                break
        
        if res:
            print("Yes")
        else:
            print("No")
        
        t -= 1

if __name__ == "__main__":
    alif()