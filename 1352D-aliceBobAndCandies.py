# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    t_str = sys.stdin.readline()
    if not t_str:
        return
    t = int(t_str)

    for _ in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().strip().split()))
        cnt, alice, bob = 0, 0, 0
        x, y = 0, n - 1
        cur, prev = 0, 0

        while x <= y:
            while x <= y and cur <= prev:
                cur += a[x]
                alice += a[x]
                x += 1
            
            if cur > 0:
                cnt += 1
            prev = cur
            cur = 0

            while x <= y and cur <= prev:
                cur += a[y]
                bob += a[y]
                y -= 1
            if cur > 0:
                cnt += 1
            prev = cur
            cur = 0

        print(cnt, alice, bob)

if __name__ == "__main__":
    alif()