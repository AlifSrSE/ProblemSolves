# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1253/problem/A

import sys

def alif():
    t = int(sys.stdin.readline())

    for _ in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        b = list(map(int, sys.stdin.readline().split()))
        for p in range(n):
            a[p] -= b[p]

        ans = True
        first_neg_idx = -1

        for p in range(n):
            if a[p] < 0:
                first_neg_idx = p
                break
        
        if first_neg_idx != -1:
            diff_value = a[first_neg_idx]
            
            for u in range(first_neg_idx, n):
                if a[u] == diff_value:
                    a[u] = 0
                elif a[u] == 0:
                    for v in range(u, n):
                        if a[v] != 0:
                            ans = False
                            break
                    break
                else:
                    ans = False
                    break
                
        for p in range(n):
            if a[p] != 0:
                ans = False
                break
        
        sys.stdout.write("YES\n" if ans else "NO\n")
        t -= 1

if __name__ == "__main__":
    alif()