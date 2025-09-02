# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    n, x = map(int, sys.stdin.readline().split())
    degree = 0
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        if u == x or v == x:
            degree += 1
    
    if n == 1:
        print("Ayush")
        return

    if degree <= 1 or n % 2 == 0:
        print("Ayush")
    else:
        print("Ashish")

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()
