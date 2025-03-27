# Author : AlifSrSE
# Date : 2025-02-27
# Problem link : https://codeforces.com/contest/1560/problem/A

def solve():
    r = 10000
    a = []
    for i in range(1, r):
        if i % 3 != 0 and i % 10 != 3:
            a.append(i)
    
    t = int(input())
    for _ in range(t):
        k = int(input())
        print(a[k - 1])

if __name__ == "__main__":
    solve()