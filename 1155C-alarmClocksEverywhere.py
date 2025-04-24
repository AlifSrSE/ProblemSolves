# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1155/problem/C

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def alif(x, p):
    g = x[1] - x[0]
    for i in range(1, len(x) - 1):
        g = gcd(g, x[i + 1] - x[i])
    
    for i in range(len(p)):
        if g % p[i] == 0:
            return f"YES\n{x[0]} {i + 1}"
    
    return "NO"

n, m = map(int, input().split())
x = list(map(int, input().split()))
p = list(map(int, input().split()))
print(alif(x, p))