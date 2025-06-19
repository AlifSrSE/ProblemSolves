# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1225/problem/B1

import collections

def alif():
    t = int(input())
    while t > 0:
        n, k, d = map(int, input().split())
        a = list(map(int, input().split()))
        s = collections.defaultdict(int)
        
        for p in range(d):
            s[a[p]] = p
        mn = len(s)
        
        for p in range(d, n):
            rem = a[p - d]
            nxt = a[p]

            if s[rem] == p - d:
                del s[rem]
            s[nxt] = p
            mn = min(mn, len(s))
        print(mn)
        t -= 1

if __name__ == "__main__":
    alif()