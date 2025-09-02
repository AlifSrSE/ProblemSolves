# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    n, x, m = map(int, sys.stdin.readline().split())
    left = x
    right = x

    for _ in range(m):
        ll, rr = map(int, sys.stdin.readline().split())
        if rr >= left and ll <= right:
            left = min(left, ll)
            right = max(right, rr)
    
    result = right - left + 1
    sys.stdout.write(str(result) + "\n")

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()  