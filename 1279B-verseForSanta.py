# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/problemset/problem/1279/B

import sys

def alif():
    t = int(sys.stdin.readline())

    for _ in range(t):
        n, s_limit = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        
        current_sum = 0
        max_val = 0
        max_val_pos = 0
        
        for p in range(n):
            current_sum += a[p]
            if a[p] > max_val:
                max_val = a[p]
                max_val_pos = p + 1
            
            if current_sum > s_limit:
                break
        
        result = max_val_pos * (1 if current_sum > s_limit else 0)
        sys.stdout.write(f"{result}\n")

if __name__ == "__main__":
    alif()