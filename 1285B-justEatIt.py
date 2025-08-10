# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1285/problem/B

import sys

def alif():
    try:
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
    except (IOError, ValueError):
        return

    ans = True
    current_sum = 0

    for p in range(n):
        current_sum += a[p]
        if current_sum <= 0 and p < n - 1:
            ans = False
            break

    if ans:
        current_sum = 0
        for p in range(n - 1, -1, -1):
            current_sum += a[p]
            if current_sum <= 0 and p > 0:
                ans = False
                break
    
    if n == 1:
        ans = False

    if ans:
        print("YES")
    else:
        print("NO")

def main():
    try:
        t = int(sys.stdin.readline())
        
        for _ in range(t):
            alif()
    except (IOError, ValueError):
        return

if __name__ == "__main__":
    main()

