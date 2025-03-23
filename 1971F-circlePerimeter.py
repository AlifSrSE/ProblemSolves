# Author: AlifSrSe
# date: 2025-03-20
# https://codeforces.com/problemset/problem/1971/D

def solve():
    rd = int(input())
    ans = 0
    for i in range(rd + 1):
        l, r = 0, rd + 5
        while r > l + 1:
            midr = l + (r - l) // 2
            if i * i + midr * midr < (rd + 1) * (rd + 1):
                l = midr
            else:
                r = midr
        cnt2 = l

        l, r = 0, rd + 5
        while r > l + 1:
            midr = l + (r - l) // 2
            if i * i + midr * midr < rd * rd:
                l = midr
            else:
                r = midr
        cnt1 = l

        ans += (cnt2 - cnt1) * 4
    print(ans)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()