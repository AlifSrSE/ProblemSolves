# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def mySolve():
    n, m, x = map(int, input().split())
    
    left = 0
    right = 10**18
    cnt = -1
    
    while left <= right:
        mid = (left + right) >> 1
        
        tobi = m // (mid + 1)
        kobi = (mid + 1) * tobi
        robi = m - kobi
        
        k = (kobi - tobi + robi) * n
        
        if k >= x:
            cnt = mid
            right = mid - 1
        else:
            left = mid + 1
            
    print(cnt)

t = int(input())
for _ in range(t):
    mySolve()