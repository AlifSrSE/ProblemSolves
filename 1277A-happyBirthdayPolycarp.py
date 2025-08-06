# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/problemset/problem/1277/A

import sys

def alif():
    t = int(sys.stdin.readline())

    for _ in range(t):
        n = int(sys.stdin.readline())
        cur = 0
        cnt = 0
        
        for p in range(10):
            cur = 10 * cur + 1

            for u in range(1, 10):
                if u * cur <= n:
                    cnt += 1
                else:
                    break
        sys.stdout.write(f"{cnt}\n")

if __name__ == "__main__":
    alif()