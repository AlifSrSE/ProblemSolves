# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    sum_so_far = 0
    result_prev_sum = 0
    result = []
    
    for i in range(n):
        sum_so_far += a[i]
        result.append(sum_so_far // m - result_prev_sum)
        result_prev_sum += result[-1]
    
    return result

print(' '.join(map(str, solve())))