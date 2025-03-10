# Author : AlifSrSE
# Date : 2025-03-09
# Problem link : https://codeforces.com/contest/1843/problem/B

def solve(a):
    non_zeros = [x for x in a if x != 0]
    
    abs_sum = sum(abs(x) for x in a)
    neg_transitions = sum(
        1 for i in range(len(non_zeros))
        if non_zeros[i] < 0 and (i == 0 or non_zeros[i-1] > 0)
    )
    
    return f"{abs_sum} {neg_transitions}"
 
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    print(solve(a))