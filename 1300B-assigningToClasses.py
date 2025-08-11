# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1300/problem/B

import sys

def solve():
    try:
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
    except (IOError, ValueError):
        return
    
    a.sort()
    result = a[n] - a[n - 1]
    print(result)

def main():
    try:
        t = int(sys.stdin.readline())
    except (IOError, ValueError):
        return

    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()