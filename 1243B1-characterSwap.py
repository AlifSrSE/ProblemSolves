# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1243/problem/B1

import sys

def alif():
    q = int(sys.stdin.readline())

    while q > 0:
        n = int(sys.stdin.readline())
        s = sys.stdin.readline().strip()
        t = sys.stdin.readline().strip()

        diff = 0
        x, y = '', ''
        N_ALPHA = 26
        v = [0] * N_ALPHA 

        for p in range(n):
            if s[p] == t[p]:
                v[ord(s[p]) - ord('a')] += 1
            else:
                if diff == 0:
                    x = s[p]
                    y = t[p]
                    diff = 1
                elif diff == 1:
                    if s[p] == x and t[p] == y:
                        diff = 2
                    else:
                        diff = -1
                        break
                else:
                    diff = -1
                    break
        if diff == 0:
            for p_alpha in range(N_ALPHA):
                if v[p_alpha] >= 2:
                    diff = 2
                    break
        if diff == 2:
            sys.stdout.write("Yes\n")
        else:
            sys.stdout.write("No\n")
        q -= 1

if __name__ == "__main__":
    alif()