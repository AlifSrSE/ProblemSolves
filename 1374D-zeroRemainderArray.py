# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
 
import sys
from collections import defaultdict

t = int(sys.stdin.readline())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    
    cnt = defaultdict(int)
    for x in a:
        rem = x % k
        if rem == 0:
            continue
        cnt[k - rem] += 1
    
    mx = 0
    for rem, count in cnt.items():
        cur = rem + k * (count - 1)
        mx = max(mx, cur)
    
    print(mx + (1 if mx > 0 else 0))
