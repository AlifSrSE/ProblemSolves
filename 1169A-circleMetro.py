# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1169/problem/A

def alif(n, a, x, b, y):
    while a != x and b != y:
        a += 1
        if a == n + 1:
            a = 1
        
        b -= 1
        if b == 0:
            b = n
        
        if a == b:
            return True
    
    return False

n, a, x, b, y = map(int, input().split())
print("YES" if alif(n, a, x, b, y) else "NO")