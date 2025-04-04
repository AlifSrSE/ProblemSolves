# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

import math

def bigmd(b, p, md):
    ans = 1
    while p:
        if p & 1:
            ans = (ans * b) % md
        p >>= 1
        b = (b * b) % md
    return ans % md

def is_prime(p):
    for i in range(2, int(math.sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True

def solve():
    x, n = map(int, input().split())
    md = 1000000007
    
    num = []
    cnt = 0
    
    for i in range(2, int(math.sqrt(x)) + 1):
        if is_prime(i) and x % i == 0:
            num.append(i)
            cnt += 1
        if is_prime(x // i) and x % i == 0 and i != (x // i):
            num.append(x // i)
            cnt += 1
    if cnt == 0:
        num.append(x)
        cnt += 1
    
    res = 1
    for i in range(cnt):
        tmp = n
        ans = 0
        while tmp >= num[i]:
            tmp //= num[i]
            ans += tmp
        res = (res * bigmd(num[i], ans, md)) % md
    
    print(res)

solve()