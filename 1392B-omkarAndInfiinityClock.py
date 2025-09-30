# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys

def alif():
    data = list(map(int, sys.stdin.read().split()))

    if not data:
        return
    t = data[0]
    p = 1
    res = []

    for _ in range(t):
        n = data[p]
        k = data[p + 1]
        p += 2
        a = data[p : p + n]
        p += n
        mx = max(a)
        a = [mx - x for x in a]
        k = (k - 1) % 2

        if k:
            mx = max(a)
            a = [mx - x for x in a]

        res.append(" ".join(map(str, a)))
    sys.stdout.write('\n'.join(res) + '\n')

alif()
