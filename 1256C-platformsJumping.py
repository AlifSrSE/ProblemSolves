# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1256/problem/C

import sys

def alif():
    n, m, d = map(int, sys.stdin.readline().split())
    c = [0] + list(map(int, sys.stdin.readline().split()))
    
    for p in range(1, m + 1):
        n -= c[p]
    r = d - 1
    s = m + 1

    if n > s * r:
        sys.stdout.write("NO\n")
    else:
        sys.stdout.write("YES\n")
        result_sequence = []

        for p in range(m + 1):
            for _ in range(c[p]):
                result_sequence.append(str(p))
            
            k = min(n, r)
            n -= k
            
            for _ in range(k):
                result_sequence.append("0")
        sys.stdout.write(" ".join(result_sequence) + "\n")

if __name__ == "__main__":
    alif()