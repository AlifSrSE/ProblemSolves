# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1237/problem/B

import sys

def alif():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))

    s = set()
    ind = 0
    cnt = 0 
    for p in range(n):
        while ind < n and a[ind] in s:
            ind += 1
        if ind < n and b[p] != a[ind]:
            cnt += 1
        s.add(b[p])
    sys.stdout.write(f"{cnt}\n")

if __name__ == "__main__":
    alif()