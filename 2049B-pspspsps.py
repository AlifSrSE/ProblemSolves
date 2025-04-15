# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com
# Link: https://codeforces.com/problemset/problem/2049/B

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        s = list(s)
        if s[0] == 's':
            s[0] = '.'
        if s[-1] == 'p':
            s[-1] = '.'
        fs = False
        fp = False
        for p in range(len(s)):
            if s[p] == 's':
                fs = True
            elif s[p] == 'p':
                fp = True
        print("NO" if fs and fp else "YES")

solve()