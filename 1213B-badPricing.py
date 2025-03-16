# Author : AlifSrSE
# Date : 2025-03-14
# Problem link : https://codeforces.com/contest/1213/problem/B
 
INF = int(1e9)
 
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        mns = [0] * n
        mn = INF
        for i in range(n-1, -1, -1):
            mn = min(mn, a[i])
            mns[i] = mn
        
        ans = 0
        for i in range(n-1):
            if a[i] > mns[i + 1]:
                ans += 1
        
        print(ans)
 
if __name__ == "__main__":
    main()