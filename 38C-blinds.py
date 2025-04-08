# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

M = 101

n, l = map(int, input().split())
a = list(map(int, input().split())) 

maxArea = 0
for u in range(l, M):
    area = 0
    for p in range(n):
        area += u * (a[p] // u)  
    maxArea = max(maxArea, area)

print(maxArea)