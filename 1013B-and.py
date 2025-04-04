# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    
    if len(set(a)) != n:
        return 0
    
    values = set(a)
    if any((ai & x) != ai and (ai & x) in values for ai in a):
        return 1
    
    masked = [ai & x for ai in a]
    if len(set(masked)) != n:
        return 2
        
    return -1

print(solve())