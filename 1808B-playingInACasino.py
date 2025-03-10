# Author : AlifSrSE
# Date : 2025-03-10
# Problem link : https://codeforces.com/contest/1808/problem/B

import math

def main():

    t = int(input())
    for tcase in range(1, t + 1):
        n, m = map(int, input().split())
        a = [[] for _ in range(m)]
        for i in range(n):
            row = list(map(int, input().split()))
            for j in range(m):
                a[j].append(row[j])
        
        ans = 0
        for i in range(m):
            a[i].sort()
            for j in range(n):
                ans += (j * a[i][j]) - (n - j - 1) * a[i][j]
        
        print(ans)

if __name__ == "__main__":
    main()