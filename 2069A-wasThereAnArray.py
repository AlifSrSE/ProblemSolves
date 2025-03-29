# Author : AlifSrSE
# Date : 2025-03-29
# Problem link : https://codeforces.com/contest/2069/problem/A

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    ok = True
    i = 0
    while i < n - 2:
        if a[i] == 1:
            i += 1
            cnt = 0
            while i < n - 2 and a[i] != 1:
                cnt += 1
                i += 1
            if cnt and cnt < 2 and i < n - 2 and a[i] == 1:
                ok = False
        else:
            i += 1
    
    print("YES" if ok else "NO")

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()