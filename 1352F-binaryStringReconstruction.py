# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t_str = sys.stdin.readline()
    if not t_str:
        return
    t = int(t_str)

    for _ in range(t):
        a, b, c = map(int, sys.stdin.readline().strip().split())

        if b == 0:
            if a > 0:
                sys.stdout.write('0' * (a + 1))
            else:
                sys.stdout.write('1' * (c + 1))
        else:
            res = ""
            for p in range(b + 1):
                res += '0' if (p % 2 == 0) else '1'
                
            res = res.replace('0', '0' * (a + 1), 1)
            res = res.replace('1', '1' * (c + 1), 1)

            sys.stdout.write(res)
        sys.stdout.write('\n')

if __name__ == "__main__":
    alif()