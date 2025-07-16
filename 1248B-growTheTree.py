# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1248/problem/B

def alif():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    x = 0
    y = 0
    
    for p in range(n // 2):
        x += a[p]
    
    for p in range(n // 2, n):
        y += a[p]
    
    print(x * x + y * y)

if __name__ == "__main__":
    alif()