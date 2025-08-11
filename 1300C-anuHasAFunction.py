# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1300/problem/C

import sys

def main():
    try:
        n_str = sys.stdin.readline()
        if not n_str:
            return
        n = int(n_str)
        a = list(map(int, sys.stdin.readline().split()))
    except (IOError, ValueError):
        return
    
    b = [~x for x in a]
    left = [0] * n
    right = [0] * n

    if n > 0:
        left[0] = b[0]
        for p in range(1, n):
            left[p] = left[p - 1] & b[p]
    if n > 0:
        right[n - 1] = b[n - 1]
        for p in range(n - 2, -1, -1):
            right[p] = right[p + 1] & b[p]
    ans = -1
    pos = -1

    for p in range(n):
        tmp = a[p]
        if p > 0:
            tmp &= left[p - 1]
        if p < n - 1:
            tmp &= right[p + 1]
        if tmp > ans:
            ans = tmp
            pos = p

    if pos != -1:
        a[0], a[pos] = a[pos], a[0]
    print(*a)

if __name__ == "__main__":
    main()