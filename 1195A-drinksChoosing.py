# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1195/problem/A

def alif():
    n, k = map(int, input().split())
    a = [0] * (k + 1)
    
    for _ in range(n):
        x = int(input())
        a[x] = 1 - a[x]
    
    cnt = 0
    for p in range(1, k + 1):
        cnt += a[p]
    
    ans = n - cnt // 2
    print(ans)

if __name__ == "__main__":
    alif()
