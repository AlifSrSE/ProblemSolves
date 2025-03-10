# Author : AlifSrSE
# Date : 2025-03-09
# Problem link : https://codeforces.com/contest/1941/problem/E

from collections import deque 

def main():
    TC = int(input()) 
    for _ in range(TC):
        n, m, k, d = map(int, input().split())
        a = []
        for _ in range(n):
            row = list(map(int, input().split()))
            a.append(row)
        
        res = [0] * n
        for r in range(n):
            dp = [0] * m
            dp[0] = 1
            
            st = [(1, 0)] 
            
            for i in range(1, m):
                min_val = st[0][0]
                dp[i] = (a[r][i] + 1) + min_val
                
                while st and st[0][1] <= i - (d + 1):
                    st.pop(0)

                st.append((dp[i], i))
                st.sort()
            
            res[r] = dp[m-1]

        ans = sum(res[:k])
        mnAns = ans
        for i in range(k, n):
            ans += res[i] - res[i-k]
            mnAns = min(mnAns, ans)
        
        print(mnAns)

if __name__ == "__main__":
    main()