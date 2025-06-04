# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1203/problem/E

def alif():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    last = 0
    cnt = 0

    for x in a:
        if last < x - 1:
            cnt += 1
            last = x - 1
        elif last < x:
            cnt += 1
            last = x
        elif last < x + 1:
            cnt += 1
            last = x + 1
    
    print(cnt)

if __name__ == "__main__":
    alif()