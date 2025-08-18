# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1305/problem/B

import sys

def alif():
    s = sys.stdin.readline().strip()
    v = []
    idx = len(s) - 1
    for p in range(len(s)):
        if s[p] == ')':
            continue
        while idx > p:
            if s[idx] == ')':
                v.append(p + 1)
                v.append(idx + 1)
                idx -= 1
                break
            idx -= 1
    
    v.sort()
    
    if not v:
        print(0)
    else:
        print(1)
        print(len(v))
        print(*v)

if __name__ == "__main__":
    alif()