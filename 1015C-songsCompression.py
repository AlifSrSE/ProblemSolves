# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n, m = map(int, input().split())
    a = []
    b = []
    for _ in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    
    if sum(b) > m:
        return -1
    
    sum_a = sum(a)
    if sum_a <= m:
        return 0
    
    diffs = sorted(a[i] - b[i] for i in range(n))
    
    curr_sum = sum_a
    for i in range(n-1, -1, -1):
        curr_sum -= diffs[i]
        if curr_sum <= m:
            return n - i
            
print(solve())