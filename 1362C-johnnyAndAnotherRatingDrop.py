# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    n = int(sys.stdin.readline())
    cnt = 0
    denom = 1
    while True:
        cnt += (n // denom)
        denom *= 2
        if denom > n:
            break
    print(cnt)

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()
