# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1322/problem/A

import sys

def alif():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    
    start = -1
    count = 0
    current_sum = 0
    
    for p in range(n):
        if s[p] == '(':
            current_sum += 1
        else:
            current_sum -= 1
        
        if s[p] == ')' and current_sum == -1:
            start = p
        elif s[p] == '(' and current_sum == 0 and start != -1:
            count += (p - start + 1)
            start = -1
    
    if current_sum != 0:
        print(-1)
    else:
        print(count)

alif()