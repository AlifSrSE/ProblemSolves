# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1243/problem/A

def alif():
    q = int(input())

    for _ in range(q):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort(reverse=True)
        side = 0
        
        for p in range(n):
            if a[p] >= p + 1:
                side = p + 1
            else:
                break
        
        print(side)

if __name__ == "__main__":
    alif()