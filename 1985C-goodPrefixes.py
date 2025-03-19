# Author : AlifSrSE
# Date : 2025-03-18
# Problem link : https://codeforces.com/contest/1985/problem/C

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    mx = [0] * n
    pf = [0] * n
    cnt = 0
    
    mx[0] = a[0]
    for i in range(1, n):
        mx[i] = max(mx[i - 1], a[i])
    
    pf[0] = a[0]
    for i in range(1, n):
        pf[i] = pf[i - 1] + a[i]
    
    for i in range(n):
        x = pf[i] - mx[i]
        if x == mx[i]:
            cnt += 1
    
    print(cnt)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()