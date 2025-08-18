# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1315/problem/A

def alif():
    t = int(input())
    for _ in range(t):
        a, b, x, y = map(int, input().split())
        
        u = max(x, a - 1 - x)
        v = max(y, b - 1 - y)
        
        res = max(u * b, v * a)
        
        print(res)

alif()