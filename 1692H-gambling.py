# Author : AlifSrSE
# Date : 2025-03-16
# Problem link : https://codeforces.com/contest/1692/problem/H

import sys
from collections import defaultdict

def check(b):
    c = [1]
    for i in range(1, len(b)):
        c.append((b[i] - b[i - 1] - 1) * -1)
        c.append(1)
    
    mx = float('-inf')
    mxe = 0
    start = end = s = 0
    
    for i in range(len(c)):
        mxe += c[i]
        
        if mx < mxe:
            mx = mxe
            start = s
            end = i
        
        if mxe < 0:
            mxe = 0
            s = i + 1
            
    return mx, start, end

def solve():
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    
    c = defaultdict(int)
    e = {}
    b = []
    f = []
    best = 0
    l = r = num = 0
    count = -1
    
    for i in range(n):
        c[a[i]] += 1
        if c[a[i]] == 1:
            count += 1
            e[a[i]] = count
            f.append(a[i])
            b.append([])
        b[e[a[i]]].append(i)
    
    for i in range(count + 1):
        d = check(b[i])
        if d[0] > best:
            best = d[0]
            num = f[i]
            l = b[i][d[1] // 2]
            r = b[i][d[2] // 2]
    
    print(num, l + 1, r + 1)

def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()