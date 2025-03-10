# Author : AlifSrSE
# Date : 2025-03-09
# Problem link : https://codeforces.com/contest/1941/problem/F

from bisect import bisect_right

def main():
    TC = int(input())
    for _ in range(TC):
        n, m, k = map(int, input().split())
        a = list(map(int, input().split()))
        d = list(map(int, input().split()))
        f = list(map(int, input().split()))
        
        ix = 0
        df = a[1] - a[0]
        df2 = 0 

        for i in range(1, n-1):
            curr_diff = a[i+1] - a[i]
            if curr_diff > df:
                ix = i
                df2 = df
                df = curr_diff
            elif curr_diff > df2:
                df2 = curr_diff
    
        t = a[ix] + ((a[ix+1] - a[ix]) // 2)
        
        f.sort()
        for i in range(m):
            j = bisect_right(f, t - d[i])
            if j < k and a[ix] <= d[i] + f[j] <= a[ix+1]:
                curr_max = max(a[ix+1] - (d[i] + f[j]), (d[i] + f[j]) - a[ix])
                df = min(df, curr_max)
            
            j -= 1
            if j >= 0 and a[ix] <= d[i] + f[j] <= a[ix+1]:
                curr_max = max(a[ix+1] - (d[i] + f[j]), (d[i] + f[j]) - a[ix])
                df = min(df, curr_max)
        
        print(max(df2, df))

if __name__ == "__main__":
    main()