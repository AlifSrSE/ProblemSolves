# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/problemset/problem/1279/A

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        a = list(map(int, sys.stdin.readline().split()))
        a.sort()
        ans = (a[2] <= (a[0] + a[1] + a[2] + 1) // 2)
        sys.stdout.write("Yes\n" if ans else "No\n")

if __name__ == "__main__":
    alif()