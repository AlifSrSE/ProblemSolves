# Author : AlifSrSE
# Date : 2025-03-16
# Problem link : https://codeforces.com/contest/1692/problem/G

from sys import stdin
input = stdin.readline

def main():
    t = int(input().strip()) 
    
    for _ in range(t):
        n, k = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        
        ans = 0
        cnt = 1
        
        for i in range(1, n):
            if cnt == k + 1:
                ans += 1
                cnt -= 1

            if a[i] > (a[i-1] // 2):
                cnt += 1
            else:
                cnt = 1
        
        if cnt == k + 1:
            ans += 1
            
        print(ans)

if __name__ == "__main__":
    main()