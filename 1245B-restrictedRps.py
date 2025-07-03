# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1245/problem/B

import sys

def alif():
    t = int(sys.stdin.readline())

    for _ in range(t):
        n = int(sys.stdin.readline())
        a, b, c = map(int, sys.stdin.readline().split())
        g = sys.stdin.readline().strip()

        cnt = 0
        h = list(g)

        for p in range(n):
            if g[p] == 'R':
                if b > 0:
                    cnt += 1
                    b -= 1
                    h[p] = 'P'
                else:
                    h[p] = '_'
            elif g[p] == 'P':
                if c > 0:
                    cnt += 1
                    c -= 1
                    h[p] = 'S'
                else:
                    h[p] = '_'
            elif g[p] == 'S':
                if a > 0:
                    cnt += 1
                    a -= 1
                    h[p] = 'R'
                else:
                    h[p] = '_'
                    
        for p in range(n):
            if h[p] == '_':
                if a > 0:
                    h[p] = 'R'
                    a -= 1
                elif b > 0:
                    h[p] = 'P'
                    b -= 1
                elif c > 0:
                    h[p] = 'S'
                    c -= 1
        
        if 2 * cnt >= n:
            sys.stdout.write("YES\n")
            sys.stdout.write("".join(h) + "\n")
        else:
            sys.stdout.write("NO\n")
        
if __name__ == "__main__":
    alif()