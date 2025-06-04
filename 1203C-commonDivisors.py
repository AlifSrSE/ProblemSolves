# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1203/problem/C

import math

def alif():
    n = int(input())
    a_list_str = input().split()
    a_list = [int(val) for val in a_list_str]
    g = a_list[0]

    for i in range(1, n):
        g = math.gcd(g, a_list[i])
    
    cnt = 0
    for p in range(1, int(math.sqrt(g)) + 1):
        if g % p == 0:
            cnt += 1
            if p * p != g:
                cnt += 1
    print(cnt)

if __name__ == "__main__":
    alif()