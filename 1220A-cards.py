# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    n = int(input())
    s = input()
    
    cnt = 0
    zro = 0
    
    for char in s:
        if char == 'z':
            zro += 1
        elif char == 'n':
            cnt += 1
            
    print("1 " * cnt, end="")
    print("0 " * zro)

solve()