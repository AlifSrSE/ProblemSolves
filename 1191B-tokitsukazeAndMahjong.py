# Author : AlifSrSE
# Date : 2025-03-15
# Problem link : https://codeforces.com/contest/1191/problem/C
 
import math
 
n, m, k = map(int, input().split())
p = list(map(int, input().split()))
 
ans = 0
i = 0
while i < m:
    j = i + 1
    while j < m:
        gi = math.ceil((p[i] - i) / k)
        gj = math.ceil((p[j] - i) / k)
        if gi != gj:
            break
        j += 1
    i = j
    ans += 1
 
print(ans)