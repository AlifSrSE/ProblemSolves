# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1251/problem/B

import sys

def alif():
    q = int(sys.stdin.readline())

    for _ in range(q):
        n = int(sys.stdin.readline())
        z = 0
        f = 0 
        
        for _ in range(n):
            s = sys.stdin.readline().strip()
            
            if len(s) % 2 != 0:
                f = 1
                
            for char_s in s:
                if char_s == '0':
                    z = 1 - z
                    
        result = n - 1 + (1 if (f or not z) else 0)
        
        sys.stdout.write(f"{result}\n")

if __name__ == "__main__":
    alif()