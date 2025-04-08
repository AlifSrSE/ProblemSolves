# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    sgn = [''] * n
    right_sum = 0
    
    for p in range(n-1, -1, -1):
        if right_sum > 0:
            right_sum -= a[p]
            sgn[p] = '-'
        else:
            right_sum += a[p]
            sgn[p] = '+'
    
    if right_sum < 0:
        for p in range(n):
            if sgn[p] == '+':
                sgn[p] = '-'
            elif sgn[p] == '-':
                sgn[p] = '+'
    
    print(''.join(sgn))

solve()