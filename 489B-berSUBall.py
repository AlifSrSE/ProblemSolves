# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def mySolve():
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    brr = list(map(int, input().split()))
    
    arr.sort()
    brr.sort()
    
    cnt = 0
    for i in range(n):
        for j in range(m):
            if abs(arr[i] - brr[j]) <= 1:
                brr[j] = 10**3 
                cnt += 1
                break
    
    print(cnt)

t = int(input())
for _ in range(t):
    mySolve()