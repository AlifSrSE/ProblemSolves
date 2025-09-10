# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        if i % 2 == 0:
            if a[i] < 0:
                a[i] *= -1
        else:
            if a[i] > 0:
                a[i] *= -1
    print(*a)
