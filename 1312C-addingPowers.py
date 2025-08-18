# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1312/problem/C

import sys

def alif():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        
        powers_used = set()
        possible = True
        
        for x in a:
            i = 0
            while x > 0:
                remainder = x % k
                if remainder > 1:
                    possible = False
                    break
                if remainder == 1:
                    if i in powers_used:
                        possible = False
                        break
                    powers_used.add(i)
                x //= k
                i += 1
            if not possible:
                break
        
        if possible:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    alif()