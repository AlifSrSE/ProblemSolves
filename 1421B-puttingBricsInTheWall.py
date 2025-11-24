# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    out = []

    for _ in range(t):
        n = int(data[idx]); idx += 1
        v = []
        for _ in range(n):
            row = list(data[idx])
            idx += 1
            for i in range(n):
                if row[i] == 'S' or row[i] == 'F':
                    row[i] = '0'
            v.append(row)

        a = int(v[0][1])         
        b = int(v[1][0])          
        c = int(v[n-2][n-1])      
        d = int(v[n-1][n-2])
        ans = []

        if a == b:
            target = 1 - a
            if c != target:
                ans.append(f"{n-1} {n}")
            if d != target:
                ans.append(f"{n} {n-1}")

        else:
            if a == 1:
                ans.append("1 2")
            if b == 1:
                ans.append("2 1")

            if c == 0:
                ans.append(f"{n-1} {n}")
            if d == 0:
                ans.append(f"{n} {n-1}")

        out.append(str(len(ans)))
        out.extend(ans)

    print("\n".join(out))

alif()
