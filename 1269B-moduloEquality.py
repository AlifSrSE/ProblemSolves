# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/problemset/problem/1269/B

import sys

def check(x_arr, y_arr, add_val, mod_val):
    transformed_x = [(val + add_val) % mod_val for val in x_arr]
    transformed_x.sort()
    
    for p in range(len(transformed_x)):
        if transformed_x[p] != y_arr[p]:
            return False
    return True

def alif():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    b.sort()
    res = m + 1 
    
    for p in range(n):
        diff = (2 * m + b[0] - a[p]) % m
        
        if diff >= res:
            continue
        
        if check(a, b, diff, m):
            res = diff
    
    sys.stdout.write(f"{res}\n")

if __name__ == "__main__":
    alif()