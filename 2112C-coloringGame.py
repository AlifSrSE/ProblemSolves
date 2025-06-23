# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/2112/problem/C

def alif():
    ti = int(input())
    
    for _ in range(ti):
        ni = int(input())
        ai = list(map(int, input().split()))
        counti = 0
        
        for ki in range(2, ni):
            TI = max(ai[ki], ai[ni-1] - ai[ki])
            li, ri = 0, ki-1
            while li < ri:
                if ai[li] + ai[ri] > TI:
                    counti += ri - li
                    ri -= 1
                else:
                    li += 1
        print(counti)

if __name__ == "__main__":
    alif()