# Author : AlifSrSE
# Date : 2025-03-30
# Problem link : https://codeforces.com/contest/2075/problem/B

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        rest = k
        if rest == 1:
            if i == 0:
                ans = max(ans, a[i] + a[n - 1])
            elif i == n - 1:
                ans = max(ans, a[i] + a[0])
            else:
                ans = max(ans, a[i] + max(a[0], a[n - 1]))
        else:
            tm = []
            for x in range(n):
                if x != i:
                    tm.append(a[x])
            tm.sort(reverse=True)
            tans = 0
            for x in range(k):
                tans += tm[x]
            ans = max(ans, a[i] + tans)
    print(ans)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()