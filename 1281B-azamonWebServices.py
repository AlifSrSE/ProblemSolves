# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/problemset/problem/1281/B

import sys

def solve():
    t = int(sys.stdin.readline())
    
    for _ in range(t):
        a_str, b_str = sys.stdin.readline().split()
        a = list(a_str)
        b = b_str

        n = len(a)
        m = len(b)

        d = [''] * n
        w = [0] * n
        d[n - 1] = a[n - 1]
        w[n - 1] = n - 1
        
        for p in range(n - 2, -1, -1):
            if a[p] < d[p + 1]:
                d[p] = a[p]
                w[p] = p
            elif a[p] == d[p + 1]:
                d[p] = d[p + 1]
                w[p] = w[p + 1]
            else:
                d[p] = d[p + 1]
                w[p] = w[p + 1]

        sub = False
        possible = False 
        
        for p in range(m):
            if p >= n:
                possible = True
                break
            
            if d[p] > b[p]:
                possible = False
                break
            
            elif not sub and d[p] < b[p]:
                c = a[p]
                a[p] = d[p]
                a[w[p]] = c
                sub = True
                possible = True
                break
            
            elif not sub and d[p] == b[p] and a[p] > b[p]:
                c = a[p]
                a[p] = d[p]
                a[w[p]] = c
                sub = True
        
        result_a_str = "".join(a)
        if result_a_str < b:
            print(result_a_str)
        else:
            print("---")

if __name__ == "__main__":
    solve()