# Author : AlifSrSE
# Date : 2025-03-16
# Problem link : https://codeforces.com/contest/1692/problem/E

from sys import stdin
input = stdin.readline

def main():
    t = int(input().strip())  
    
    for _ in range(t):
        n, s = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))

        sum_total = sum(a)
        ps = [0] * n
        ps[0] = a[0]
        for i in range(1, n):
            ps[i] = ps[i-1] + a[i]
        
        if s > sum_total:
            print(-1)
        elif s == sum_total:
            print(0)
        else:
            ans = -1
            for i in range(n):
                if ps[i] == s:
                    ans = max(ans, i + 1)
                elif ps[i] > s:
                    ds = ps[i] - s
                    l = 0
                    while l < i and ps[l] < ds:
                        l += 1
                    if ps[l] >= ds:
                        ans = max(ans, i - l)
            
            print(n - ans)

if __name__ == "__main__":
    main()