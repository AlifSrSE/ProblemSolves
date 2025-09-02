# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com

import sys

def alif():
    n = int(sys.stdin.readline())
    s = set(map(int, sys.stdin.readline().split()))
    
    res = -1
    for k in range(1, 1024):
        w = set()
        for x in s:
            w.add(x ^ k)
        
        if s == w:
            res = k
            break
            
    print(res)

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        alif()

if __name__ == "__main__":
    main()
