# Author: AlifSrSE
# Email: alif.rahman.c@gmail.com

def solve():
    l, r = map(int, input().split())
    
    for x in range(l, r + 1):
        s = str(x)
        if len(set(s)) == len(s):
            print(x)
            return
    print(-1)

solve()