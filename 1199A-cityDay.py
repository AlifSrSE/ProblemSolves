# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1199/problem/A

def alif():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    
    ans = 0
    for p in range(n):
        least = True
        
        for u in range(1, x + 1):
            if not least:
                break
            if p - u >= 0 and a[p - u] < a[p]:
                least = False
        
        for u in range(1, y + 1):
            if not least:
                break
            if p + u < n and a[p + u] < a[p]:
                least = False
        
        if least:
            ans = p + 1
            break
            
    print(ans)

if __name__ == "__main__":
    alif()