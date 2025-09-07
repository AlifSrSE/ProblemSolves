# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
n, k = map(int, input().split())
a = list(map(int, input().split()))
def can(x):
    cnt = 0
    i = 0
    while i < n and cnt < k:
        if cnt % 2 == 0:
            if a[i] <= x:
                cnt += 1
                i += 1
            else:
                i += 1
        else:
            cnt += 1
            i += 1
    if cnt >= k:
        return True
    cnt = 0
    i = 0
    while i < n and cnt < k:
        if cnt % 2 == 1:
            if a[i] <= x:
                cnt += 1
                i += 1
            else:
                i += 1
        else:
            cnt += 1
            i += 1
    return cnt >= k
l, r = 1, 10**9
while l < r:
    m = (l + r) // 2
    if can(m):
        r = m
    else:
        l = m + 1
print(l)