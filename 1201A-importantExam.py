# Author : AlifSrSE
# Email : alif.rahman.c@gmail.com
# Link : https://codeforces.com/contest/1201/problem/A

def alif():
    n, m = map(int, input().split())
    w = []

    for _ in range(n):
        w.append(input())
    a = list(map(int, input().split()))
    total = 0

    for p in range(m):
        s = [0] * 5
        for u in range(n):
            s[ord(w[u][p]) - ord('A')] += 1
        mx = 0

        for val in s:
            mx = max(mx, val)
        total += a[p] * mx
    print(total)

if __name__ == "__main__":
    alif()