# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def get_product(x):
    s = str(x)
    return int(min(s)) * int(max(s))

def alif():
    n, k = map(int, sys.stdin.readline().split())
    
    for _ in range(k - 1):
        product = get_product(n)
        if product == 0:
            break
        n += product
    print(n)

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()