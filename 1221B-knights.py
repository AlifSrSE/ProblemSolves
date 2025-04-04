# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n = int(input())
    
    s1 = ""
    s2 = ""
    
    for i in range(1, n + 1):
        if i % 2 == 1:
            s1 += 'W'
            s2 += 'B'
        else:
            s1 += 'B'
            s2 += 'W'
            
    for i in range(1, n + 1):
        if i % 2 == 1:
            print(s1)
        else:
            print(s2)

solve()