# Author : AlifSrSE
# Date : 2025-03-12
# Problem link : https://codeforces.com/contest/2036/problem/A

def solve(a):
    return all(abs(a[i + 1] - a[i]) in (5, 7) for i in range(len(a) - 1))

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        print("YES" if solve(a) else "NO")

if __name__ == "__main__":
    main()